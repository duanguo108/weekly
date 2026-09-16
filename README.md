# 科技爱好者周刊 · 工具清单

本项目基于 [阮一峰](https://github.com/ruanyf) 的 [科技爱好者周刊](https://github.com/ruanyf/weekly)，从每期文章的「工具 / 软件」章节中自动提取工具条目，整理为可检索的工具清单文档。

原始周刊记录每周值得分享的科技内容，每期都会推荐若干实用工具。本仓库在保留原文的基础上，通过脚本将这些工具汇总、去重，并按每 50 期拆分为多个 Markdown 文件，方便查阅与检索。

## 数据来源

- 原文仓库：[ruanyf/weekly](https://github.com/ruanyf/weekly)
- 文章目录：`docs/issue-*.md`（第 1 期 ~ 第 412 期）
- 提取章节：`## 工具`、`## 软件`

## 工具提取脚本

脚本位于 `tool-extractor/extract_tools.py`，支持增量解析：只处理尚未提取的新期文章，清单文档仅追加、不修改历史条目。

```bash
# 增量更新（处理新发布的期数）
python tool-extractor/extract_tools.py

# 全量重建（清空后重新生成所有清单）
python tool-extractor/extract_tools.py --reset

# 自定义拆分粒度（默认每 50 期一个文件）
python tool-extractor/extract_tools.py --reset --chunk-size 50
```

输出目录：`tool-extractor/output/`  
状态文件：`tool-extractor/state.json`（记录已处理文章与已知 URL，用于增量与去重）

## 工具清单文档

共 **4061** 条不重复工具，拆分为 **9** 个文件（每 50 期一段）。以下列出每个文档中的前 10 个工具及简要描述，完整内容请点击文件名查看。

### [tools-list-001-050.md](tool-extractor/output/tools-list-001-050.md)（第 1–50 期）

1. **Spectrum**：开源的社区软件，形式非常新颖美观。
2. **jsonstore.io**：通过 HTTP Header 读写 JSON 数据的免费 datastore。
3. **flamebearer**：Node 应用的火焰图生成工具，用于性能分析。
4. **DNS Performance Test**：DNS 响应时间的命令行比较脚本。
5. **merge-images**：多张图片合成一张图片的浏览器 JS 库，使用了 Canvas。
6. **Tabler**：一个基于 Bootstrap4 的面板（dashboard）组件库。
7. **Etherpad**：老牌的多人实时编辑协同工具。
8. **Mustard UI**：一个简洁、好看的 CSS 框架，压缩后只有5.28KB。
9. **ReactOS**：ReactOS 是一个开源的操作系统，目标是兼容 Windows，能够运行 Windows 的应用程序和驱动程序。它只能安装在 FAT16 或者 FAT32 的…
10. **Remote Browser**：一个浏览器自动化框架，可以用脚本控制已经打开的浏览器。

…

---

### [tools-list-051-100.md](tool-extractor/output/tools-list-051-100.md)（第 51–100 期）

1. **node-five**：一个基于 QT 的 Nodejs 框架，用于开发 Node 应用的图形界面。
2. **Learn anything**：一个学习资源的搜索引擎，可以搜索各种主题，返回相应的教程。
3. **Gckit-CLI**：命令行下使用一行命令，生成`Swift`、`Objective-C`等项目的模板代码。
4. **php-lisp**：一个使用 PHP 写的 Lisp 代码解释器。
5. **Paste to Markdown**：粘贴到该窗口的任何文本内容，都会自动转为 Markdown 格式。
6. **RCT**：一个通过解析 rdb 文件对 redis 内存结构分析的一站式平台。
7. **squoosh**：谷歌开源的图像压缩服务。
8. **Whoer.net**：查看你的 HTTP 请求携带多少个人信息的网站。
9. **chunkwm**：Mac 电脑的多窗口平铺式管理器。
10. **StreamSaver.js**：流媒体保存成本地文件的浏览器库。

…

---

### [tools-list-101-150.md](tool-extractor/output/tools-list-101-150.md)（第 101–150 期）

1. **GoMailer**：一个轻量的电子邮件推送开源工具，可以与网站的用户反馈、留言等功能进行集成，将数据填入模板，投递到指定的邮箱。
2. **Zarm**：一个 React 组件库，众安科技出品。特点是依赖少体积小（压缩后 60KB），扩展性好，样式命名采用了 BEM 规范。
3. **KafkaCenter**：一站式的 Kafka 集群管理和维护平台，代码开源，完善的权限设计，使用方便，无需精通 Kafka 就能管理集群。
4. **XAudioPro**：在线音频实时剪辑转码网站。我个人本身是做音频开发出生的，对音频算法底层很熟悉，所以就诞生了创建这个网站的想法。 专业的 Audition 软件主要面对很多专业人…
5. **办公室噪音生成器**：在家远程办公的时候，你会不会想起办公室嘈杂的工作环境，说话声、电话铃声、敲击键盘声、喝水声…… 这里有一个办公室噪音生成器，可以无限播放。
6. **HugeGraph**：百度安全团队研发的一款易用、高效、通用的开源图数据库系统， 具备完善的工具链组件，助力用户轻松构建基于图数据库之上的应用和产品。 典型应用场景包括深度关系探索、…
7. **SimpleCTO  screenshot**：一个在线生成网站截图的工具，用户提交 URL，就能下载网页截图，代码开源。
8. **Swift Playgrounds**：苹果公司官方的免费 Mac 桌面软件，通过游戏学习 Swift 语言。
9. **time.gov**：美国政府显示国内各时区的时间的网站。
10. **progressive-image-element**：一个 HTML 的自定义元素（custom element），可以懒加载网页图片。这个元素的代码非常简单，可以作为学习自定义元素的写法范例。

…

---

### [tools-list-151-200.md](tool-extractor/output/tools-list-151-200.md)（第 151–200 期）

1. **Gotify**：一个 Go 语言写的 WebSockets 库，有服务端、客户端和安卓端。
2. **lint-md**：一个检查中文 Markdown 语法风格的命令行工具，比如英文字母与全角字符之间有一个空格。
3. **FairEmail**：开源的安卓电子邮件客户端，强调安全和隐私保护。
4. **AR-lab**：一个实验性桌面程序，使用百度飞轮和 Electron 实现的 AR 剪贴和复制。手机先对准某人，再对准电脑屏幕，即可把他/她复制粘贴到桌面程序里面！
5. **rss_everyday**：一个 GitHub Actions 模板，每天定时运行，将 RSS 内容推送到 Telegram 频道。
6. **mdBook**：GitBook 的 Rust 语言移植，可以将 markdown 源文件转成一个在线阅读网站。
7. **flowchart-fun**：可能是最简单的流程图制作工具。左边的文本框输入，一行就代表一个新节点，缩进代表隶属关系，右边自动生成图形。
8. **DarkModeBuddy**：一个 macOS 应用，自动根据外部光线的强弱，调整桌面为亮模式或暗模式。
9. **Arrow**：一个 Python 的日期时间库，借鉴了 moment.js 的 API 设计。
10. **Wombo**：一个手机 App，上传一张脸部照片和一首歌曲，它就会自动生成照片人物对口型唱歌的视频。

…

---

### [tools-list-201-250.md](tool-extractor/output/tools-list-201-250.md)（第 201–250 期）

1. **PeaZip**：一个开源的桌面压缩软件，带有图形界面，优点是支持一些新的压缩算法，包括 Zstandard 和 Brotli 算法。
2. **Speech To Code**：一个实验性的语音编程项目，通过口述指令生成代码，这里试用 [Demo](https://pedrooaugusto.github.io/speech-to-co…
3. **HertzBeat 赫兹跳动**：一个国产的开源云监控系统，具有监控网站、PING 连通性、端口可用性、数据库、操作系统、阈值告警等功能，告警通知可通过邮件、微信、钉钉、飞书等发送。
4. **stop-mess-around**：一个浏览器插件，减少摸鱼的时间和频率。打开插件后，一旦访问指定的消磨时间的网址，它就会自动统计浏览时间，达到门槛值就会弹出提醒。
5. **视频 PPT 提取器**：某些教学视频都在讲解 PPT 文案，或者需要导出 PPT 供以后学习，这个工具可以从视频里面提取 PPT，保存为 PDF 文件。
6. **sqlite-utils**：一个命令行工具，可以直接对 SQLite 数据库执行 SQL 查询。
7. **Simple.css**：一个极简化的 CSS 框架，追求“无类化使用”，即不用指定 class，直接对 HTML 标签生效。 类似的框架还有很多，比如 [Pico.css](https…
8. **Sci Hub Injector**：一个浏览器插件，可以在国外著名的论文网站上（比如 PubMed、Nature 等等），插入某篇论文对应的 SciHub 链接。它的代码很简单，可以用来学习如何写…
9. **fq**：一个命令行工具，可以方便地查看二进制文件的内容。
10. **lemmy**：一个开源的论坛聚合服务，只要是支持 Fediverse 协议的论坛，都可以用它订阅。然后就可以在一个页面上，同时浏览多个论坛并发帖。

…

---

### [tools-list-251-300.md](tool-extractor/output/tools-list-251-300.md)（第 251–300 期）

1. **nango**：一个[开源](https://github.com/NangoHQ/nango)的 Web 服务，自动获取和管理各种 OAuth 认证的 token，可以自己架…
2. **docker-rollout**：这个工具可以不停机更新 Docker Compose 里面的某个服务。原理是同时新建两个实例，用已更新的实例替换未更新的实例。
3. **Web LLM**：这个软件通过 WebGPU API，在浏览器里面运行 LLM 模型，可以离线运行，并且不限定模型。 当然，它不能用来训练大模型，而且表现肯定不如 ChatGPT…
4. **OpenAI 接口应用**：使用 Express 搭建的 Node.js 应用，用来连接 OpenAI API 进行聊天。代码开源。这是前端代码，另有[后端代码](https://gith…
5. **Animated Drawings**：这个工具使用 AI 模型，将手绘的人物草图变成一段动画。
6. **scrutiny**：实时检查硬盘 S.M.A.R.T 健康状态的工具，Docker 安装，自带 Web UI。
7. **browsertunnel**：这个软件可以将用户信息，通过网页的 DNS 请求传回服务器。注意，不是 HTTP 请求，而是使用查询域名的 DNS 请求夹带额外信息。这种监视用户的方法，很难发…
8. **Upbase**：一个网页应用，将项目管理、日程安排、聊天、文档等功能做到了一起，目标是成为团队协作的一站式工具。
9. **Bot Aquarium**：一个 Linux 系统运行的虚拟机，特点是完全交给 OpenAI 控制。 你描述想用虚拟机完成的任务，它把这段描述传给 OpenAI，并且自动执行返回的命令。等…
10. **Autodoc**：使用 LLM 模型自动生成代码文档。作者的想法是将它加入持续构建，每次代码变更，就会同时自动更新文档。

…

---

### [tools-list-301-350.md](tool-extractor/output/tools-list-301-350.md)（第 301–350 期）

1. **SunEditor**：一个开源的“所见即所得”编辑器，兼容性比较好。
2. **TrasHTTPandas**：这个网站提供各种状态码的 HTTP 回应，供 API 调用，可以用来调试前端请求。
3. **安读**：一款使用 Flutter 编写的桌面读书软件，支持 WebDAV 同步。
4. **VSpace**：一个浏览器插件，提供侧边栏的垂直书签和标签页管理器。
5. **FreeReNamer**：开源的跨平台桌面软件，用来将文件批量重命名。
6. **Keyviz**：开源的 Windows 软件，在桌面上显示用户实时的按键。
7. **XIAOJUSURVEY**：一套开源的问卷系统，自带后端和前端，用于架设管理自己的问卷。
8. **Quetta**：一个注意保护个人隐私的手机浏览器，支持 iOS 和安卓，不收集用户的任何数据，也防止被网站收集。
9. **Sandstorm**：一个开源的 Web 应用软件商店，安装以后，就可以在它的商店里面，点击安装/运行多种 Web 应用。
10. **Database Diagram**：一个免费网站，在线生成数据库的 ER（实体-关系）图。

…

---

### [tools-list-351-400.md](tool-extractor/output/tools-list-351-400.md)（第 351–400 期）

1. **Quarkdown**：一个使用 Markdown 语法的排版系统。
2. **RsyncUI**：一个开源的 Mac 应用，提供 rsync 的图形界面，用于跟远程服务器传输文件。
3. **Donut**：一个浏览器的编排器，可以保存各种不同的浏览器配置，根据需要快速启动。
4. **Read Frog**：（陪读蛙） 一个浏览器插件，可以翻译页面，提取文章主要内容，给出单词和句子和详细解释，[代码开源](https://github.com/mengxi-ream…
5. **Datetime.app**：开源的日期时间网站，time.is 的替代品。
6. **naviix**：网页的键盘导航库，通过上下左右的方向键，选取网页的焦点元素。
7. **go-v2ex**：基于 Go 语言的命令行版 V2EX 客户端。
8. **TL-RTC-APP**：开源的 Web 即时通信系统，基于 webrtc。
9. **Cap.js**：一个网页上的机器人识别工具，用作 CAPTCHA 方案，采用 SHA-256 工作量证明算法。
10. **Quartz**：Markdown 文档的静态站点发布器，适合用作收费服务 Obsidian Publish 的替代品。

…

---

### [tools-list-401-450.md](tool-extractor/output/tools-list-401-450.md)（第 401–412 期）

1. **Lore**：游戏公司 EpicGames 开源的一个版本管理系统。跟 Git 相比，它的最大特点是为二进制文件提供版本管理。 它将大型的二进制文件拆分成一个个数据块，进行储…
2. **DNS Pick**：一个命令行的 DNS 优选工具，结合平均延迟与解析成功率，选出兼顾速度与稳定性的最优 DNS 服务器。
3. **GitFolio**：轻量级的 Git 仓库管理系统，类似于 Gitea，支持从 GitHub 镜像同步仓库数据。
4. **ssh-at**：`~/.ssh/config` 的图形化管理工具。
5. **LockIME**：macOS 的输入法锁定工具，可以指定不同应用的默认输入法。
6. **封面生成器**：（Cover Maker） 封面制作的网页工具。
7. **PowerLens**：Oh-My-Zsh 插件，在命令行提示符实时展示电源功率、电池、CPU、CPU 温度、风扇转速、内存和网络流量。
8. **MyKVM**：源跨平台软件 KVM，在同一局域网内，让 macOS、Windows、Linux 共享一套键盘、鼠标和剪贴板。
9. **ai_caption_video**：开源的 Windows 应用，生成大字报式的中文短视频，支持关键词高亮、字幕动效、本地 TTS 配音和语音克隆。
10. **AnyDrag**：一款 macOS 小工具，不必按住标题栏，就能拖动、缩放、最大化、平铺窗口。

…

---

## 条目格式说明

每条工具记录包含：

- 工具名称与所属期数
- 原文链接（`docs/issue-xxx.md`）
- 工具 URL
- 简要描述（摘自周刊原文）

同一 URL 在全库中只保留一条（以首次出现的期数为准）。

## 许可与致谢

周刊原文版权归 [阮一峰](https://github.com/ruanyf) 所有，遵循原仓库 [MIT License](https://github.com/ruanyf/weekly/blob/master/LICENSE)。  
工具清单为基于公开内容的整理提取，仅供学习与交流使用。
