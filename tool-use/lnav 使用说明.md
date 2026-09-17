# lnav 使用说明

[lnav](https://lnav.org/)（The Logfile Navigator）是基于终端的**日志文件查看器**，支持自动识别日志格式、多文件按时间合并、搜索过滤、错误快速跳转，以及 SQL 统计分析。  
周刊第 409 期推荐：[issue-409.md](docs/issue-409.md)

---

## 安装

### Linux

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install lnav

# Fedora
sudo dnf install lnav

# RHEL / CentOS / Rocky / AlmaLinux（需先启用 EPEL）
sudo dnf install epel-release    # 部分系统
sudo dnf install lnav

# Arch Linux
sudo pacman -S lnav

# openSUSE
sudo zypper install lnav

# Snap（通用，版本可能略旧）
sudo snap install lnav

# 官方静态链接二进制（任意 x86_64 Linux）
# 下载：https://lnav.org/downloads 或 GitHub Releases
unzip lnav-*.zip
sudo install -m 755 lnav /usr/local/bin/

# RHEL 系 RPM 仓库
curl -s https://packagecloud.io/install/repositories/tstack/lnav/script.rpm.sh | sudo bash
sudo yum install lnav

# 源码编译
git clone https://github.com/tstack/lnav.git
cd lnav && ./autogen.sh && ./configure && make && sudo make install
```

### Windows

从 **v0.13.1** 起官方支持 Windows，建议在 **Windows Terminal** 或 **PowerShell** 中使用。

```powershell
# 方式一：WinGet（推荐）
winget install --id tstack.lnav --exact

# 方式二：Scoop
scoop install lnav

# 方式三：官方 ZIP
# 从 https://github.com/tstack/lnav/releases/latest 下载 lnav-*-windows-x86_64.zip
# 解压后目录内需同时存在 lnav.exe 和 msys-2.0.dll，再将 bin 目录加入 PATH
```

手动加入 PATH（用户级，无需管理员）：

```powershell
$dir = 'C:\tools\lnav-0.14.1\bin'   # 改为你的实际路径
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
[Environment]::SetEnvironmentVariable('Path', "$userPath;$dir", 'User')
```

加入后**重新打开终端**，验证：

```powershell
lnav -V
```

> **注意**：Windows 版基于 MSYS2 构建，`lnav.exe` 与 `msys-2.0.dll` 必须在同一目录。若在 WSL 中使用，请按 Linux 方式安装。

### macOS / FreeBSD

```bash
brew install lnav          # macOS
pkg install lnav           # FreeBSD
```

---

## 界面与基本流程

启动 lnav 后进入 TUI 界面，主要区域如下：

| 区域 | 说明 |
|------|------|
| 主视图 | 默认 **LOG 视图**，按时间合并显示日志 |
| 底部 Files 面板 | 显示文件索引进度，**需等索引完成**再执行 SQL |
| 底部 Filters 面板 | 按 `Tab` 切换，可视化管理过滤器 |
| 最底行提示符 | 输入搜索 `/`、命令 `:`、SQL `;` |

**推荐操作顺序：**

1. `lnav your.log` 打开日志  
2. 等待底部 Files 面板索引完成（出现 ✔）  
3. 用 `/` 搜索、`e`/`w` 跳错误，或按 `;` 写 SQL  
4. 按 `q` 返回上一级视图 / 退出  

---

## 命令行用法

### 打开日志

```bash
# 单个文件
lnav /var/log/nginx/access.log
lnav C:\logs\app.log

# 多个文件（按时间戳合并）
lnav access.log error.log

# 整个目录（自动发现新文件、支持轮转）
lnav /var/log/nginx/

# 实时跟踪（类似 tail -f，可回滚、搜索、过滤）
lnav -f app.log

# 压缩日志（自动解压 .gz）
lnav access.log.1.gz

# 从 stdin 管道读入
cat app.log | lnav
```

### 无界面模式（脚本 / CI）

```bash
# -n：不进入 TUI
# -c：执行一条 lnav 命令（SQL 以 ; 开头）

# 统计 HTTP 500 数量
lnav -n -c ';SELECT count(*) FROM access_log WHERE sc_status >= 500' access.log

# 过滤 ERROR 并导出 CSV
lnav -n -c ':filter-in ERROR' -c ':write-csv errors.csv' app.log

# 查看有哪些日志格式（表名）
lnav -n -c ';SELECT log_format, count(*) FROM all_logs GROUP BY log_format' app.log
```

---

## 交互快捷键

### 四种输入模式

| 按键 | 模式 | 用途 |
|------|------|------|
| `/` | 搜索 | 正则搜索当前视图 |
| `:` | 命令 | 过滤、高亮、配置等 |
| `;` | SQL | 查询与统计分析 |
| `\|` | 脚本 | 执行 lnav 脚本 |

取消输入：按 **Esc**（有时需按两次）。

### 日志浏览

| 按键 | 作用 |
|------|------|
| `j` / `k` 或 ↑ / ↓ | 上 / 下滚动一行 |
| `Space` / `b` | 下翻 / 上翻一页 |
| `g` / `G` | 跳到开头 / 末尾 |
| `e` / `E` | 下一条 / 上一条 **Error** |
| `w` / `W` | 下一条 / 上一条 **Warning** |
| `n` / `N` | 下一个 / 上一个搜索匹配 |
| `/` | 开始正则搜索 |
| `i` | 时间直方图（错误分布时段） |
| `P` | 美化 JSON / XML 结构化内容 |
| `Shift + P` | 进入 Pretty 视图 |
| `t` | 切换到纯文本视图 |
| `v` | 切换到 DB（SQL 结果）视图 |
| `m` | 标记当前行（书签） |
| `Tab` | 聚焦 Files / Filters 配置面板 |
| `q` | 返回上一视图；在顶层则退出 |
| `?` 或 `F1` | 内置帮助 |

### 命令模式（按 `:` 输入）

```text
:filter-in ERROR              # 只显示含 ERROR 的行
:filter-in 500                # 只显示含 500 的行
:filter-out healthcheck       # 排除 healthcheck
:filter-out                   # 清除所有 filter-in/out
:highlight Exception          # 高亮匹配内容
:highlight                    # 清除高亮
:goto 120                     # 跳到第 120 行
:write-csv result.csv         # 导出当前视图为 CSV
:config /ui/theme grayscale   # 切换为灰度主题（减少着色）
```

---

## 查看有哪些表（SQL 虚拟表）

lnav 为每种识别出的日志格式创建一张**虚拟表**，表名通常等于格式名。

### 方法一：`.schema`（最完整）

1. 按 **`;`** 进入 SQL 模式  
2. 输入：

```text
.schema
```

3. 回车 → 进入 **SCHEMA 视图**，列出所有表及字段定义  
4. 查看单表：`.schema access_log`  
5. 按 **`q`** 返回日志视图  

### 方法二：SQL 查询格式分布

```sql
SELECT log_format, count(*) AS cnt
FROM all_logs
GROUP BY log_format
ORDER BY cnt DESC;
```

### 方法三：Tab 补全

在 SQL 模式下输入 `SELECT * FROM ` 后按 **Tab**，会提示当前可用表名。

### 常见表名对照

| 日志类型 | 典型表名 |
|----------|----------|
| Nginx / Apache 访问日志 | `access_log` |
| 系统 syslog | `syslog_log` |
| JSON Lines | `json_log` 等（视格式而定） |
| 所有已识别日志 | `all_logs` |

---

## SQL 查询详解

lnav 内置 **SQLite 接口**：每条日志是一行，可直接 SQL 统计，无需导入数据库。

### 1. 进入与执行 SQL

1. 打开日志，**等待索引完成**  
2. 按 **`;`** 进入 SQL 输入框  
3. 输入 SQL，执行方式取决于**单行 / 多行模式**：

| 模式 | 如何执行 | 说明 |
|------|----------|------|
| **单行模式** | 按 **Enter** | 适合简单一句查询 |
| **多行模式** | 按 **Ctrl + X** | Enter 只会换行，**不会执行** |

**多行模式相关快捷键：**

| 按键 | 作用 |
|------|------|
| **Ctrl + X** | 执行当前 SQL（多行必用） |
| **Ctrl + L** | 格式化 SQL 并切换到多行模式 |
| **Alt + =** | 增加输入框高度 |
| **Alt + -** | 减少输入框高度 |
| **Tab** | SQL 关键字 / 表名补全 |
| **Esc** | 取消输入 |

> **常见误区**：写了多行 SQL 后一直按 Enter 没有反应——请改用 **Ctrl + X** 执行。

**单行示例**（Enter 执行）：

```sql
SELECT log_format, count(*) FROM all_logs GROUP BY log_format
```

**多行示例**（Ctrl + X 执行）：

```sql
SELECT sc_status, count(*) AS cnt
FROM access_log
GROUP BY sc_status
ORDER BY cnt DESC;
```

### 2. 查看结果（DB 视图）

执行成功后自动进入 **DB 视图**：

| 按键 | 作用 |
|------|------|
| `q` | 返回日志视图 |
| `v` | DB 视图 ↔ 日志视图切换 |
| `Shift + V` | 结果含 `log_line` 时，在结果与原文行间跳转 |
| `F5` | 重新执行上一条 SQL |
| `p` | 打开当前行详情面板 |

### 3. 字段说明

**各格式专属字段**（以 `access_log` 为例）：

| 字段 | 含义 |
|------|------|
| `c_ip` | 客户端 IP |
| `cs_method` | HTTP 方法 |
| `cs_uri_stem` | 请求路径 |
| `sc_status` | HTTP 状态码 |
| `sc_bytes` | 响应字节数 |
| `cs_user_agent` | User-Agent |

**所有格式共用字段**：

| 字段 | 含义 |
|------|------|
| `log_line` | 日志行号（可配合 Shift+V 跳回原文） |
| `log_time` | 时间戳 |
| `log_level` | 级别（error / warning / info） |
| `log_idle_msecs` | 与上一条的时间间隔（毫秒） |
| `log_format` | 日志格式名（即表名） |
| `log_mark` | 是否被用户标记 |

隐藏字段（需显式 SELECT）：`log_path`、`log_text`、`log_body`、`log_raw_text`

### 4. 重要限制

- **只有当前屏幕上显示的日志**参与 SQL；被 `:filter-out` 过滤掉的行**查不到**
- 索引未完成时查询可能为空或不完整
- 表名随日志格式变化，不确定时先用 `all_logs` 或 `.schema`

### 5. 实用 SQL 示例

#### 5.1 单表查询（`access_log` 等）

适用于已确认日志格式、需要用到专属字段（IP、状态码等）的场景：

```sql
-- 统计 HTTP 状态码
SELECT sc_status, count(*) AS cnt
FROM access_log
GROUP BY sc_status
ORDER BY cnt DESC;

-- 流量最大的 10 个 IP
SELECT c_ip, avg(sc_bytes) AS avg_bytes, max(sc_bytes) AS max_bytes
FROM access_log
GROUP BY c_ip
ORDER BY max_bytes DESC
LIMIT 10;

-- 5xx 错误明细（含行号，便于 Shift+V 跳回日志）
SELECT log_line, log_time, c_ip, cs_uri_stem, sc_status
FROM access_log
WHERE sc_status >= 500
ORDER BY log_time DESC
LIMIT 20;
```

#### 5.2 `all_logs` 常用案例

`all_logs` 汇总**所有已识别格式**的日志，适合多文件混看、不确定表名、或只做通用字段分析时使用。

**（1）摸清当前有哪些日志格式**

```sql
SELECT log_format, count(*) AS cnt
FROM all_logs
GROUP BY log_format
ORDER BY cnt DESC;
```

**（2）各级别数量一览**

```sql
SELECT log_level, count(*) AS cnt
FROM all_logs
GROUP BY log_level
ORDER BY cnt DESC;
```

**（3）格式 × 级别交叉统计（哪类日志 error 最多）**

```sql
SELECT log_format, log_level, count(*) AS cnt
FROM all_logs
GROUP BY log_format, log_level
ORDER BY log_format, cnt DESC;
```

**（4）最近 10 条 error（含原文，可 Shift+V 跳回）**

```sql
SELECT log_line, log_time, log_format, log_body
FROM all_logs
WHERE log_level = 'error'
ORDER BY log_time DESC
LIMIT 10;
```

**（5）按时间范围筛选**

```sql
-- 某时刻之后的日志
SELECT log_line, log_time, log_format, log_level, log_body
FROM all_logs
WHERE log_time > '2026-08-25 00:20:00'
ORDER BY log_time ASC
LIMIT 50;

-- 指定时间段
SELECT log_line, log_time, log_format, log_body
FROM all_logs
WHERE log_time BETWEEN '2026-08-25 00:00:00' AND '2026-08-25 01:00:00'
ORDER BY log_time ASC;
```

**（6）全文关键字搜索（跨所有格式）**

```sql
-- 搜 Exception / timeout / OOM 等
SELECT log_line, log_time, log_format, log_level, log_body
FROM all_logs
WHERE log_body LIKE '%Exception%'
ORDER BY log_time DESC
LIMIT 30;

-- 多个关键字（AND）
SELECT log_line, log_time, log_format, log_body
FROM all_logs
WHERE log_body LIKE '%error%' AND log_body LIKE '%connection%'
ORDER BY log_time DESC
LIMIT 20;
```

**（7）按时间分桶统计日志量（找高峰时段）**

```sql
-- 每 5 分钟一条日志量
SELECT timeslice(log_time_msecs, '5m') AS slice, count(*) AS cnt
FROM all_logs
GROUP BY slice
ORDER BY slice;

-- 每小时内 error 数量
SELECT strftime('%Y-%m-%d %H:00', log_time) AS hour, count(*) AS errors
FROM all_logs
WHERE log_level = 'error'
GROUP BY hour
ORDER BY hour;
```

**（8）找出日志「空档」（长时间无新日志）**

```sql
-- 与上一条间隔超过 60 秒（60000 毫秒）
SELECT log_line, log_time, log_format, log_idle_msecs, log_body
FROM all_logs
WHERE log_idle_msecs > 60000
ORDER BY log_idle_msecs DESC
LIMIT 20;
```

**（9）按来源文件统计**

```sql
SELECT log_path, log_format, count(*) AS cnt
FROM all_logs
GROUP BY log_path, log_format
ORDER BY cnt DESC;
```

**（10）查看已标记的重要行**

```sql
-- 在日志视图按 m 标记后，用 SQL 列出
SELECT log_line, log_time, log_format, log_body
FROM all_logs
WHERE log_mark = 1
ORDER BY log_time;
```

**（11）重复消息 Top N（找刷屏日志）**

```sql
SELECT log_body, count(*) AS cnt
FROM all_logs
GROUP BY log_body
HAVING cnt > 5
ORDER BY cnt DESC
LIMIT 20;
```

**（12）错误占比（整体健康度）**

```sql
SELECT
  count(*) AS total,
  sum(CASE WHEN log_level = 'error' THEN 1 ELSE 0 END) AS errors,
  round(100.0 * sum(CASE WHEN log_level = 'error' THEN 1 ELSE 0 END) / count(*), 2) AS error_pct
FROM all_logs;
```

**（13）各格式最近一条日志（确认是否还在写入）**

```sql
SELECT log_format, max(log_time) AS last_seen, count(*) AS cnt
FROM all_logs
GROUP BY log_format
ORDER BY last_seen DESC;
```

**（14）排除某类噪音后再统计 error**

```sql
-- 先 :filter-out healthcheck，再执行；或在 SQL 里排除
SELECT log_line, log_time, log_format, log_body
FROM all_logs
WHERE log_level = 'error'
  AND log_body NOT LIKE '%healthcheck%'
ORDER BY log_time DESC
LIMIT 20;
```

> **提示**：涉及 `log_body`、`log_path` 的查询需显式 SELECT 这些隐藏字段；多行 SQL 写完后按 **Ctrl + X** 执行。

### 6. 命令行 SQL（无界面）

```bash
lnav -n -c ';SELECT count(*) FROM access_log WHERE sc_status >= 500' access.log

lnav -n \
  -c ';SELECT c_ip, count(*) AS cnt FROM access_log GROUP BY c_ip ORDER BY cnt DESC LIMIT 20' \
  -c ':write-csv top_ips.csv' \
  access.log
```

### 7. PRQL（v0.12.1+，可选）

SQL 提示符下也可写 PRQL，lnav 会显示管道各阶段预览：

```sql
from access_log | group sc_status (aggregate { count this })
```

等价 SQL：

```sql
SELECT sc_status, count(*) FROM access_log GROUP BY sc_status;
```

---

## 与 less 的对比

| 场景 | 推荐 |
|------|------|
| 读普通文本、代码、配置 | `less` |
| 排查 Nginx / 应用 / 系统日志 | `lnav` |
| 多文件按时间线合并 | `lnav` |
| 快速跳转 error / warning | `lnav` |
| 对日志做 SQL 统计 | `lnav` |
| 实时 tail 且需回滚搜索 | `lnav -f` |

**lnav 优势**：理解日志格式、多文件合并、自动解压、错误索引、过滤高亮、SQL/PRQL 分析。  
**less 优势**：轻量通用、内存占用低，适合非日志纯文本。

---

## 典型排查流程

### 1. 线上故障实时盯盘

```bash
lnav -f /var/log/myapp/app.log
```

- 按 `/` 搜 `Exception` 或 `error`  
- 按 `e` 在 error 间跳转  
- 按 `i` 看错误时间分布  

### 2. Nginx access + error 联合分析

```bash
lnav /var/log/nginx/access.log /var/log/nginx/error.log
```

多文件按时间戳自动合并，左侧色条区分来源文件。

### 3. 历史轮转日志目录

```bash
lnav /var/log/myapp/
```

自动加载目录内文件，支持 `.gz` 压缩包。

### 4. JSON 结构化日志

```bash
lnav app.json.log
```

- 按 `/` 搜 `request_id`  
- 光标移到 JSON 行，按 **`P`** 美化显示  
- 按 **`;`** 对 JSON 字段做 SQL（若格式被识别）  

### 5. 用 SQL 做简单报表

```bash
lnav /var/log/nginx/access.log
# 索引完成后按 ;，执行状态码统计，Ctrl+X 提交
```

---

## 常见问题

**Q：多行 SQL 按 Enter 不执行？**  
A：多行模式下 Enter 只换行，请按 **Ctrl + X** 执行。

**Q：SQL 查不到数据？**  
A：检查索引是否完成、表名是否正确（用 `.schema` 或查 `all_logs`）、是否被 filter 过滤。

**Q：不知道表名？**  
A：执行 `SELECT log_format, count(*) FROM all_logs GROUP BY log_format` 或输入 `.schema`。

**Q：Windows 下 lnav 无法运行？**  
A：确认 `lnav.exe` 与 `msys-2.0.dll` 同目录，PATH 已配置，使用 Windows Terminal。

**Q：和 grep / tail 怎么配合？**  
A：lnav 可替代「tail + grep + less」组合做交互分析；脚本化批量处理仍可用 grep/awk，或用 `lnav -n -c '...'`。

---

## 参考链接

- 官网：https://lnav.org/
- 功能：https://lnav.org/features
- GitHub：https://github.com/tstack/lnav
- 文档：https://docs.lnav.org/
- SQL 接口：https://docs.lnav.org/en/latest/sqlext.html
- 快捷键：https://docs.lnav.org/en/latest/hotkeys.html
