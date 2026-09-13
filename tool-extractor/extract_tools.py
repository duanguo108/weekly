#!/usr/bin/env python3
"""从周刊文章中增量提取「工具」条目，按每 50 期拆分追加写入工具清单文档。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

CHUNK_SIZE = 50
TOOL_SECTIONS = {"工具", "软件"}
TOOL_HEADING = re.compile(r"^##\s+(.+?)\s*$")
TOOL_ENTRY = re.compile(r"^(\d+)、\s*\[([^\]]+)\]\(([^)]+)\)(.*)$")
ISSUE_NUMBER = re.compile(r"issue-(\d+)\.md$", re.IGNORECASE)
ISSUE_TITLE = re.compile(r"第\s*(\d+)\s*期")


@dataclass
class ToolEntry:
    index: int
    name: str
    url: str
    description: str
    section: str


@dataclass
class ExtractState:
    processed_issues: list[str]
    known_urls: list[str]
    last_run: str | None = None

    @classmethod
    def load(cls, path: Path) -> ExtractState:
        if not path.exists():
            return cls(processed_issues=[], known_urls=[])
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            processed_issues=list(data.get("processed_issues", [])),
            known_urls=list(data.get("known_urls", [])),
            last_run=data.get("last_run"),
        )

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "processed_issues": self.processed_issues,
            "known_urls": self.known_urls,
            "last_run": self.last_run,
        }
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def normalize_url(url: str) -> str:
    return url.strip().rstrip("/")


def issue_sort_key(path: Path) -> tuple[int, str]:
    match = ISSUE_NUMBER.search(path.name)
    if match:
        return int(match.group(1)), path.name
    return 0, path.name


def parse_issue_number(path: Path, content: str) -> int | None:
    match = ISSUE_NUMBER.search(path.name)
    if match:
        return int(match.group(1))
    title_match = ISSUE_TITLE.search(content.splitlines()[0] if content else "")
    if title_match:
        return int(title_match.group(1))
    return None


def chunk_range(issue_number: int, chunk_size: int = CHUNK_SIZE) -> tuple[int, int]:
    start = ((issue_number - 1) // chunk_size) * chunk_size + 1
    end = start + chunk_size - 1
    return start, end


def chunk_filename(start: int, end: int) -> str:
    return f"tools-list-{start:03d}-{end:03d}.md"


def chunk_path(output_dir: Path, issue_number: int, chunk_size: int) -> Path:
    start, end = chunk_range(issue_number, chunk_size)
    return output_dir / chunk_filename(start, end)


def is_tool_section(heading: str) -> bool:
    return heading in TOOL_SECTIONS


def should_skip_description_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if TOOL_ENTRY.match(stripped):
        return True
    if TOOL_HEADING.match(stripped):
        return True
    if stripped.startswith("![](") or stripped.startswith("[![]("):
        return True
    if stripped.startswith("[") and "](" in stripped and stripped.endswith(")"):
        return True
    if stripped.startswith("http://") or stripped.startswith("https://"):
        return True
    return False


def parse_tools_from_content(content: str) -> list[ToolEntry]:
    tools: list[ToolEntry] = []
    current_section: str | None = None
    current: ToolEntry | None = None
    description_lines: list[str] = []

    def flush_current() -> None:
        nonlocal current, description_lines
        if current is None:
            return
        current.description = " ".join(description_lines).strip()
        tools.append(current)
        current = None
        description_lines = []

    for raw_line in content.splitlines():
        line = raw_line.rstrip()

        heading_match = TOOL_HEADING.match(line)
        if heading_match:
            flush_current()
            heading = heading_match.group(1).strip()
            current_section = heading if is_tool_section(heading) else None
            continue

        if current_section is None:
            continue

        entry_match = TOOL_ENTRY.match(line.strip())
        if entry_match:
            flush_current()
            index = int(entry_match.group(1))
            name = entry_match.group(2).strip()
            url = entry_match.group(3).strip()
            suffix = entry_match.group(4).strip()
            description_lines = [suffix] if suffix else []
            current = ToolEntry(
                index=index,
                name=name,
                url=url,
                description="",
                section=current_section,
            )
            continue

        if current is not None and not should_skip_description_line(line):
            description_lines.append(line.strip())

    flush_current()
    return tools


def format_tool_block(issue_name: str, issue_number: int | None, tool: ToolEntry) -> str:
    issue_label = f"第 {issue_number} 期" if issue_number else issue_name
    lines = [
        f"### [{issue_label}] {tool.name}",
        "",
        f"- 来源: docs/{issue_name}",
        f"- 链接: {tool.url}",
    ]
    if tool.description:
        lines.append(f"- 描述: {tool.description}")
    lines.extend(["", "---", ""])
    return "\n".join(lines)


def ensure_output_header(output_path: Path, start: int, end: int) -> None:
    if output_path.exists() and output_path.stat().st_size > 0:
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        f"# 科技爱好者周刊 - 工具清单（第 {start}-{end} 期）\n\n"
        "> 本文件由 `tool-extractor/extract_tools.py` 自动生成，仅追加新条目，不修改历史记录。\n\n"
        "---\n\n"
    )
    output_path.write_text(header, encoding="utf-8")


def append_tools(
    output_dir: Path,
    issue_path: Path,
    issue_number: int | None,
    tools: list[ToolEntry],
    known_urls: set[str],
    chunk_size: int,
) -> tuple[int, set[str], Path | None]:
    if issue_number is None:
        match = ISSUE_NUMBER.search(issue_path.name)
        issue_number = int(match.group(1)) if match else 1

    new_tools = []
    for tool in tools:
        normalized = normalize_url(tool.url)
        if normalized in known_urls:
            continue
        known_urls.add(normalized)
        new_tools.append(tool)

    if not new_tools:
        return 0, known_urls, None

    start, end = chunk_range(issue_number, chunk_size)
    output_path = output_dir / chunk_filename(start, end)
    ensure_output_header(output_path, start, end)

    blocks = [
        format_tool_block(issue_path.name, issue_number, tool) for tool in new_tools
    ]
    with output_path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(blocks))

    return len(new_tools), known_urls, output_path


def collect_issue_files(docs_dir: Path) -> list[Path]:
    return sorted(docs_dir.glob("issue-*.md"), key=issue_sort_key)


def reset_outputs(output_dir: Path, state_path: Path) -> None:
    if output_dir.exists():
        for path in output_dir.glob("tools-list-*.md"):
            path.unlink()
        legacy = output_dir / "tools-list.md"
        if legacy.exists():
            legacy.unlink()
    if state_path.exists():
        state_path.unlink()


def run(
    docs_dir: Path,
    output_dir: Path,
    state_path: Path,
    chunk_size: int,
    force_issue: str | None = None,
    reset: bool = False,
) -> int:
    if not docs_dir.is_dir():
        print(f"错误: 文章目录不存在: {docs_dir}", file=sys.stderr)
        return 1

    if reset:
        reset_outputs(output_dir, state_path)
        print("已清空输出目录与状态文件，准备全量重建。")

    output_dir.mkdir(parents=True, exist_ok=True)

    state = ExtractState.load(state_path)
    processed = set(state.processed_issues)
    known_urls = {normalize_url(url) for url in state.known_urls}

    issue_files = collect_issue_files(docs_dir)
    if force_issue:
        issue_files = [path for path in issue_files if path.name == force_issue]
        if not issue_files:
            print(f"错误: 未找到文章 {force_issue}", file=sys.stderr)
            return 1
        processed.discard(force_issue)

    pending = [path for path in issue_files if path.name not in processed]
    if not pending:
        print("没有需要处理的新文章。")
        chunk_files = sorted(output_dir.glob("tools-list-*.md"))
        if chunk_files:
            print("当前拆分文档:")
            for path in chunk_files:
                print(f"  - {path.name}")
        return 0

    total_new_tools = 0
    processed_count = 0
    touched_files: set[Path] = set()

    for issue_path in pending:
        content = issue_path.read_text(encoding="utf-8")
        issue_number = parse_issue_number(issue_path, content)
        tools = parse_tools_from_content(content)
        added, known_urls, output_path = append_tools(
            output_dir,
            issue_path,
            issue_number,
            tools,
            known_urls,
            chunk_size,
        )
        processed.add(issue_path.name)
        processed_count += 1
        total_new_tools += added
        if output_path is not None:
            touched_files.add(output_path)
        print(
            f"{issue_path.name}: 解析 {len(tools)} 个工具，新增 {added} 个"
        )

    state.processed_issues = sorted(processed, key=lambda name: issue_sort_key(Path(name)))
    state.known_urls = sorted(known_urls)
    state.last_run = datetime.now(timezone.utc).isoformat()
    state.save(state_path)

    chunk_files = sorted(output_dir.glob("tools-list-*.md"))
    print(
        f"完成: 处理 {processed_count} 篇文章，新增 {total_new_tools} 条工具记录。"
    )
    print(f"输出目录: {output_dir}")
    print(f"拆分文档数: {len(chunk_files)}（每 {chunk_size} 期一个文件）")
    if touched_files:
        print("本次更新的文档:")
        for path in sorted(touched_files):
            print(f"  - {path.name}")
    print(f"状态文件: {state_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    parser = argparse.ArgumentParser(
        description="增量提取 docs/issue-*.md 中「工具/软件」章节，按每 50 期拆分写入工具清单。"
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=project_root / "docs",
        help="周刊文章目录，默认 ../docs",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=script_dir / "output",
        help="工具清单输出目录",
    )
    parser.add_argument(
        "--state",
        type=Path,
        default=script_dir / "state.json",
        help="增量解析状态文件",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=CHUNK_SIZE,
        help="每个清单文件包含的期数，默认 50",
    )
    parser.add_argument(
        "--issue",
        help="仅重新处理指定文章，例如 issue-412.md",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="清空已有输出与状态后全量重建",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.chunk_size <= 0:
        print("错误: --chunk-size 必须大于 0", file=sys.stderr)
        return 1
    return run(
        args.docs_dir,
        args.output_dir,
        args.state,
        args.chunk_size,
        args.issue,
        args.reset,
    )


if __name__ == "__main__":
    raise SystemExit(main())
