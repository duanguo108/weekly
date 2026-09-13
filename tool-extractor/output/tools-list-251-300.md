# 科技爱好者周刊 - 工具清单（第 251-300 期）

> 本文件由 `tool-extractor/extract_tools.py` 自动生成，仅追加新条目，不修改历史记录。

---

### [第 251 期] nango

- 来源: docs/issue-251.md
- 链接: https://www.nango.dev/
- 描述: 一个[开源](https://github.com/NangoHQ/nango)的 Web 服务，自动获取和管理各种 OAuth 认证的 token，可以自己架设。

---

### [第 251 期] docker-rollout

- 来源: docs/issue-251.md
- 链接: https://github.com/Wowu/docker-rollout
- 描述: 这个工具可以不停机更新 Docker Compose 里面的某个服务。原理是同时新建两个实例，用已更新的实例替换未更新的实例。

---

### [第 251 期] Web LLM

- 来源: docs/issue-251.md
- 链接: https://mlc.ai/web-llm/
- 描述: 这个软件通过 WebGPU API，在浏览器里面运行 LLM 模型，可以离线运行，并且不限定模型。 当然，它不能用来训练大模型，而且表现肯定不如 ChatGPT，但是能在浏览器里面运行，大大降低了自己架设 LLM 的门槛，而且非常适合一些离线任务（比如总结文档），详见这篇[测评](https://simonwillison.net/2023/Apr/16/web-llm/)。

---

### [第 251 期] OpenAI 接口应用

- 来源: docs/issue-251.md
- 链接: https://github.com/KiritoCheng/openai-public
- 描述: 使用 Express 搭建的 Node.js 应用，用来连接 OpenAI API 进行聊天。代码开源。这是前端代码，另有[后端代码](https://github.com/KiritoCheng/openai-server)。（[@KiritoCheng](https://github.com/ruanyf/weekly/issues/3055) 投稿）

---

### [第 251 期] Animated Drawings

- 来源: docs/issue-251.md
- 链接: https://github.com/facebookresearch/AnimatedDrawings
- 描述: 这个工具使用 AI 模型，将手绘的人物草图变成一段动画。

---

### [第 251 期] scrutiny

- 来源: docs/issue-251.md
- 链接: https://github.com/AnalogJ/scrutiny
- 描述: 实时检查硬盘 S.M.A.R.T 健康状态的工具，Docker 安装，自带 Web UI。

---

### [第 251 期] browsertunnel

- 来源: docs/issue-251.md
- 链接: https://github.com/veggiedefender/browsertunnel
- 描述: 这个软件可以将用户信息，通过网页的 DNS 请求传回服务器。注意，不是 HTTP 请求，而是使用查询域名的 DNS 请求夹带额外信息。这种监视用户的方法，很难发现，也很难阻止。

---

### [第 251 期] Upbase

- 来源: docs/issue-251.md
- 链接: https://upbase.io/
- 描述: 一个网页应用，将项目管理、日程安排、聊天、文档等功能做到了一起，目标是成为团队协作的一站式工具。

---

### [第 251 期] Bot Aquarium

- 来源: docs/issue-251.md
- 链接: https://github.com/fafrd/aquarium
- 描述: 一个 Linux 系统运行的虚拟机，特点是完全交给 OpenAI 控制。 你描述想用虚拟机完成的任务，它把这段描述传给 OpenAI，并且自动执行返回的命令。等到虚拟机出来了执行结果（比如报错），它再自动把执行结果提交给 OpenAI，不断重复这个过程，直到任务完成。

---

### [第 251 期] Autodoc

- 来源: docs/issue-251.md
- 链接: https://github.com/context-labs/autodoc
- 描述: 使用 LLM 模型自动生成代码文档。作者的想法是将它加入持续构建，每次代码变更，就会同时自动更新文档。

---

### [第 251 期] SceneXplain

- 来源: docs/issue-251.md
- 链接: https://scenex.jina.ai/
- 描述: 用户上传一张图片，它会给出图片的详细文字描述，号称比其他模型效果好。

---
### [第 252 期] rety

- 来源: docs/issue-252.md
- 链接: https://rety.verou.me/
- 描述: 一个网页 JS 库，可以将打字编辑的过程录制下来，然后重新播放。非常适合演讲时，向听众展示代码输入。

---

### [第 252 期] ReceiveSMS

- 来源: docs/issue-252.md
- 链接: https://www.receivesms.io/
- 描述: 国外的手机接码平台。（[@williamwoodhq](https://github.com/ruanyf/weekly/issues/3066) 投稿）

---

### [第 252 期] Word GPT Plus

- 来源: docs/issue-252.md
- 链接: https://github.com/Kuingsmile/word-GPT-Plus
- 描述: Microsoft Word 的插件，集成了 ChatGPT，用来生成、修改文本。（[@Kuingsmile](https://github.com/ruanyf/weekly/issues/3069) 投稿）

---

### [第 252 期] create-chart

- 来源: docs/issue-252.md
- 链接: https://github.com/food-billboard/create-chart
- 描述: 一个基于 echarts 的可视化大屏设计器。（[@food-billboard](https://github.com/ruanyf/weekly/issues/3074) 投稿）

---

### [第 252 期] Typst

- 来源: docs/issue-252.md
- 链接: https://typst.app/
- 描述: 一个在线排版系统，跟 LaTeX 类似，可以实时查看渲染效果，主要用于学术出版物，代码[开源](https://github.com/typst/typst)。（[@wolfg1969](https://github.com/ruanyf/weekly/issues/3080) 投稿）

---

### [第 252 期] Wails

- 来源: docs/issue-252.md
- 链接: https://wails.io/
- 描述: 一个用来写跨平台桌面应用的 Go 框架，可以替代 Electron。跟 [Tauri](https://tauri.app/) 的作用类似，不同的是 Tauri 基于 Rust 语言，它基于 Go。

---

### [第 252 期] CSS 的机械装置

- 来源: docs/issue-252.md
- 链接: https://cohost.org/blackle/post/42994-div-style-pointer
- 描述: 一个互动式的机械装置，很难相信它的互动效果完全用 CSS 实现，拉动左侧的绳柄，整个装置就动起来了。

---

### [第 252 期] Relight

- 来源: docs/issue-252.md
- 链接: https://clipdrop.co/relight
- 描述: 这个网页工具可以调节照片的灯光。用户上传一张照片，它可以修改灯光，调节颜色、距离、亮度等等，还可以添加其他光源。

---

### [第 252 期] Unclutter

- 来源: docs/issue-252.md
- 链接: https://unclutter.it/
- 描述: 一个浏览器插件，可以网页的正文提取出来，以阅读模式展示，并且可以调整各种参数。这里还有一个[类似的工具](https://reader-next.pages.dev/)。

---
### [第 253 期] stagit

- 来源: docs/issue-253.md
- 链接: https://git.codemadness.org/stagit/
- 描述: 这个软件可以将 Git 仓库转为一个静态网站，为每个文件、每次提交生成一个页面。

---

### [第 253 期] 元标签生成器

- 来源: docs/issue-253.md
- 链接: https://websitemetadata.com/meta-tags-generator
- 描述: 很多社交媒体对于外部 URL，会显示一个卡片，上面有标题、缩略图和页面简要内容。这些信息来自网页里面的元标签，这个工具可以帮助你生成这些元标签。

---

### [第 253 期] CJK 字体识别

- 来源: docs/issue-253.md
- 链接: https://github.com/JeffersonQin/YuzuMarker.FontDetection
- 描述: 上传一张东亚文字的图片，这个开源工具可以识别这些文字用了什么字体。（[@JeffersonQin](https://github.com/ruanyf/weekly/issues/3090) 投稿）

---

### [第 253 期] microblog.pub

- 来源: docs/issue-253.md
- 链接: https://microblog.pub/
- 描述: 一个自托管的开源微博网站，只能一个人使用（即没有多用户），支持 ActivityPub 协议。

---

### [第 253 期] Textual Markdown Browser

- 来源: docs/issue-253.md
- 链接: https://github.com/willmcgugan/textual-markdown
- 描述: 一个终端窗口的 Markdown 文件渲染器，适合用来在终端下阅读 Markdown 文件。

---

### [第 253 期] HorusPass

- 来源: docs/issue-253.md
- 链接: https://horuspass.com/send
- 描述: 这个网站为用户输入的文本，生成一个用于分享的 URL。但是，这个 URL 只能打开一次，第二次访问就会不存在，有点像“阅后即焚”。

---

### [第 253 期] Progress-up

- 来源: docs/issue-253.md
- 链接: https://progress-up.live/
- 描述: 一个带有上传进度显示的网页多文件上传 JS 库。

---

### [第 253 期] snappify

- 来源: docs/issue-253.md
- 链接: https://snappify.com/editor
- 描述: 一个将代码片段生成截图的工具。

---

### [第 253 期] RustDesk

- 来源: docs/issue-253.md
- 链接: https://rustdesk.com/
- 描述: 一个开源的远程桌面软件，让你远程操作其他电脑的桌面，有各种操作系统的客户端。

---

### [第 253 期] LosslessCut

- 来源: docs/issue-253.md
- 链接: https://mifi.no/losslesscut/
- 描述: 一个视频编辑器，最大特点是不进行重新编码，按照原视频的格式进行剪切连接，因此速度极快。

---
### [第 254 期] Instant Logo Design

- 来源: docs/issue-254.md
- 链接: https://instantlogodesign.com/
- 描述: 输入产品或公司的英文名称，这个网站可以自动生成几十款 Logo，供你选择。

---

### [第 254 期] Accessibility

- 来源: docs/issue-254.md
- 链接: https://github.com/ranbuch/accessibility
- 描述: 一个 JS 库，用来增强网页的可用性。只要插入这个库，网页就会出现一个工具栏，让用户自己选择增大字体、加深对比色、增大间隔、朗读文本等等。

---

### [第 254 期] 沉浸式翻译

- 来源: docs/issue-254.md
- 链接: https://immersive-translate.owenyoung.com/
- 描述: 浏览器的双语翻译插件，可以指定翻译引擎（10多种可选），并可以翻译 pdf、epub 电子书。（[@theowenyoung](https://github.com/ruanyf/weekly/issues/3100) 投稿）

---

### [第 254 期] ChatLLM-Web

- 来源: docs/issue-254.md
- 链接: https://github.com/Ryan-yang125/ChatLLM-Web
- 描述: 开源的浏览器 LLM 模型，只要访问作者已经部署的网页，就能使用，所有数据都在本地训练。（[@Ryan-yang125](https://github.com/ruanyf/weekly/issues/3104) 投稿） 注意，用户需要满足三个使用条件。 > - Chrome 113 以上浏览器。 > - 下载训练数据约 4GB（只需下载一次）。 > - 显卡最好有 6.4GB 以上显存。

---

### [第 254 期] 1Panel

- 来源: docs/issue-254.md
- 链接: https://1panel.cn/
- 描述: 开源的 Linux 服务器运维面板。（[@maninhill](https://github.com/ruanyf/weekly/issues/3098) 投稿）

---

### [第 254 期] PyQt-Fluent-Widgets

- 来源: docs/issue-254.md
- 链接: https://github.com/zhiyiYo/PyQt-Fluent-Widgets
- 描述: Python 图形界面框架 PyQt 的组件库。（[@zhiyiYo](https://github.com/ruanyf/weekly/issues/3097) 投稿）

---

### [第 254 期] VizGPT

- 来源: docs/issue-254.md
- 链接: https://github.com/ObservedObserver/viz-gpt
- 描述: 一个对话式的可视化图表生成工具，用户使用自然语言告诉 AI 生成什么样的图表，可以多轮调整。（[@ObservedObserver](https://github.com/ruanyf/weekly/issues/3108) 投稿）

---

### [第 254 期] Vue DevTools

- 来源: docs/issue-254.md
- 链接: https://github.com/webfansplz/vite-plugin-vue-devtools
- 描述: 网友实现的 Vue 开发者工具。（[@webfansplz](https://github.com/ruanyf/weekly/issues/3107) 投稿）

---

### [第 254 期] Dify.AI

- 来源: docs/issue-254.md
- 链接: https://dify.ai/
- 描述: 一个开发者工具，帮你快速生成基于 AI 的应用。（[@Panmuse](https://github.com/ruanyf/weekly/issues/3110) 投稿）

---

### [第 254 期] dnrm

- 来源: docs/issue-254.md
- 链接: https://github.com/markthree/dnrm
- 描述: deno 实现的 npm 镜像源切换工具，每次切换都在 100ms 内，速度超级快。（[@markthree](https://github.com/ruanyf/weekly/issues/3111) 投稿）

---
### [第 255 期] Astrodon

- 来源: docs/issue-255.md
- 链接: https://github.com/astrodon/astrodon
- 描述: 一个使用 Deno 的跨平台桌面应用开发工具，类似于 Electron，但底层是移植到 JavaScript 环境的 Tauri 框架。

---

### [第 255 期] HuggingChat

- 来源: docs/issue-255.md
- 链接: https://huggingface.co/chat
- 描述: AI 平台 HuggingFace 自家的 AI 聊天页面，底层可以配置不同模型，免费使用。

---

### [第 255 期] Chat with any PDF

- 来源: docs/issue-255.md
- 链接: https://damngood.tools/tools/chat-pdf
- 描述: 上传一个 PDF 文件，就能跟该文件交谈，让它回答相关问题。 目前好像不支持中文 PDF 文件，但是支持用中文提问和回答。类似工具还有 [ScholarTurbo](https://scholarturbo.com/)。

---

### [第 255 期] Nature 编程语言

- 来源: docs/issue-255.md
- 链接: https://github.com/nature-lang/nature
- 描述: 网友发明的一种编程语言，语法追求简洁优雅、符合直觉。（[@weiwenhao](https://github.com/ruanyf/weekly/issues/3117) 投稿）

---

### [第 255 期] LaWGPT

- 来源: docs/issue-255.md
- 链接: https://github.com/pengxiao-song/LawGPT
- 描述: 基于中文法律知识的开源大语言模型，很适合用于司法考试。（[@pengxiao-song](https://github.com/ruanyf/weekly/issues/3116) 投稿）

---

### [第 255 期] mblog

- 来源: docs/issue-255.md
- 链接: https://github.com/kingwrcy/mblog-backend
- 描述: 网友开发的基于 Java + MySQL 的多用户微博系统。（[@kingwrcy](https://github.com/ruanyf/weekly/issues/3121) 投稿）

---

### [第 255 期] wallpaper-box

- 来源: docs/issue-255.md
- 链接: https://github.com/wangrongding/wallpaper-box
- 描述: 一个基于 Electron 的桌面壁纸客户端，支持壁纸管理、动态壁纸、动态托盘图标等功能。（[@wangrongding](https://github.com/ruanyf/weekly/issues/3118) 投稿）

---

### [第 255 期] Pho

- 来源: docs/issue-255.md
- 链接: https://github.com/fregie/pho
- 描述: 一个开源的安卓相册应用，可以将照片同步到多种协议（smb、webdav、nfs）的网络储存。（[@fregie](https://github.com/ruanyf/weekly/issues/3122) 投稿）

---

### [第 255 期] 哔哩哔哩字幕列表

- 来源: docs/issue-255.md
- 链接: https://github.com/IndieKKY/bilibili-subtitle
- 描述: 一个浏览器扩展，列出 BiliBili 视频字幕内容，用户点击就可以跳转到相应的视频位置。（[@IndieKKY](https://github.com/ruanyf/weekly/issues/3123) 投稿）

---

### [第 255 期] stitching

- 来源: docs/issue-255.md
- 链接: https://github.com/lukasalexanderweber/stitching
- 描述: 一个 Python 软件包，用于将多幅照片合成一幅。

---
### [第 256 期] Convoy

- 来源: docs/issue-256.md
- 链接: https://github.com/frain-dev/convoy
- 描述: 开源的 Webhooks 网关，自带管理后台，具有重试、速率限制、静态 IP、熔断等大量功能。

---

### [第 256 期] AME Wizard

- 来源: docs/issue-256.md
- 链接: https://ameliorated.io/
- 描述: 一个修改 Windows 11 配置的工具。特点是可以根据使用场景，从它的网站下载对应的配置文件，然后运行该文件就完成配置。

---

### [第 256 期] RunApi

- 来源: docs/issue-256.md
- 链接: https://www.showdoc.com.cn/runapi/30291
- 描述: 国内公司开发的一个跨平台桌面软件，用于 API 接口开发测试，类似于 Postman。（[@star7th](https://github.com/ruanyf/weekly/issues/3128) 投稿）

---

### [第 256 期] Shaku

- 来源: docs/issue-256.md
- 链接: https://github.com/JSerZANP/shaku
- 描述: 一个 Markdown 页面的增强渲染工具，可以基于代码块里面的注释，将代码渲染成指定样式（上图），详见[介绍文章](https://jser.dev/2023-05-14-introducing-shaku/)。（[@DongHY1](https://github.com/ruanyf/weekly/issues/3133) 投稿）

---

### [第 256 期] eslint-plugin-check-file

- 来源: docs/issue-256.md
- 链接: https://github.com/DukeLuo/eslint-plugin-check-file
- 描述: 一个 ESLint 插件，检查文件名是否符合指定规则。（[@DukeLuo](https://github.com/ruanyf/weekly/issues/3132) 投稿）

---

### [第 256 期] Soft Serve

- 来源: docs/issue-256.md
- 链接: https://github.com/charmbracelet/soft-serve
- 描述: 只需在命令行执行一条命令，就能自己搭建 Git 服务器，简单易用，但是不带 Web 界面。

---

### [第 256 期] JShelter

- 来源: docs/issue-256.md
- 链接: https://jshelter.org/
- 描述: 一个浏览器扩展，指定你要关闭哪些浏览器 API，主要用来防止被追踪。

---

### [第 256 期] Tails

- 来源: docs/issue-256.md
- 链接: https://tails.boum.org/index.en.html
- 描述: 一个融合了 Debian 和 Tor 的操作系统，放到 U 盘里面，插入 USB 接口就能用，可以很好地保护隐私。

---

### [第 256 期] Just

- 来源: docs/issue-256.md
- 链接: https://just.systems/
- 描述: 一个命令运行器，类似于 Make，但不具备构建功能。 它允许把一个项目的所有命令行命令，都写在一个文件里面，并可以指定命令之间的依赖关系，还可以跨平台使用。

---

### [第 256 期] Dora.ai

- 来源: docs/issue-256.md
- 链接: https://www.dora.run/
- 描述: 国人开发的一个 AI 工具，给出文本描述就能生成网页，还能添加 3D 互动。目前处于测试阶段，需要排队登记内测资格。 [Product Hunt 的投票中](https://www.producthunt.com/posts/dora-ai-alpha)，暂时排在第一，作者到周刊讨论区求票了。（[@CharlesLiuyx](https://github.com/ruanyf/weekly/issues/3144) 投稿）

---
### [第 257 期] Csv2ImageApp

- 来源: docs/issue-257.md
- 链接: https://github.com/fummicc1/csv2img
- 描述: 这个开源工具可以将 CSV 文件转成图片。

---

### [第 257 期] SAMIST

- 来源: docs/issue-257.md
- 链接: https://github.com/dibrale/samist
- 描述: 一个 Python 桌面程序，为 Meta 公司的 [AI 模型 SAM](https://segment-anything.com/) 提供了图形界面，可以提取照片里面的物体。

---

### [第 257 期] Git-Sim

- 来源: docs/issue-257.md
- 链接: https://initialcommit.com/blog/git-sim
- 描述: 一个命令行工具，可以生成图片或动画，显示某个 Git 命令对当前仓库的影响。

---

### [第 257 期] Read Something

- 来源: docs/issue-257.md
- 链接: https://github.com/ReadSomething/ReadSomething
- 描述: 一个开源的 Chrome 插件，可以将网页转成阅读模式，并且内置了 AI 总结、翻译、Mardown 转换等功能。（[@zhongyiio](https://github.com/ruanyf/weekly/issues/3162) 投稿）

---

### [第 257 期] MIB

- 来源: docs/issue-257.md
- 链接: https://github.com/QC2168/mib
- 描述: 一款开源的 Windows 桌面应用，将安卓手机备份到桌面电脑，支持增量备份。（[@QC2168](https://github.com/ruanyf/weekly/issues/3148) 投稿）

---

### [第 257 期] Rubic

- 来源: docs/issue-257.md
- 链接: https://rubic.jaskang.vip/
- 描述: 一个响应式小程序开发框架，采用跟 Vue3 一样的编程模型。（[@JasKang](https://github.com/ruanyf/weekly/issues/3150) 投稿）

---

### [第 257 期] SQLucky

- 来源: docs/issue-257.md
- 链接: https://github.com/tenie/SQLucky
- 描述: 一款开源的数据库可视化操作工具，基于 Java，用来平替同类付费软件。（[@tenie](https://github.com/ruanyf/weekly/issues/3154) 投稿）

---

### [第 257 期] flutter_chatgpt

- 来源: docs/issue-257.md
- 链接: https://github.com/bravekingzhang/flutter_chat_box
- 描述: 一款开源的 ChatGPT 聊天客户端，基于 Flutter，支持手机和桌面所有平台。（[@bravekingzhang](https://github.com/ruanyf/weekly/issues/3151) 投稿）

---

### [第 257 期] IceCubesApp

- 来源: docs/issue-257.md
- 链接: https://github.com/Dimillian/IceCubesApp
- 描述: 开源的社交媒体 Mastodon 的 iOS 客户端，功能比较多，还在不断开发中。

---

### [第 257 期] Juice Shop

- 来源: docs/issue-257.md
- 链接: https://github.com/juice-shop/juice-shop
- 描述: 一个用作安全训练的 Web 应用，里面包含了最常用的10种安全漏洞，供练习者破解。

---
### [第 258 期] Tabby

- 来源: docs/issue-258.md
- 链接: https://github.com/TabbyML/tabby
- 描述: GitHub Copilot 的开源替代品，AI 代码助手，可以自己架设，并且离线使用。它还提供 Web 界面，根据指令生成代码。

---

### [第 258 期] undb

- 来源: docs/issue-258.md
- 链接: https://github.com/undb-xyz/undb
- 描述: 一个无代码数据库操作界面，数据保存在一个文件里面。（[@nichenqin](https://github.com/ruanyf/weekly/issues/3172) 投稿）

---

### [第 258 期] jelBAN.js

- 来源: docs/issue-258.md
- 链接: https://github.com/Fcmam5/jelban-js
- 描述: 一个 JS 库，用来过滤 Email 地址，包括一次性地址和邮箱的地址别名。

---

### [第 258 期] Herowand Editor

- 来源: docs/issue-258.md
- 链接: https://editor.herowand.com/
- 描述: 一个网页工具，可以将 JSON、XML、YAML、TOML 格式的数据可视化展示。

---

### [第 258 期] sqlite-gui

- 来源: docs/issue-258.md
- 链接: https://github.com/little-brother/sqlite-gui
- 描述: 一个 Windows 系统的轻量级 SQLite 编辑器。

---

### [第 258 期] val town

- 来源: docs/issue-258.md
- 链接: https://www.val.town/
- 描述: 该网站是免费的云函数运行环境。用户在网页输入云函数，该网站可以自动运行这个函数。

---

### [第 258 期] stable-diffusion-videos

- 来源: docs/issue-258.md
- 链接: https://github.com/nateraw/stable-diffusion-videos
- 描述: 用户提供两张图片，这个工具使用开源的 Stable Diffusion 模型，生成一段视频，内容是图片 A 逐渐变成图片 B。

---

### [第 258 期] Helix

- 来源: docs/issue-258.md
- 链接: https://helix-editor.com/
- 描述: 一个现代版 Vim 编辑器，完全用 Rust 语言重写了。它跟 NeoVim 的主要不同是，它把一些主要的插件都做进去了，不用安装插件。

---

### [第 258 期] Chitchatter

- 来源: docs/issue-258.md
- 链接: https://chitchatter.im/
- 描述: 一个开源的点对点网页聊天应用，聊天内容不经过服务器，可以自己搭建，分享房间号给其他人。

---

### [第 258 期] Aether

- 来源: docs/issue-258.md
- 链接: https://getaether.net/
- 描述: 一个点对点的桌面软件，用来搭建私人社区，一组用户可以用它交换内容，一个人发帖，其他人都可以看到，不需要服务器。

---
### [第 259 期] Mosh

- 来源: docs/issue-259.md
- 链接: https://mosh.org/
- 描述: SSH 替代品，用来登陆服务器。最大特点是会话不会因为丢线而中断。下次连接或者换台机器连接，还能进入前一次会话。

---

### [第 259 期] Ezno

- 来源: docs/issue-259.md
- 链接: https://github.com/kaleidawave/ezno
- 描述: 一个用 Rust 语言写的 TypeScript 编译器，目标是作为官方 tsc 的替代品。

---

### [第 259 期] Bark

- 来源: docs/issue-259.md
- 链接: https://github.com/suno-ai/bark
- 描述: 一个语音生成引擎，效果不错，可以在朗读的同时，发出大笑、叹息和哭泣，还可以生成音乐。

---

### [第 259 期] trzsz-ssh

- 来源: docs/issue-259.md
- 链接: https://github.com/trzsz/trzsz-ssh
- 描述: 用 Go 实现的 ssh 客户端，可以记住登陆过的服务器，内置支持上传和下载文件。（[@lonnywong](https://github.com/ruanyf/weekly/issues/3180) 投稿）

---

### [第 259 期] STDF

- 来源: docs/issue-259.md
- 链接: https://github.com/dufu1991/stdf
- 描述: 基于 Svelte 与 Tailwind 的移动页面组件库。（[@dufu1991](https://github.com/ruanyf/weekly/issues/3175) 投稿）

---

### [第 259 期] code-inspector

- 来源: docs/issue-259.md
- 链接: https://github.com/zh-lx/code-inspector
- 描述: 一个 Vue 的开发者工具，点击页面上的某个元素，它自动打开代码编辑器，定位到对应的代码位置。（[@zh-lx](https://github.com/ruanyf/weekly/issues/3178) 投稿）

---

### [第 259 期] Tiny Player

- 来源: docs/issue-259.md
- 链接: https://tiny-player.vercel.app/
- 描述: 极简的网页视频播放器，支持硬解/软解，可以自定义各种控件样式。（[@wangrongding](https://github.com/ruanyf/weekly/issues/3174) 投稿）

---

### [第 259 期] BrutalityExtractor

- 来源: docs/issue-259.md
- 链接: https://github.com/hxz393/BrutalityExtractor
- 描述: Windows 解压软件，针对多核 CPU 和高速固态硬盘优化，实现多进程同时解压，比普通解压软件速度快。（[@hxz393](https://github.com/ruanyf/weekly/issues/3181) 投稿）

---

### [第 259 期] highlight.io

- 来源: docs/issue-259.md
- 链接: https://github.com/highlight/highlight
- 描述: 一个前端页面报错的监控平台，需要自己搭建，类似于 sentry，但是功能更强大一些。

---

### [第 259 期] Keyv

- 来源: docs/issue-259.md
- 链接: https://keyvhq.js.org/
- 描述: 一个键值对存储的操作库，提供简单的操作方法，支持多种数据库（MySQL、PostgreSQL、SQLite、Redis等等）作为后端。

---

### [第 259 期] Jellylade

- 来源: docs/issue-259.md
- 链接: https://app.jellylade.com/
- 描述: 一个美化网页截图的 Web 工具。

---
### [第 260 期] Tushan

- 来源: docs/issue-260.md
- 链接: https://github.com/msgbyte/tushan
- 描述: 一个基于 React 的前端框架，用来搭建网站的管理后台。（[@moonrailgun](https://github.com/ruanyf/weekly/issues/3194) 投稿）

---

### [第 260 期] SafeLine（雷池）

- 来源: docs/issue-260.md
- 链接: https://github.com/chaitin/safeline
- 描述: 开源的 WAF（应用程序防火墙），挡在网站之前对 Web 流量进行安全清洗。（[@naocanmonster](https://github.com/ruanyf/weekly/issues/3207) 投稿）

---

### [第 260 期] Vue Skia

- 来源: docs/issue-260.md
- 链接: https://github.com/rustq/vue-skia
- 描述: 一个基于 Skia 的 2D 网页图形渲染库，底层使用 Rust 语言实现，前端使用 Vue 语言。你可以把它看作 SVG 的替代方案。（[@meloalright](https://github.com/ruanyf/weekly/issues/3199) 投稿）

---

### [第 260 期] ReviewGPT

- 来源: docs/issue-260.md
- 链接: https://reviewgpt.net/
- 描述: 为你的文章进行打分、评价，提出修改意见，甚至还可以扮演莎士比亚、金庸等知名作家，帮助你重新撰写。（[@lvwzhen](https://github.com/ruanyf/weekly/issues/3206) 投稿）

---

### [第 260 期] Light Chaser

- 来源: docs/issue-260.md
- 链接: https://github.com/xiaopujun/light-chaser
- 描述: 数据可视化大屏设计器，基于 React + Mobx。（[@xiaopujun](https://github.com/ruanyf/weekly/issues/3202) 投稿）

---

### [第 260 期] 语音转字幕工具

- 来源: docs/issue-260.md
- 链接: https://godlucky.net/whisperapp/
- 描述: 仅需浏览器，AI 自动生成语音字幕，免费且可本地离线运行。（[@ZSMX](https://github.com/ruanyf/weekly/issues/3211) 投稿）

---

### [第 260 期] AI 面试助手

- 来源: docs/issue-260.md
- 链接: https://interview.sofasay.com/
- 描述: 只需职位、职位描述以及简历信息，就可以开始模拟面试，AI 扮演面试官角色提问。（[@cocomany](https://github.com/ruanyf/weekly/issues/3213) 投稿）

---

### [第 260 期] ArtQR 智绘二维码

- 来源: docs/issue-260.md
- 链接: https://hysli.io/#/projectManagement
- 描述: 一键将二维码变成一幅可扫码的画。（[@yangchuansheng](https://github.com/ruanyf/weekly/issues/3209) 投稿）

---

### [第 260 期] OrbStack

- 来源: docs/issue-260.md
- 链接: https://orbstack.dev/
- 描述: Mac 应用软件，在图形界面管理 Docker 容器，据称速度比官方的 Docker Desktop 快得多。

---
### [第 261 期] jianmu（建木）

- 来源: docs/issue-261.md
- 链接: https://jianmu.dev/
- 描述: 开源 CI/CD 工具，可视化编排 DevOps 流程。（[@lxitgto](https://github.com/ruanyf/weekly/issues/3233) 投稿）

---

### [第 261 期] Milky Warp

- 来源: docs/issue-261.md
- 链接: https://github.com/hugoattal/milky-warp
- 描述: 一个桌面程序，对任意桌面区域产生放大镜效果。

---

### [第 261 期] ICP Query

- 来源: docs/issue-261.md
- 链接: https://github.com/yuedanlabs/icp-query-extension
- 描述: 开源的 Chrome 浏览器插件，显示网站 ICP 备案、Whois、DNS、服务器位置及运营商信息。（[@yuedanlabs](https://github.com/ruanyf/weekly/issues/3223) 投稿）

---

### [第 261 期] 艺码

- 来源: docs/issue-261.md
- 链接: https://yima.me/
- 描述: 根据文字描述，将二维码转成一幅可扫描的图像的网页工具。（[@Cobb9527](https://github.com/ruanyf/weekly/issues/3226) 投稿）

---

### [第 261 期] Language Reactor

- 来源: docs/issue-261.md
- 链接: https://www.languagereactor.com/
- 描述: 浏览器插件，可以在 Netflix 和 Youtube 视频上，同时显示两种语言的字幕，方便学习外语。

---

### [第 261 期] Directus

- 来源: docs/issue-261.md
- 链接: https://github.com/directus/directus
- 描述: 这个工具运行在各种数据库之上，自动为数据库生成 REST +  GraphQL API，使得它们可以网络访问操作，并自带一个 Web 仪表盘。

---

### [第 261 期] CheerpJ

- 来源: docs/issue-261.md
- 链接: https://leaningtech.com/announcing-cheerpj-3-0-a-jvm-replacement-in-html5-and-webassembly-to-run-java-applications-and-applets-on-modern-browsers/
- 描述: 一个实验性工具，将 JVM 解释器搬上网页，让 Java 代码可以直接在网页运行。

---

### [第 261 期] SailboatUI

- 来源: docs/issue-261.md
- 链接: https://sailboatui.com/
- 描述: 一个基于 Tailwind CSS 的 UI 组件库，目前有超过150个组件。

---

### [第 261 期] komorebi

- 来源: docs/issue-261.md
- 链接: https://github.com/LGUG2Z/komorebi
- 描述: Windows 系统的窗口管理器，自动在桌面编排多个应用程序窗口。

---

### [第 261 期] WezTerm

- 来源: docs/issue-261.md
- 链接: https://wezfurlong.org/wezterm/
- 描述: 一个跨平台的终端模拟器，采用 GPU 加速，在显示上面有一定的性能优势。 另外，再推荐一个终端模拟器 [Hyper](https://hyper.is/)，它基于 Electron，使用 HTML/CSS/JS 构建，充分利用了网页技术。

---
### [第 262 期] Connect-Web

- 来源: docs/issue-262.md
- 链接: https://connect.build/
- 描述: 一个 TypeScript 库，用于从浏览器调用 RPC 服务器，参见[介绍文章](https://buf.build/blog/connect-web-protobuf-grpc-in-the-browser)。

---

### [第 262 期] xBrowserSync

- 来源: docs/issue-262.md
- 链接: https://www.xbrowsersync.org/
- 描述: 一个浏览器的同步插件，最大特点是跨浏览器同步，比如安卓的 Chrome 同步了桌面的 Firefox。

---

### [第 262 期] I Don't Care About Commit Message

- 来源: docs/issue-262.md
- 链接: https://github.com/mefengl/vscode-i-dont-care-about-commit-message
- 描述: VS Code 插件，使用 AI 自动生成代码提交的 Commit 摘要，你就不必自己写了。它需要 OpenAI API Key。（[@mefengl](https://github.com/ruanyf/weekly/issues/3248) 投稿）

---

### [第 262 期] React1s

- 来源: docs/issue-262.md
- 链接: https://github.com/aaamoon/react1s
- 描述: 浏览器插件，本地开发 React 项目时，点击页面元素，就会跳转到编辑器的对应组件位置。（[@aaamoon](https://github.com/ruanyf/weekly/issues/3268) 投稿）

---

### [第 262 期] TGSCAN

- 来源: docs/issue-262.md
- 链接: https://github.com/tgscan-dev/tgscan
- 描述: 开源的 Telegram 搜索引擎。（[@HandelDev](https://github.com/ruanyf/weekly/issues/3263) 投稿）

---

### [第 262 期] LeaferJS

- 来源: docs/issue-262.md
- 链接: https://www.leaferjs.com/
- 描述: 一个国产的 Canvas 2D 图形渲染引擎，追求极致性能。（[@leaferjs](https://github.com/ruanyf/weekly/issues/3246) 投稿）

---

### [第 262 期] AltTab

- 来源: docs/issue-262.md
- 链接: https://github.com/lwouis/alt-tab-macos
- 描述: 这个软件可以让 Mac 电脑具备 Windows 的 alt + tab 键的功能，方便地切换各个窗口。

---

### [第 262 期] Rsync time backup

- 来源: docs/issue-262.md
- 链接: https://github.com/laurent22/rsync-time-backup
- 描述: 一个命令行工具，类似于苹果的 Time Machine 备份工具，对文件和目录进行增量备份，以后可以恢复到任意时点。它支持跨平台使用。

---

### [第 262 期] XState

- 来源: docs/issue-262.md
- 链接: https://xstate.js.org/
- 描述: 一个 JS 库，实现了有限状态机，设计得很简洁，可以用来学习有限状态机。

---

### [第 262 期] hat-syslog

- 来源: docs/issue-262.md
- 链接: https://github.com/hat-open/hat-syslog
- 描述: Linux 系统日志 Syslog 的图形操作工具。

---
### [第 263 期] hiSHtory

- 来源: docs/issue-263.md
- 链接: https://github.com/ddworken/hishtory
- 描述: 一个强大的 Shell 操作历史的搜索工具，可以替代 Bash 内置的 ctrl-r 搜索。

---

### [第 263 期] TinyVG

- 来源: docs/issue-263.md
- 链接: https://tinyvg.tech/
- 描述: SVG 图片格式的二进制版本，可以大大缩小 SVG 文件体积。

---

### [第 263 期] Gitstars

- 来源: docs/issue-263.md
- 链接: https://github.com/cfour-hi/gitstars
- 描述: 一个开源的在线服务，用来管理你在 GitHub 打过星标的项目（收藏的项目）。（[@cfour-hi](https://github.com/ruanyf/weekly/issues/3286) 投稿）

---

### [第 263 期] 迅排设计

- 来源: docs/issue-263.md
- 链接: https://github.com/palxiao/poster-design
- 描述: 开源的在线海报图片设计器。（[@palxiao](https://github.com/ruanyf/weekly/issues/3284) 投稿）

---

### [第 263 期] Spring Startup Ananlyzer

- 来源: docs/issue-263.md
- 链接: https://github.com/linyimin0812/spring-startup-analyzer
- 描述: Spring 性能分析工具，收集启动过程数据，生成交互式分析报告。（[@linyimin0812](https://github.com/ruanyf/weekly/issues/3280) 投稿）

---

### [第 263 期] WebAV

- 来源: docs/issue-263.md
- 链接: https://github.com/hughfenghen/WebAV
- 描述: Chrome 94 开放了 WebCodecs API，意味着 JS 也能处理音视频了。这是一个实验性项目，尝试提供简单易用的 API 在浏览器中处理音视频数据。（[@hughfenghen](https://github.com/ruanyf/weekly/issues/3282) 投稿）

---

### [第 263 期] kafka-console-ui

- 来源: docs/issue-263.md
- 链接: https://github.com/xxd763795151/kafka-console-ui
- 描述: 一款轻量级的 Kafka 可视化管理平台。（[@xxd763795151](https://github.com/ruanyf/weekly/issues/3272) 投稿）

---

### [第 263 期] killport

- 来源: docs/issue-263.md
- 链接: https://github.com/jkfran/killport
- 描述: 一个 Rust 语言写的命令行程序，可以杀死占用指定端口的进程。

---

### [第 263 期] Sniffnet

- 来源: docs/issue-263.md
- 链接: https://github.com/GyulyVGC/sniffnet
- 描述: 一个跨平台桌面应用，用来追踪监控网络流量，并以可视化的方式呈现。

---
### [第 264 期] Aimless.js

- 来源: docs/issue-264.md
- 链接: https://github.com/ChrisCavs/aimless.js
- 描述: 一个生成各种随机值的 JS 库。

---

### [第 264 期] Primo

- 来源: docs/issue-264.md
- 链接: https://primocms.org/
- 描述: 一个开源的内容管理系统（CMS），作为 WordPress 的替代品而开发，基于 JavaScript 的 Svelte 框架。

---

### [第 264 期] Link Redirect Trace

- 来源: docs/issue-264.md
- 链接: https://chrome.google.com/webstore/detail/link-redirect-trace/nnpljppamoaalgkieeciijbcccohlpoh
- 描述: 一个浏览器插件，显示当前页面的所有重定向跳转。

---

### [第 264 期] Clang.js

- 来源: docs/issue-264.md
- 链接: https://github.com/luoxuhai/clang.js
- 描述: 在浏览器直接运行 C/C++ 代码。（[@luoxuhai](https://github.com/ruanyf/weekly/issues/3297) 投稿）

---

### [第 264 期] mess-reader

- 来源: docs/issue-264.md
- 链接: https://github.com/ppz-pro/mess-reader
- 描述: 一个网页的 Epub 阅读器，可以离线使用。（[@daGaiGuanYu](https://github.com/ruanyf/weekly/issues/3302) 投稿）

---

### [第 264 期] Automa

- 来源: docs/issue-264.md
- 链接: https://www.automa.site/
- 描述: Chrome 浏览器插件，用来设置任务自动化。另外，Chrome 有内置的[用户行为录制](https://developer.chrome.com/docs/devtools/recorder/)。（[@dllen](https://github.com/ruanyf/weekly/issues/3301) 投稿）

---

### [第 264 期] Rickrack

- 来源: docs/issue-264.md
- 链接: https://eigenmiao.com/yanhuo
- 描述: （焰火十二卷） 开源的调色板软件，提供多种色彩搭配功能，适用于各种设计场景。（[@eigenmiao](https://github.com/ruanyf/weekly/issues/3306) 投稿）

---

### [第 264 期] iFrame Resizer

- 来源: docs/issue-264.md
- 链接: http://davidjbradshaw.github.io/iframe-resizer/
- 描述: 一个控制 iframe 窗口的 JS 库，可以根据加载网页的内容，调整 iframe 窗口的高度和宽度，并提供许多其他功能。

---

### [第 264 期] Standard Ebooks

- 来源: docs/issue-264.md
- 链接: https://github.com/standardebooks/tools
- 描述: Epub 电子书生成工具，参见[教程](https://standardebooks.org/contribute/producing-an-ebook-step-by-step)。

---

### [第 264 期] Tablane

- 来源: docs/issue-264.md
- 链接: https://tablane.net/
- 描述: 一个[开源](https://github.com/Tablane/tablane)的 Web 软件，用来进行任务管理。它实际上是一个列表管理软件，任何可以表示成列表的东西，都可以用它管理。

---
### [第 265 期] Vanilla

- 来源: docs/issue-265.md
- 链接: https://open.vanillaforums.com/
- 描述: PHP 的论坛程序，功能强大，也很美观。

---

### [第 265 期] GitHub 名片

- 来源: docs/issue-265.md
- 链接: https://github-business-card.vercel.app/
- 描述: 这个网页可以根据 GitHub 主页，生成用户的 GitHub 名片。

---

### [第 265 期] Equal UI

- 来源: docs/issue-265.md
- 链接: https://equal-ui.github.io/Equal/
- 描述: 基于 Tailwind CSS 的一套 Vue 3 组件库。

---

### [第 265 期] emaction

- 来源: docs/issue-265.md
- 链接: https://github.com/emaction/emaction.frontend
- 描述: 一个 Web Component，生成类似 GitHub 的 Emoji 反馈栏。（[@tiezhudotwang](https://github.com/ruanyf/weekly/issues/3309) 投稿）

---

### [第 265 期] ChatHub

- 来源: docs/issue-265.md
- 链接: https://github.com/chathub-dev/chathub
- 描述: 浏览器插件，在一个页面中同时使用多个 GPT （ChatGPT、new Bing Chat、Google Bard、Claude 等）。（[@wong2](https://github.com/ruanyf/weekly/issues/3310) 投稿）

---

### [第 265 期] Whistle 客户端

- 来源: docs/issue-265.md
- 链接: https://github.com/avwo/whistle-client
- 描述: 一个基于 Whistle (命令行版本) + Electron 的跨平台桌面程序，用来调试各种网络请求，查看流量细节。（[@ATQQ](https://github.com/ruanyf/weekly/issues/3312) 投稿）

---

### [第 265 期] Erin

- 来源: docs/issue-265.md
- 链接: https://erin-homepage.vercel.app/
- 描述: Chrome 浏览器插件，将标签显示为类似 macOS 底部 Dock 图标栏的风格。（[@Developer27149](https://github.com/ruanyf/weekly/issues/3318) 投稿）

---

### [第 265 期] AI Code Translator

- 来源: docs/issue-265.md
- 链接: https://aicodeconvert.com/
- 描述: 该网站可以将一种语言的程序，转换成另一种语言。用户也可以描述想要什么程序，它来生成代码。（[@JustAIGitHub](https://github.com/ruanyf/weekly/issues/3322) 投稿）

---

### [第 265 期] Slashbase

- 来源: docs/issue-265.md
- 链接: https://github.com/slashbaseide/slashbase
- 描述: 一个基于浏览器的数据库操作 IDE，有点类似 PHPMyAdmin，但使用 Go 语言编写，并且支持 PostgreSQL 和 MongoDB。

---

### [第 265 期] YouPlot

- 来源: docs/issue-265.md
- 链接: https://github.com/red-data-tools/YouPlot
- 描述: 一个命令行工具，可以在终端显示图形。

---

### [第 265 期] PrettyPolly

- 来源: docs/issue-265.md
- 链接: https://www.prettypolly.app/app
- 描述: 学习外语时，最好有一个对话环境，可以练习口语，这个 AI 应用就解决了这个问题。 它目前提供26种语言（包括中文、日文和韩文），你在网页上选择一种，就可以与 AI 进行口语练习了。感觉以后国内的外语培训产业，都要被 AI 取代了。

---
### [第 266 期] TypeCell

- 来源: docs/issue-266.md
- 链接: https://www.typecell.org/
- 描述: 一个 TypeScript 互动式网页环境，可以在网页文档上直接查看代码运行结果，类似于 Jupyter 笔记本，适合内嵌 TypeScript 代码的文档。

---

### [第 266 期] 小抽屉

- 来源: docs/issue-266.md
- 链接: https://play.google.com/store/apps/details?id=com.mydobby.pandora
- 描述: 安卓 App，可以实现屏幕翻译，方便使用外国 App。（[@tuesda](https://github.com/ruanyf/weekly/issues/3328) 投稿）

---

### [第 266 期] FoodCa

- 来源: docs/issue-266.md
- 链接: https://apps.apple.com/cn/app/foodca-ai%E5%8A%A0%E6%8C%81%E7%9A%84%E9%A3%9F%E7%89%A9%E7%83%AD%E9%87%8F%E9%80%9F%E6%9F%A5%E4%B8%8E%E8%AE%B0%E5%BD%95%E5%B7%A5%E5%85%B7/id6451112435
- 描述: 一个 iOS 应用，基于 chatGPT，实现口语化的输入来记录食物热量，例如“我吃了三颗葡萄”。（[@wdkwdkwdk](https://github.com/ruanyf/weekly/issues/3330) 投稿）

---

### [第 266 期] 抖音聊天（PC 版）

- 来源: docs/issue-266.md
- 链接: https://imdesktop.douyin.com/
- 描述: 抖音推出的 PC 端聊天软件。（[@stefanJi](https://github.com/ruanyf/weekly/issues/3329) 投稿）

---

### [第 266 期] 麦默笔记

- 来源: docs/issue-266.md
- 链接: https://github.com/usememos/memos
- 描述: （memos） 基于 Web 的个人笔记软件，需要自己搭建服务，可以实现与其他站点的聚合。（[@pmxiao](https://github.com/ruanyf/weekly/issues/3349) 投稿）

---

### [第 266 期] PDDON

- 来源: docs/issue-266.md
- 链接: https://pddon.com/
- 描述: 一款在线画图工具，提供低代码和 AI 智能辅助工具。（[@pddon](https://github.com/ruanyf/weekly/issues/3351) 投稿）

---

### [第 266 期] Ruff

- 来源: docs/issue-266.md
- 链接: https://github.com/astral-sh/ruff
- 描述: Rust 语言写的 Python Linter，用来检查 Python 代码是否风格正确，运行速度非常快。

---

### [第 266 期] ReactPy

- 来源: docs/issue-266.md
- 链接: https://reactpy.dev/docs/index.html
- 描述: 使用 Python 实现的 React 框架，让你用 Python 写前端 HTML 页面。

---

### [第 266 期] Wasmer

- 来源: docs/issue-266.md
- 链接: https://wasmer.io/
- 描述: 一个命令行工具，直接在命令行下运行 wasm 模块，参见[介绍文章](https://wasmer.io/posts/announcing-wasmer-3.0)。

---

### [第 266 期] GoodbyeDPI

- 来源: docs/issue-266.md
- 链接: https://github.com/ValdikSS/GoodbyeDPI
- 描述: 这个工具是俄罗斯程序员写的，旨在绕过该国的“深度包检测”（DPI），只适用于 Windows。

---
### [第 267 期] Novel

- 来源: docs/issue-267.md
- 链接: https://github.com/steven-tey/novel
- 描述: 一个类似 notion 那样的“所见即所得”的网页编辑器，支持 AI 生成内容。

---

### [第 267 期] trurl

- 来源: docs/issue-267.md
- 链接: https://github.com/curl/trurl
- 描述: curl 的作者 Daniel Stenberg 新写的命令行工具，用来解析和操作 URL。

---

### [第 267 期] WingetUI

- 来源: docs/issue-267.md
- 链接: http://www.marticliment.com/wingetui/
- 描述: Windows 命令行包管理器 Winget 的 非官方 UI 界面。

---

### [第 267 期] Bytebase

- 来源: docs/issue-267.md
- 链接: https://www.oschina.net/p/bytebase
- 描述: 国产的数据库数据结构（schema）管理工具，基于 Web 界面，需要自己部署，支持各种主流数据库。（[@shandbb](https://github.com/ruanyf/weekly/issues/3367) 投稿）

---

### [第 267 期] DevPod

- 来源: docs/issue-267.md
- 链接: https://devpod.sh/
- 描述: 一个桌面软件，让本地 IDE 的运行结果自动保存到远程，类似于自己搭建 GitHub 的 CodeSpace，支持各种后端（包括 SSH 和云主机）。

---

### [第 267 期] Anime.js

- 来源: docs/issue-267.md
- 链接: https://animejs.com/
- 描述: 一个轻量级 JavaScript 动画库，具有简单但强大的 API。

---

### [第 267 期] Mailpit

- 来源: docs/issue-267.md
- 链接: https://github.com/axllent/mailpit
- 描述: 一个电子邮件测试工具，用来验证你的应用发送邮件是否正常，可以拦截邮件，并自带 SMTP 测试工具。

---

### [第 267 期] OpenResume

- 来源: docs/issue-267.md
- 链接: https://github.com/xitanggg/open-resume
- 描述: 一个开源的简历生成器，还支持将现有的简历导入。

---

### [第 267 期] Glitch Text Generator

- 来源: docs/issue-267.md
- 链接: https://glitchtext.net/
- 描述: 为字符加上毛刺效果的网页工具。（[@maojindao55](https://github.com/ruanyf/weekly/issues/3373) 投稿）

---

### [第 267 期] Fresns

- 来源: docs/issue-267.md
- 链接: https://fresns.cn
- 描述: 一款开源的 PHP 应用，可以根据需要作为论坛、社交网络、CMS 系统等使用。（[@jevantang](https://github.com/ruanyf/weekly/issues/3374) 投稿）

---
### [第 268 期] Simple Statistics

- 来源: docs/issue-268.md
- 链接: http://simplestatistics.org/
- 描述: 一个统计学的 JS 库，提供基本的统计函数。

---

### [第 268 期] 豆包

- 来源: docs/issue-268.md
- 链接: https://www.doubao.com/
- 描述: 字节推出的 ChatGPT 类产品，免费使用。

---

### [第 268 期] TrackerControl

- 来源: docs/issue-268.md
- 链接: https://github.com/TrackerControl/tracker-control-android
- 描述: 一个手机 App，用来监控手机软件对于用户行为的数据收集（即跟踪行为）。（[@cheanus](https://github.com/ruanyf/weekly/issues/3381) 投稿）

---

### [第 268 期] DCNews

- 来源: docs/issue-268.md
- 链接: https://github.com/121812/dcnews
- 描述: 一个开源的 Go 应用，将微信群的聊天消息，自动同步到预设的 Discord 频道。（[@121812](https://github.com/ruanyf/weekly/issues/3382) 投稿）

---

### [第 268 期] Walrus

- 来源: docs/issue-268.md
- 链接: https://github.com/seal-io/walrus
- 描述: 一个开源的应用管理平台，让开发人员无需了解底层平台的细节，即可自助进行部署、管理和交付。（[@Aleegra](https://github.com/ruanyf/weekly/issues/3385) 投稿）

---

### [第 268 期] GFPGAN

- 来源: docs/issue-268.md
- 链接: https://github.com/TencentARC/GFPGAN
- 描述: 腾讯开源的旧照片 AI 修复，查看 [Demo](https://replicate.com/tencentarc/gfpgan)。（[@Y024](https://github.com/ruanyf/weekly/issues/3387) 投稿）

---

### [第 268 期] 铜钟

- 来源: docs/issue-268.md
- 链接: https://tonzhon.com/
- 描述: 一个主打“听歌”功能的 Web App，有丰富的音乐资源、简洁的 UI 和方便的交互，[代码开源](https://github.com/enzeberg/tonzhon-music)。（[@enzeberg](https://github.com/ruanyf/weekly/issues/3392) 投稿）

---

### [第 268 期] auto-animate

- 来源: docs/issue-268.md
- 链接: https://github.com/formkit/auto-animate
- 描述: 一个网页动画库，可以为网页应用添加平滑的过渡，支持各种主流框架。（[@GenerQAQ](https://github.com/ruanyf/weekly/issues/3398) 投稿）

---

### [第 268 期] background-removal-js

- 来源: docs/issue-268.md
- 链接: https://github.com/imgly/background-removal-js
- 描述: 一个去除图片背景的 JS 库。

---

### [第 268 期] scrcpy

- 来源: docs/issue-268.md
- 链接: https://github.com/Genymobile/scrcpy
- 描述: 一个跨平台的桌面应用，映射安卓手机的屏幕到电脑桌面，允许使用鼠标和键盘控制手机。

---
### [第 269 期] youki

- 来源: docs/issue-269.md
- 链接: https://github.com/containers/youki
- 描述: 一个用 Rust 语言写的 Docker 镜像运行器。

---

### [第 269 期] Tabserve

- 来源: docs/issue-269.md
- 链接: https://tabserve.dev/
- 描述: 一个有趣的网络应用，浏览器只要访问它的网站，就能建立一个反向代理，让公网可以访问你的当前计算机（即 localhost）。

---

### [第 269 期] React18 JSON View

- 来源: docs/issue-269.md
- 链接: https://github.com/YYsuni/react18-json-view
- 描述: 一个展示 JSON 数据的 React 组件。（[@YYsuni](https://github.com/ruanyf/weekly/issues/3400) 投稿）

---

### [第 269 期] dtrx

- 来源: docs/issue-269.md
- 链接: https://github.com/dtrx-py/dtrx
- 描述: 一个基于 Python 的命令行工具，可以解开大部分压缩格式。相当于只装一个工具，就能解开各种压缩包。（[@lengyijun](https://github.com/ruanyf/weekly/issues/3401) 投稿）

---

### [第 269 期] Transmate

- 来源: docs/issue-269.md
- 链接: https://transmate.ai/
- 描述: 浏览器插件，利用 ChatGPT 批量翻译各种格式的文档。（[@isuperwm](https://github.com/ruanyf/weekly/issues/3405) 投稿）

---

### [第 269 期] examor

- 来源: docs/issue-269.md
- 链接: https://github.com/codeacme17/examor
- 描述: 这个工具允许用户上传文档，它会根据这些文档生成各种问答题，可以用来面试、教学和复习。它代码开源，需要用户自己搭建服务。（[@codeacme17](https://github.com/ruanyf/weekly/issues/3408) 投稿）

---

### [第 269 期] 极速图片压缩器

- 来源: docs/issue-269.md
- 链接: https://www.ticompressor.com/online/
- 描述: 一款图片压缩软件，有在线版和 Windows 桌面版。（[@Dreamer365](https://github.com/ruanyf/weekly/issues/3417) 投稿）

---

### [第 269 期] 漫画工厂

- 来源: docs/issue-269.md
- 链接: https://huggingface.co/spaces/jbilcke-hf/comic-factory
- 描述: 一个 AI 引擎，输入剧情自动产生多种风格漫画（日式、美式等等）。（[@Y024](https://github.com/ruanyf/weekly/issues/3420) 投稿）

---

### [第 269 期] DB-GPT

- 来源: docs/issue-269.md
- 链接: http://dev.dbgpt.site/
- 描述: 用户上传 Excel 文件，该[开源](https://github.com/eosphoros-ai/DB-GPT/)工具让你与文件聊天，向它发出指令。（[@csunny](https://github.com/ruanyf/weekly/issues/3423) 投稿）

---

### [第 269 期] use autojump in vscode

- 来源: docs/issue-269.md
- 链接: https://marketplace.visualstudio.com/items?itemName=webxmsj.autojump
- 描述: VSCode 插件，用户可以使用快捷键，跳转到指定目录，类似于 z、autojump、zoxide 等命令行工具。（[@webxmsj](https://github.com/ruanyf/weekly/issues/3419) 投稿）

---
### [第 270 期] Figma.Pub

- 来源: docs/issue-270.md
- 链接: https://figma.pub/
- 描述: 为 figma 设计稿生成可自动更新的图片链接，支持 jpg 、png 、svg 格式和 scale 参数。（[@airyland](https://github.com/ruanyf/weekly/issues/3431) 投稿）

---

### [第 270 期] MusicFree 桌面版

- 来源: docs/issue-270.md
- 链接: https://github.com/maotoumao/MusicFreeDesktop
- 描述: 一个开源的音乐播放器，通过插件支持各种音源，参见[示例插件库](https://github.com/maotoumao/MusicFreePlugins)。（[@maotoumao](https://github.com/ruanyf/weekly/issues/3451) 投稿）

---

### [第 270 期] NiceShots

- 来源: docs/issue-270.md
- 链接: https://apps.apple.com/cn/app/niceshots/id6450619697
- 描述: 一个 iOS App，用来美化手机截图，可以实现带手机壳效果。（[@JimmyByte](https://github.com/ruanyf/weekly/issues/3452) 投稿）

---

### [第 270 期] TabX

- 来源: docs/issue-270.md
- 链接: https://github.com/Developer27149/tabX
- 描述: 一个 Chrome 插件，用来管理 Tab 页。（[@Developer27149](https://github.com/ruanyf/weekly/issues/3441) 投稿）

---

### [第 270 期] AI 小镇

- 来源: docs/issue-270.md
- 链接: https://github.com/get-convex/ai-town
- 描述: 一个开源的网页游戏，人物都是 AI 驱动的，用户加入这个虚拟小镇，就可以跟这些角色互动。（[@dllen](https://github.com/ruanyf/weekly/issues/3442) 投稿）

---

### [第 270 期] Android-Touch-Helper

- 来源: docs/issue-270.md
- 链接: https://github.com/zfdang/Android-Touch-Helper
- 描述: 开源的安卓手机的开屏广告自动跳过助手。（[@Lyeragain](https://github.com/ruanyf/weekly/issues/3402#issuecomment-1704958856) 投稿）

---

### [第 270 期] MagicNotch

- 来源: docs/issue-270.md
- 链接: https://apps.apple.com/cn/app/magicnotch-elegant-shortcut/id6447055708?mt=12
- 描述: 一款 macOS 刘海屏工具，将快捷键藏在刘海里面，鼠标移入时显示。（[@fengyiqicoder](https://github.com/ruanyf/weekly/issues/3445) 投稿）

---

### [第 270 期] 文件桥

- 来源: docs/issue-270.md
- 链接: https://github.com/ppz-pro/file-bridge
- 描述: 一个简单的 JS 脚本，用来架设静态文件服务器。A 电脑在网页上打开一个本地文件目录，B 电脑就能下载里面的文件，两者不必在同一局域网。（[@daGaiGuanYu](https://github.com/ruanyf/weekly/issues/3449) 投稿）

---

### [第 270 期] Whisper Web

- 来源: docs/issue-270.md
- 链接: https://huggingface.co/spaces/Xenova/whisper-web
- 描述: 不必登录，将英语音频转成文本的在线工具。（[@Y024](https://github.com/ruanyf/weekly/issues/3457) 投稿）

---

### [第 270 期] StableDiffusion XL 体验站

- 来源: docs/issue-270.md
- 链接: https://www.stablediffusionai.ai/
- 描述: SDXL 是 Stable Diffusion 最新发布的画图模型。这是网友架设的体验站，不需要登陆也不需要付费，直接体验文生图。（[@zengdamo](https://github.com/ruanyf/weekly/issues/3455) 投稿）

---
### [第 271 期] echoserver

- 来源: docs/issue-271.md
- 链接: https://echoserver.dev/
- 描述: 一个免费服务，你可以定制这台服务器返回的 HTTP 数据头，适合用来测试。

---

### [第 271 期] DocuSeal

- 来源: docs/issue-271.md
- 链接: https://github.com/docusealco/docuseal
- 描述: 创建、填写、签名数字文档的在线工具，代码开源。

---

### [第 271 期] g

- 来源: docs/issue-271.md
- 链接: https://github.com/Equationzhao/g
- 描述: Go 语言写的 ls 命令替代品，跨平台。（[@Equationzhao](https://github.com/ruanyf/weekly/issues/3465) 投稿）

---

### [第 271 期] Github Old Feed

- 来源: docs/issue-271.md
- 链接: https://github.com/wangrongding/github-old-feed
- 描述: 一个油猴脚本，恢复 GitHub 首页的旧版 feed，查看自己关注的人的动态。（[@wangrongding](https://github.com/ruanyf/weekly/issues/3478) 投稿）

---

### [第 271 期] LoremGenie

- 来源: docs/issue-271.md
- 链接: https://loremgenie.com
- 描述: Figma 插件，快速生成用来占位的数据文字，插入设计稿。（[@guojiangnian](https://github.com/ruanyf/weekly/issues/3473) 投稿）

---

### [第 271 期] NoteAI

- 来源: docs/issue-271.md
- 链接: https://noteai.com/
- 描述: 用户在该网站输入问题，它会用 AI 从搜索引擎返回的网页结果里面，总结出答案。

---

### [第 271 期] Idify

- 来源: docs/issue-271.md
- 链接: https://github.com/zhbhun/idify
- 描述: 一个开源软件，将用户上传的人像照，转成证件照，全部使用前端代码，数据不会上传。（[@zhbhun](https://github.com/ruanyf/weekly/issues/3481) 投稿）

---

### [第 271 期] Plane

- 来源: docs/issue-271.md
- 链接: https://github.com/makeplane/plane
- 描述: 一个基于 Web 的开源项目管理工具，JIRA 的替代品。

---

### [第 271 期] Octos

- 来源: docs/issue-271.md
- 链接: https://github.com/underpig1/octos
- 描述: 一个开源的 Windows 桌面软件，用来创建和管理 HTML、CSS 和 JS 做的实时交互式壁纸。

---

### [第 271 期] 作文批改

- 来源: docs/issue-271.md
- 链接: https://www.essay.art/
- 描述: 使用 GPT4 对雅思作文和托福作文判分和批改。（[@zengdamo](https://github.com/ruanyf/weekly/issues/3483) 投稿）

---

### [第 271 期] RustRover

- 来源: docs/issue-271.md
- 链接: https://www.jetbrains.com/rust/
- 描述: JetBrains 公司最新推出的 Rust 语言 IDE，目前免费使用。

---
### [第 272 期] Linkwarden

- 来源: docs/issue-272.md
- 链接: https://github.com/linkwarden/linkwarden
- 描述: 一个开源的桌面程序，用来管理网络书签。

---

### [第 272 期] v0

- 来源: docs/issue-272.md
- 链接: https://v0.dev/
- 描述: Vercel 推出的一个实验性产品，使用 AI 网页生成网页。 你用文字描述想要什么页面，它会给出三个 UI 设计，让你选一个，然后生成该页面的 React + Tailwind CSS 实现，并允许不断微调。 官网有很多作品展示，其中有几个相当可以（上图）。它应该是目前最强的 AI 网页生成器。现在还处于 Alpha 阶段，使用资格需要排队等待开通。（[@James-Lam](https://github.com/ruanyf/weekly/issues/3486) 投稿）

---

### [第 272 期] Extension Manager

- 来源: docs/issue-272.md
- 链接: https://github.com/JasonGrass/auto-extension-manager
- 描述: 一个浏览器插件，用来管理浏览器安装的各种插件，弥补系统自带的扩展管理器的不足。（[@JasonGrass](https://github.com/ruanyf/weekly/issues/3500) 投稿）

---

### [第 272 期] 讯飞星火认知大模型

- 来源: docs/issue-272.md
- 链接: https://passport.xfyun.cn/login
- 描述: 讯飞公司的 AI 大模型，可以根据提示生成 PPT 和简历，以及文档问答。（[@huiyanghu12](https://github.com/ruanyf/weekly/issues/3502) 投稿）

---

### [第 272 期] Subdomain Center

- 来源: docs/issue-272.md
- 链接: https://www.subdomain.center/
- 描述: 该网站可以查询一个域名有多少个子域名，点击查询框后，通过可以直接改地址栏的 URL 来查询。它的[代码开源](https://github.com/ARPSyndicate/puncia)。

---

### [第 272 期] Sqids

- 来源: docs/issue-272.md
- 链接: https://sqids.org/
- 描述: 一个生成短字母 ID 的库，有各种主要语言的版本。

---

### [第 272 期] Webrecorder

- 来源: docs/issue-272.md
- 链接: https://webrecorder.net/
- 描述: 一个工具包，用来保存交互式网页，做到离线时也能尽可能准确地重现它。

---

### [第 272 期] Reflex

- 来源: docs/issue-272.md
- 链接: https://github.com/reflex-dev/reflex
- 描述: 一个 Python 语言的前端 UI 框架，适合不想用 JavaScript 写前端网页的 Python 程序员。

---
### [第 273 期] Gitness

- 来源: docs/issue-273.md
- 链接: https://github.com/harness/gitness
- 描述: 最新出现的 GitHub 开源替代品，用于自己架设服务，托管代码。

---

### [第 273 期] Dexie.js

- 来源: docs/issue-273.md
- 链接: https://github.com/dexie/Dexie.js
- 描述: 浏览器原生数据库 IndexedDB 的包装库，提供易于操作的 API。

---

### [第 273 期] WeOCR

- 来源: docs/issue-273.md
- 链接: https://ocr.plantree.me/ocr
- 描述: 一个图片文字识别的 OCR 网站，可以离线使用。（[@plantree](https://github.com/ruanyf/weekly/issues/3517) 投稿）

---

### [第 273 期] 小鹿查单词

- 来源: docs/issue-273.md
- 链接: https://apps.apple.com/app/id6447361715
- 描述: 一个苹果设备的 App，用于语音查单词，你读一遍每个字母（比如 h-e-l-l-o），它就显示单词的意思。（[@haozes](https://github.com/ruanyf/weekly/issues/3509) 投稿）

---

### [第 273 期] DevToys

- 来源: docs/issue-273.md
- 链接: https://devtoys.app/
- 描述: 一款 Windows 的小工具集合，收入了开发者会用到的许多小工具。（[@dllen](https://github.com/ruanyf/weekly/issues/3533) 投稿）

---

### [第 273 期] Sutando

- 来源: docs/issue-273.md
- 链接: https://sutando.org/
- 描述: 一个 Node.js 的 ORM 库，用来操作关系型数据库。（[@kiddyuchina](https://github.com/ruanyf/weekly/issues/3534) 投稿）

---

### [第 273 期] Inke

- 来源: docs/issue-273.md
- 链接: https://github.com/yesmore/inke
- 描述: Notion 风格的开源 Web 笔记本，集成了 AI 自动补全（需要 OpenAI Key）。（[@yesmore](https://github.com/ruanyf/weekly/issues/3545) 投稿）

---

### [第 273 期] FastBootstrap

- 来源: docs/issue-273.md
- 链接: https://fastbootstrap.com/
- 描述: Atlassian 公司基于 Bootstrap v5.2 开发的一套 UI 开源组件库。

---

### [第 273 期] Jailer

- 来源: docs/issue-273.md
- 链接: https://github.com/Wisser/Jailer
- 描述: 一个跨平台的桌面软件，用来浏览关系型数据库的关系模型。

---
### [第 274 期] Mycelite

- 来源: docs/issue-274.md
- 链接: https://github.com/mycelial/mycelite
- 描述: 一个 SQLite 扩展，用来从一个 SQLite 实例同步到另一个，适合从本地向服务端同步数据。

---

### [第 274 期] Pictode

- 来源: docs/issue-274.md
- 链接: https://github.com/JessYan0913/pictode
- 描述: 一个开源的网页绘图编辑器。（[@JessYan0913](https://github.com/ruanyf/weekly/issues/3567) 投稿）

---

### [第 274 期] Squircle-CE

- 来源: docs/issue-274.md
- 链接: https://github.com/massivemadness/Squircle-CE
- 描述: 一个开源的安卓代码编辑器，在手机上开发代码。

---

### [第 274 期] LocalSend

- 来源: docs/issue-274.md
- 链接: https://localsend.org/
- 描述: 一款开源的跨平台文件传送软件，不需要互联网连接，依靠共享 Wifi 分享文件。

---

### [第 274 期] Uninstallr

- 来源: docs/issue-274.md
- 链接: https://uninstalr.com/
- 描述: 一个免费的 Windows 卸载程序，号称可以准确、完整地卸载各种 Windows 软件，残留最少，参见[作者自述](https://jv16powertools.com/blog/comparing-windows-uninstallers-and-making-uninstalr/)。

---

### [第 274 期] Auto-i18n

- 来源: docs/issue-274.md
- 链接: https://github.com/linyuxuanlin/Auto-i18n
- 描述: 它使用 GitHub Actions 和 ChatGPT，将仓库里面的 Markdown 文件翻译成其他语言，适合制作网站的国际化版本。（[@linyuxuanlin](https://github.com/ruanyf/weekly/issues/3564) 投稿）

---

### [第 274 期] 在线 ffmpeg

- 来源: docs/issue-274.md
- 链接: https://ffmpeg-online.vercel.app/
- 描述: 网页版的 ffmpeg，可以离线在网页上执行 ffmpeg 命令行，来编辑视频。

---

### [第 274 期] little-rat

- 来源: docs/issue-274.md
- 链接: https://github.com/dnakov/little-rat
- 描述: 一个 Chrome 插件，用来统计并关闭其他插件发出的 HTTP 请求，可以了解插件是否在偷偷上传数据。

---

### [第 274 期] Fooocus

- 来源: docs/issue-274.md
- 链接: https://github.com/lllyasviel/Fooocus
- 描述: 一个桌面应用，可以在离线条件下，通过文本生成图片。

---

### [第 274 期] try

- 来源: docs/issue-274.md
- 链接: https://github.com/binpash/try
- 描述: 一个 Linux 沙盒程序，让你在更改系统（比如安装程序或运行脚本）之前，先在沙盒中运行命令并检查效果。

---
### [第 275 期] oxc

- 来源: docs/issue-275.md
- 链接: https://github.com/web-infra-dev/oxc/
- 描述: 一个 JavaScript 工具包，包含了多个工具（解析器、代码压缩、格式美化、类型检查等），使用 Rust 语言开发，运行速度快。

---

### [第 275 期] TinaCMS

- 来源: docs/issue-275.md
- 链接: https://tina.io/
- 描述: 一个网站 CMS（内容管理系统），特别之处是它的内容不放在数据库，而是放在 Git 仓库，也可以用于 Git 仓库的网页编辑器。

---

### [第 275 期] Writerside

- 来源: docs/issue-275.md
- 链接: https://www.jetbrains.com/writerside/
- 描述: JetBrains 公司新推出的桌面软件，用来编写代码文档，写出来的文档保存在 Git 仓库。

---

### [第 275 期] EuBackend

- 来源: docs/issue-275.md
- 链接: https://gitee.com/zhaoeryu/eu-backend
- 描述: 一套开源的 Java SpringBoot + Vue 网站开发平台，可以基于它的前端和后端开发网站。（[@zhaoeryu](https://github.com/ruanyf/weekly/issues/3579) 投稿）

---

### [第 275 期] EmuDeck

- 来源: docs/issue-275.md
- 链接: https://www.emudeck.com/
- 描述: Steam Deck 掌机的游戏模拟器工具，让你在这个掌机上模拟其他平台，玩那些平台的游戏，后面还会适配安卓、Windows。

---

### [第 275 期] Secretive

- 来源: docs/issue-275.md
- 链接: https://github.com/maxgoedjen/secretive
- 描述: Mac 电脑的 SSH 密钥管理工具，支持使用 Touch ID 或 Apple Watch 进行身份验证，通过后才能访问密钥。

---

### [第 275 期] tRPC

- 来源: docs/issue-275.md
- 链接: https://github.com/trpc-group/trpc
- 描述: 腾讯内部使用的一款程序远程通信框架，类似于谷歌的 gRPC，首期开源 Go 和 C++ 实现，参见[介绍文章](https://mp.weixin.qq.com/s/ODEBU6fSTZ0ixgnQxeamTg)。（[@ryantang1991](https://github.com/ruanyf/weekly/issues/3584) 投稿）

---

### [第 275 期] Atuin

- 来源: docs/issue-275.md
- 链接: https://atuin.sh/
- 描述: 命令行工具，将 Shell 操作历史写入 SQLite 数据库，方便统计和复用。

---

### [第 275 期] pear-rec

- 来源: docs/issue-275.md
- 链接: https://github.com/027xiguapi/pear-rec/
- 描述: 一个开源的 Electron 应用，可以截图、录屏、录音等。（[@027xiguapi](https://github.com/ruanyf/weekly/issues/3587) 投稿）

---

### [第 275 期] TwitterShots

- 来源: docs/issue-275.md
- 链接: https://twittershots.com/
- 描述: 一个网页工具，生成推文的截图。（[@0xinhua](https://github.com/ruanyf/weekly/issues/3588) 投稿）

---
### [第 276 期] Alexandria

- 来源: docs/issue-276.md
- 链接: https://github.com/btpf/Alexandria
- 描述: 一个开源的 Windows/Linux 的桌面软件，用来阅读各种电子书籍。

---

### [第 276 期] YouTube Dubbing

- 来源: docs/issue-276.md
- 链接: https://www.youtube-dubbing.com/
- 描述: 一个 Chrome 插件，可以将 YouTube 视频的英文语音，转成中文语音。（[@dyc87112](https://github.com/ruanyf/weekly/issues/3592) 投稿）

---

### [第 276 期] pyvideotrans

- 来源: docs/issue-276.md
- 链接: https://github.com/jianchang512/pyvideotrans
- 描述: 一个 Windows 应用，跟上一个软件作用相似，可以将本地视频文件的语音，翻译成另一种语言，比如英文旁白改成机器语音合成的中文。 该工具只用了 CPU，没有用到 GPU，也没有用到任何商业接口，无需付费。（[@jianchang512](https://github.com/ruanyf/weekly/issues/3600) 投稿）

---

### [第 276 期] tailspin

- 来源: docs/issue-276.md
- 链接: https://github.com/bensadeh/tailspin
- 描述: 一个命令行工具，实时高亮显示日志文件。

---

### [第 276 期] WO Mic

- 来源: docs/issue-276.md
- 链接: https://wolicheng.com/womic/index.html
- 描述: 这个 App 可以将旧手机变成麦克风，把音频信号传入电脑或其他设备，无线、USB 线传输皆可。（[@GXY2017](https://github.com/ruanyf/weekly/issues/3602) 投稿）

---

### [第 276 期] Olive

- 来源: docs/issue-276.md
- 链接: https://olivevideoeditor.org/
- 描述: 一个跨平台的视频编辑器，据说简单好用，适合快速编辑生成短视频。类似的视频编辑器还有 [Shotcut](https://shotcut.org/)、[Pitivi](https://pitivi.org/)，主要适合 Linux 平台。

---

### [第 276 期] tldraw

- 来源: docs/issue-276.md
- 链接: https://www.tldraw.com/
- 描述: 一个 Web 白板工具，支持多人实时协作。

---

### [第 276 期] Rspack

- 来源: docs/issue-276.md
- 链接: https://www.rspack.dev/zh/
- 描述: 一个 Rust 语言写的 JS 脚本打包器，速度很快，支持从 Webpack 移植。（[@hardfist](https://github.com/ruanyf/weekly/issues/3596) 投稿）

---

### [第 276 期] Fantastic-admin

- 来源: docs/issue-276.md
- 链接: https://github.com/fantastic-admin/basic
- 描述: 一款开箱即用的 Vue3 中后台管理系统框架。（[@hooray](https://github.com/ruanyf/weekly/issues/3595) 投稿）

---

### [第 276 期] ScratchCard

- 来源: docs/issue-276.md
- 链接: https://github.com/1587315093/scratch-card
- 描述: 一个刮刮卡的 React 组件。（[@1587315093](https://github.com/1587315093/scratch-card) 投稿）

---
### [第 277 期] SSHFS

- 来源: docs/issue-277.md
- 链接: https://github.com/deadbeefsociety/sshfs
- 描述: 这个工具使用 SSH 协议，将远程服务器挂载成本地目录。

---

### [第 277 期] inshellisense

- 来源: docs/issue-277.md
- 链接: https://github.com/microsoft/inshellisense
- 描述: 微软推出的命令行自动补全工具。

---

### [第 277 期] KDesign

- 来源: docs/issue-277.md
- 链接: https://kingdee.design/
- 描述: 金蝶的企业级产品设计系统，包括设计规范、设计资源、前端组件库。（[@quanzhiyuan](https://github.com/ruanyf/weekly/issues/3606) 投稿）

---

### [第 277 期] react-exercise-playground

- 来源: docs/issue-277.md
- 链接: https://github.com/fewismuch/react-playground
- 描述: 一个开源的 React 练习场（playground）。（[@fewismuch](https://github.com/ruanyf/weekly/issues/3609) 投稿）

---

### [第 277 期] ChatGPT 中文网页版

- 来源: docs/issue-277.md
- 链接: https://github.com/Yidadaa/ChatGPT-Next-Web
- 描述: 一个开源的 ChatGPT 中文网页版，做得非常精致，可以自己部署。这里是 [Demo](https://chatgpt.gitapp.cn/)。（[@geeeeeeeek](https://github.com/ruanyf/weekly/issues/3611) 投稿）

---

### [第 277 期] Caravaggio

- 来源: docs/issue-277.md
- 链接: https://caravaggio.ramielcreations.com/
- 描述: 一个图像处理服务器，可以根据 URL 参数将原图转换成不同大小、格式等，适合用作图像 CDN 的源服务器。

---

### [第 277 期] Soul

- 来源: docs/issue-277.md
- 链接: https://github.com/thevahidal/soul
- 描述: 一个 JS 库，可以为 SQLite 数据库添加 HTTP 服务，自动提供 RESTful 接口。

---

### [第 277 期] Aegis

- 来源: docs/issue-277.md
- 链接: https://getaegis.app/
- 描述: 一个开源的安卓双因素认证的密码管理器。它的最大特点是可以导入导出数据，其他密码管理器好像都没有这个功能。

---

### [第 277 期] LazyVim

- 来源: docs/issue-277.md
- 链接: https://www.lazyvim.org/
- 描述: neovim 的一套配置文件，让其快速变成一个 IDE。

---

### [第 277 期] Glance

- 来源: docs/issue-277.md
- 链接: https://github.com/novoselrok/glance
- 描述: 一个很有意思的工具，使用 AI 找出代码最重要的部分，高亮显示。

---
### [第 278 期] ShortbreadAI

- 来源: docs/issue-278.md
- 链接: https://shortbread.ai/
- 描述: 这个网站让你方便地生成漫画。

---

### [第 278 期] ripsecrets

- 来源: docs/issue-278.md
- 链接: https://github.com/sirwart/ripsecrets
- 描述: 这个工具用于检查代码仓库，有没有泄漏密钥。它可以配置在 CI/CD 流程里面自动运行。

---

### [第 278 期] EmojiGen

- 来源: docs/issue-278.md
- 链接: https://emoji.fly.dev/
- 描述: 根据文字提示生成 Emoji 图案。

---

### [第 278 期] screenshot-to-code

- 来源: docs/issue-278.md
- 链接: https://github.com/abi/screenshot-to-code
- 描述: 一个开源的 Web 应用，用户上传一张网页截图，它会通过 OpenAI，给出该网页的 HTML/Tailwind/JS 代码实现。

---

### [第 278 期] PageSpyWeb

- 来源: docs/issue-278.md
- 链接: https://github.com/HuolalaTech/page-spy-web
- 描述: 一个开源的远程调试工具，提供类似浏览器控制台的界面，进行远程调试。（[@wqcstrong](https://github.com/ruanyf/weekly/issues/3616) 投稿）

---

### [第 278 期] IPS

- 来源: docs/issue-278.md
- 链接: https://github.com/sjzar/ips
- 描述: 一个命令行工具， 查询和处理 IP 地理位置数据库。（[@sjzar](https://github.com/ruanyf/weekly/issues/3631) 投稿）

---

### [第 278 期] GWS

- 来源: docs/issue-278.md
- 链接: https://github.com/lxzan/gws
- 描述: 一个开源的高性能 WebSocket 实现，包括服务器和客户端，用 Go 语言编写。（[@lxzan](https://github.com/ruanyf/weekly/issues/3623) 投稿）

---

### [第 278 期] ChatGot

- 来源: docs/issue-278.md
- 链接: https://start.chatgot.io/login
- 描述: 在一个窗口内，同时跟多个模型互动，可以让 GPT 输出文字，然后用 @midjourney 生成图片。（[@qinleilxl](https://github.com/ruanyf/weekly/issues/3624) 投稿）

---

### [第 278 期] 网页 AI 评审

- 来源: docs/issue-278.md
- 链接: https://uxaudit.vercel.app/
- 描述: 这个 Web 工具对用户提供的网址，进行 AI 评审，给出页面的设计问题和改进建议。 它是免费的，但是用户多的时候，会停止服务。如果 AI 表现好，以后设计稿评审和代码评审都可以交给它了。

---

### [第 278 期] AITDK

- 来源: docs/issue-278.md
- 链接: https://aitdk.com/zh-CN/
- 描述: 用户输入文章的主题，该网页工具会自动生成 SEO 友好的标题、描述、关键词和常见问题解答。（[@typewe](https://github.com/ruanyf/weekly/issues/3614) 投稿）

---
### [第 279 期] vectorious

- 来源: docs/issue-279.md
- 链接: https://github.com/mateogianolio/vectorious
- 描述: 一个用于矩阵计算的 JS 库。

---

### [第 279 期] EpubPress

- 来源: docs/issue-279.md
- 链接: https://github.com/sunxen/EpubPressX
- 描述: Chrome 浏览器插件，可以将打开的多个网页制作成一本 epub 电子书。（[@sunxen](https://github.com/ruanyf/weekly/issues/3642) 投稿）

---

### [第 279 期] CV 声音克隆工具

- 来源: docs/issue-279.md
- 链接: https://github.com/jianchang512/clone-voice
- 描述: 该开源工具可以提取人类音色，将一段文字或另一个语音转成该音色的语音，相当于克隆了他人的声音。 支持中文、英文、日语、韩语4种语言，可在线从麦克风录制声音。（[@jianchang512](https://github.com/ruanyf/weekly/issues/3652) 投稿）

---

### [第 279 期] Elog

- 来源: docs/issue-279.md
- 链接: https://github.com/LetTTGACO/elog
- 描述: 该工具可以将写作平台（语雀/飞书/Notion/FlowUs）的内容，发布到博客平台（Hexo/Vitepress/Confluence/WordPress）等。（[@LetTTGACO](https://github.com/ruanyf/weekly/issues/3644) 投稿）

---

### [第 279 期] ConfigCenterComparer

- 来源: docs/issue-279.md
- 链接: https://github.com/hxz393/ConfigCenterComparer
- 描述: 一款配置中心对比工具，可以比较不同配置中心的配置数据，只支持 Windows 平台。（[@hxz393](https://github.com/ruanyf/weekly/issues/3645) 投稿）

---

### [第 279 期] GPTs URL

- 来源: docs/issue-279.md
- 链接: https://github.com/CH563/gtps-url
- 描述: 一个开源的 Web 应用，用来搭建网络资源的分类网站，基于 Astro 框架，参见 [Demo](https://www.gptsurl.com/)。（[@CH563](https://github.com/ruanyf/weekly/issues/3646) 投稿）

---

### [第 279 期] PPz's chrome filter

- 来源: docs/issue-279.md
- 链接: https://github.com/ppz-pro/chrome-filter
- 描述: 一个极简的 Chrome 插件，让页面变为暗模式，只有11行 JS，可以用作入门示例。（[@daGaiGuanYu](https://github.com/ruanyf/weekly/issues/3654) 投稿）

---
### [第 280 期] Biome

- 来源: docs/issue-280.md
- 链接: https://biomejs.dev/
- 描述: JS 语言格式化工具 Prettier，提出谁能用 Rust 语言重新实现它，并通过所有测试用例，就能获得2万美元，因为它们自己没有资源做这件事。 结果，只过了两个星期，Biome 就[赢得了这场比赛](https://prettier.io/blog/2023/11/27/20k-bounty-was-claimed.html)。 Biome 是一个 JS 工具箱，零配置就能实现 JS 脚本的格式化和 Lint，性能出众。

---

### [第 280 期] IP Guide

- 来源: docs/issue-280.md
- 链接: https://ip.guide/
- 描述: 该网站提供免费 API，查询 IP 的地理位置。

---

### [第 280 期] Chrome-macOS-Screen-Saver-Tab

- 来源: docs/issue-280.md
- 链接: https://github.com/jason5ng32/macOS-Screen-Saver-as-Chrome-New-Tab
- 描述: Chrome/Edge 浏览器插件，让空白标签页显示 macOS 的 4K 航拍屏保视频，就像真屏保一样。（[@Y024](https://github.com/ruanyf/weekly/issues) 投稿）

---

### [第 280 期] streamlit-shadcn-ui

- 来源: docs/issue-280.md
- 链接: https://github.com/ObservedObserver/streamlit-shadcn-ui
- 描述: Python 的 Web 框架 streamlit 的一个组件库。（[@ObservedObserver](https://github.com/ruanyf/weekly/issues/3668) 投稿）

---

### [第 280 期] miniPaint

- 来源: docs/issue-280.md
- 链接: https://zaixianps.net/
- 描述: 一个中文版在线绘图工具，基于英文的[原始开源项目](https://github.com/viliusle/miniPaint)进行中文化。（[@geeeeeeeek](https://github.com/ruanyf/weekly/issues/3665) 投稿）

---

### [第 280 期] Rsbuild

- 来源: docs/issue-280.md
- 链接: https://github.com/web-infra-dev/rsbuild
- 描述: 一个 Web 构建工具，可以取代 Webpack，减少 90% 的配置并获得 10 倍的构建速度。（[@chenjiahan](https://github.com/ruanyf/weekly/issues/3662) 投稿）

---

### [第 280 期] Chatfairy

- 来源: docs/issue-280.md
- 链接: https://github.com/yuxiaoy1/chatfairy
- 描述: 一个极简的 Python 脚本，只用115行，实现一个网页聊天室，使用 SSE 进行后端消息推送，对 Python 全栈开发感兴趣的朋友可以参考。（[@yuxiaoy1](https://github.com/ruanyf/weekly/issues/3659) 投稿）

---

### [第 280 期] Gmeek

- 来源: docs/issue-280.md
- 链接: https://github.com/Meekdai/Gmeek
- 描述: 超轻量级个人博客模板，将 GitHub 的 issue 转成博客网站。（[@Meekdai](https://github.com/ruanyf/weekly/issues/3669) 投稿）

---

### [第 280 期] TQUIC

- 来源: docs/issue-280.md
- 链接: https://github.com/Tencent/tquic
- 描述: 腾讯对 QUIC 协议的实现，新开源的 QUIC 库，参考[介绍文章](https://mp.weixin.qq.com/s/9wgVtK7wBeEHIAaguOydJA)。（[@ryantang1991](https://github.com/ruanyf/weekly/issues/3671) 投稿）

---

### [第 280 期] ai-teacher

- 来源: docs/issue-280.md
- 链接: https://github.com/guojingwen/ai-teacher
- 描述: 一个 ChatGPT 的前端开发示例，可以当作代码参考。（[@guojingwen](https://github.com/ruanyf/weekly/issues/3667) 投稿）

---

### [第 280 期] DevOpsGPT

- 来源: docs/issue-280.md
- 链接: https://github.com/kuafuai/DevOpsGPT
- 描述: 一个 LLM 应用，根据需求生成开发文档，然后生成软件代码。（[@qinwanglsm](https://github.com/ruanyf/weekly/issues/3664) 投稿）

---
### [第 281 期] Cloudscape

- 来源: docs/issue-281.md
- 链接: https://cloudscape.design/
- 描述: 一个 React 组件库，专为云产品设计的。

---

### [第 281 期] TinyLD

- 来源: docs/issue-281.md
- 链接: https://github.com/komodojp/tinyld
- 描述: 一个 JS 库，用来判断一段文字是什么语言（汉语、英语、日语等等）。

---

### [第 281 期] VineJS

- 来源: docs/issue-281.md
- 链接: https://github.com/vinejs/vine
- 描述: 一个 Node.js 的表单验证库，只用于后端，支持大量验证规则，验证速度快。

---

### [第 281 期] AI Image Captions

- 来源: docs/issue-281.md
- 链接: https://felix.link/apps/captions
- 描述: 一个在线工具，可以为图片生成介绍词，用于社交媒体，可以指定语言、风格和长度。

---

### [第 281 期] Python Online Compiler

- 来源: docs/issue-281.md
- 链接: https://pythononlinecompiler.com/
- 描述: 一个在网页运行 Python 代码、显示运行结果的编译器，可以指定 Python 版本。

---

### [第 281 期] IP 工具箱

- 来源: docs/issue-281.md
- 链接: https://github.com/jason5ng32/MyIP/blob/main/README_CN.md
- 描述: 一个开源的本地网站，集成了 IP 相关的各种查询。（[@wangyanan19](https://github.com/ruanyf/weekly/issues/3691) 投稿）

---

### [第 281 期] GoMusic

- 来源: docs/issue-281.md
- 链接: https://github.com/Bistutu/GoMusic
- 描述: 音乐迁移助手，将网易云音乐、QQ 音乐的歌单，迁移至 Apple/Youtube/Spotify Music。（[@Bistutu](https://github.com/ruanyf/weekly/issues/3700) 投稿）

---

### [第 281 期] 33 字幕

- 来源: docs/issue-281.md
- 链接: https://www.33subs.com/
- 描述: 一个 Win/Mac 桌面软件，用于识别/制作音频和视频文件的双语字幕。（[@YeDaxia](https://github.com/ruanyf/weekly/issues/3693) 投稿）

---

### [第 281 期] Ai Cute Wallpapers

- 来源: docs/issue-281.md
- 链接: https://aicutewallpapers.com/
- 描述: 免费生成/下载 AI 壁纸。（[@huhan-123](https://github.com/ruanyf/weekly/issues/3686) 投稿）

---

### [第 281 期] vue-draggable-plus

- 来源: docs/issue-281.md
- 链接: https://github.com/Alfred-Skyblue/vue-draggable-plus
- 描述: Vue2 & Vue3 的拖拽组件。（[@Alfred-Skyblue](https://github.com/ruanyf/weekly/issues/3703) 投稿）

---
### [第 282 期] Imagine

- 来源: docs/issue-282.md
- 链接: https://imagine.meta.com/
- 描述: Meta 公司推出的文生图工具，使用 Facebook 和 Instagram 的11亿张图片训练，现在可以免费使用。

---

### [第 282 期] NotebookLM

- 来源: docs/issue-282.md
- 链接: https://notebooklm.google.com/
- 描述: 谷歌发布的 AI 笔记工具，用户上传文档，然后可以对文档提问，并且自动生成笔记，目前对美国用户免费开放。参见[谷歌的介绍文章](https://blog.google/technology/ai/notebooklm-new-features-availability/)。 不过，它好像只支持上传英文的 PDF 文件。

---

### [第 282 期] Scalar API Reference

- 来源: docs/issue-282.md
- 链接: https://github.com/scalar/scalar
- 描述: 一个开源工具，将 Swagger/OpenAPI 文件转成互动式 API 文档。

---

### [第 282 期] RoomGPT

- 来源: docs/issue-282.md
- 链接: https://github.com/Nutlope/roomGPT
- 描述: 一个开源软件，你上传一张房间照片，它使用 AI 重新设计你的房间。

---

### [第 282 期] Comments

- 来源: docs/issue-282.md
- 链接: https://github.com/DongHY1/comments
- 描述: 一个开源的网页评论系统，类似于 Vercel Comment，可以对页面的各个部分拉框评论。它采用 GitHub 的身份认证，数据放在 supabase。（[@DongHY1](https://github.com/ruanyf/weekly/issues/3743) 投稿）

---

### [第 282 期] GPT Assistant

- 来源: docs/issue-282.md
- 链接: https://github.com/ruanyf/weekly/issues/3725
- 描述: 网友写的开源 GPT 安卓客户端，可以跟 AI 语音聊天，还可以发送图片到 GPT-4V，并基于安卓 WebView，让 GPT 访问任何网站。（[@Skythinker616](https://github.com/ruanyf/weekly/issues/3725) 投稿）

---

### [第 282 期] MD Video

- 来源: docs/issue-282.md
- 链接: https://www.wvovw.com/guide/what-is-wvovw.html
- 描述: 一个桌面软件，将 Markdown 文档转成一段短视频。（[@lqomg](https://github.com/ruanyf/weekly/issues/3736) 投稿）

---

### [第 282 期] CodeGeeX2

- 来源: docs/issue-282.md
- 链接: https://github.com/THUDM/CodeGeeX2
- 描述: AI 编程助手，支持 VS Code、 IntelliJ IDEA、PyCharm、GoLand、WebStorm 等 IDE 编辑器，参见[介绍文章](https://github.com/CatsAndMice/blog/issues/72)。（[@CatsAndMice](https://github.com/ruanyf/weekly/issues/3731) 投稿）

---

### [第 282 期] bproxy

- 来源: docs/issue-282.md
- 链接: https://github.com/zobor/bproxy
- 描述: 一款抓包代理工具，可以拦截 HTTP 请求，配置文件是一个 JS 脚本。（[@zobor 投稿](https://github.com/ruanyf/weekly/issues/3728)）

---

### [第 282 期] Trippy

- 来源: docs/issue-282.md
- 链接: https://trippy.cli.rs/
- 描述: 一个命令行工具，可以代替 traceroute 查看互联网通信的路径，分析网络状况。

---
### [第 283 期] snowmachine

- 来源: docs/issue-283.md
- 链接: https://github.com/sontek/snowmachine
- 描述: 一个 Python 脚本，可以在终端窗口显示下雪和圣诞树。

---

### [第 283 期] Photo to Anime

- 来源: docs/issue-283.md
- 链接: https://photo-to-anime.com/
- 描述: 这个网站可以将上传的图片动漫化，也可以通过文本生成动漫图片。（[@dongan-beta](https://github.com/ruanyf/weekly/issues/3746) 投稿）

---

### [第 283 期] CBox

- 来源: docs/issue-283.md
- 链接: https://github.com/jokimina/cbox-chrome-extension
- 描述: Chrome 浏览器插件，通过快捷键唤起一个弹窗，执行各种操作（搜索、浏览历史、跳转标签）。（[@jokimina](https://github.com/ruanyf/weekly/issues/3753) 投稿）

---

### [第 283 期] DartBook

- 来源: docs/issue-283.md
- 链接: https://github.com/lindeer/dartbook
- 描述: 作者重新实现的 GitBook，加快了 Markdown 的解析速度，并新增了一些功能。（[@lindeer](https://github.com/ruanyf/weekly/issues/3763) 投稿）

---

### [第 283 期] pastebin-worker

- 来源: docs/issue-283.md
- 链接: https://github.com/xiadd/pastebin-worker
- 描述: 一个基于 Cloudflare Worker 实现的文字/代码分享网站，类似于 Pastebin。（[@xiadd](https://github.com/ruanyf/weekly/issues/3771) 投稿）

---

### [第 283 期] EasyTranslator

- 来源: docs/issue-283.md
- 链接: https://github.com/artwalker/EasyTranslator
- 描述: 一个命令行的文件翻译工具，可以翻译.txt、.pdf、.docx、.md、.mobi、.epub 文件，需要 OpenAI key。（[@artwalker](https://github.com/ruanyf/weekly/issues/3760) 投稿）

---

### [第 283 期] V2EX Polish

- 来源: docs/issue-283.md
- 链接: https://v2p.app/
- 描述: 一款浏览器插件，用来增强 V2ex 论坛的功能。（[@Codennnn](https://github.com/ruanyf/weekly/issues/3762) 投稿）

---
### [第 284 期] Score In URL

- 来源: docs/issue-284.md
- 链接: https://powersnail.com/ScoreInUrl/
- 描述: 一个在线编辑和分享乐谱的网站，乐谱保存在 URL 之中。

---

### [第 284 期] Teamlinker

- 来源: docs/issue-284.md
- 链接: https://github.com/Teamlinker/Teamlinker/blob/main/README-ZH-CN.md
- 描述: 一个开源的团队协作平台，包含项目、Wiki、日历、会议、聊天和网盘等功能。（[@xbdsky](https://github.com/ruanyf/weekly/issues/3780) 投稿）

---

### [第 284 期] Rspress

- 来源: docs/issue-284.md
- 链接: https://rspress.dev/zh/
- 描述: 基于 Rspack 的静态站点生成器，内置了 Rust 工具链，性能优秀，上手简单。（[@sanyuan0704](https://github.com/ruanyf/weekly/issues/3792) 投稿）

---

### [第 284 期] AudioCut

- 来源: docs/issue-284.md
- 链接: https://audiocut.app/
- 描述: 一个 Web 工具，可以自动剪辑音频文件，去除噪音和重复内容，删除选中的单词和句子，适合编辑播客。（[@tangpanqing](https://github.com/ruanyf/weekly/issues/3794) 投稿）

---

### [第 284 期] Tianji

- 来源: docs/issue-284.md
- 链接: https://github.com/msgbyte/tianji
- 描述: 一个开源工具，网站流量分析 + 业务监控告警 + 服务器监控三合一，三种服务做在了一起。（[@moonrailgun](https://github.com/ruanyf/weekly/issues/3795) 投稿）

---

### [第 284 期] Memo Card

- 来源: docs/issue-284.md
- 链接: https://memocard.net/
- 描述: 一个 Web 工具，用来生成文字分享的卡片图。（[@ivone-liu](https://github.com/ruanyf/weekly/issues/3803) 投稿）

---

### [第 284 期] vocal-separate

- 来源: docs/issue-284.md
- 链接: https://github.com/ruanyf/weekly/issues/3806
- 描述: 一款极简的人声和背景音乐分离工具，将音视频文件分离为单独的人声文件和伴奏文件，完全本地化作业，无需连接外网。（[@jianchang512](https://github.com/ruanyf/weekly/issues/3806) 投稿）

---

### [第 284 期] DouyinLiveRecorder

- 来源: docs/issue-284.md
- 链接: https://github.com/ihmily/DouyinLiveRecorder
- 描述: 一款免费的直播录制工具，支持录制抖音、Tiktok、快手、虎牙、斗鱼、B站、小红书等多平台的直播视频。（[@ihmily](https://github.com/ruanyf/weekly/issues/3809) 投稿）

---

### [第 284 期] Drawing Prompt

- 来源: docs/issue-284.md
- 链接: https://drawing-prompt.com/en
- 描述: 一个文生图的辅助工具，可以自动扩展提示语，将简短的提示（非英语也可以）变成详尽丰富的英语提示，免费且无需登录。还支持生成随机的提示词 tag 组合，并内嵌 Fast SDXL 模型，用于预览效果。（[@dongan-beta](https://github.com/ruanyf/weekly/issues/3810) 投稿）

---

### [第 284 期] cloudflare-ai-web

- 来源: docs/issue-284.md
- 链接: https://github.com/Jazee6/cloudflare-ai-web
- 描述: 通过免费的 Cloudflare Worker，搭建一个你自己的 AI 平台，支持切换多个 AI 模型，试用 [Demo](https://ai.jaze.top/)。（[@Jazee6](https://github.com/ruanyf/weekly/issues/3812) 投稿）

---

### [第 284 期] Penumbra

- 来源: docs/issue-284.md
- 链接: https://github.com/nealmckee/penumbra
- 描述: 一种配色方案，有明暗两个主题。据说是通过数学计算得到的、最有利于感知的配色方案。

---
### [第 285 期] vx.dev

- 来源: docs/issue-285.md
- 链接: https://github.com/Yuyz0112/vx.dev
- 描述: Vercel 的 [v0.dev](https://v0.dev/) 可以通过输入需求，直接生成网站。这里是它的一个开源仿制品，通过逆向工程进行模仿，详见[介绍文章](https://step-saga-examples.pages.dev/v0-dev-reverse-engineer/)。([@Yuyz0112](https://github.com/ruanyf/weekly/issues/3813) 投稿)

---

### [第 285 期] Triangle Patterns

- 来源: docs/issue-285.md
- 链接: https://sinqi.tools/triangle
- 描述: 三角渐变图案的生成工具。（[@zerosoul](https://github.com/ruanyf/weekly/issues/3815) 投稿）

---

### [第 285 期] Copilot-GPT4-service

- 来源: docs/issue-285.md
- 链接: https://github.com/aaamoon/copilot-gpt4-service
- 描述: 作者发现 Github Copilot Chat 的底层是调用 ChatGPT 接口，因此做了这个工具。 它可以将 ChatGPT 请求转换为 Github Copilot Chat 的请求。只要拥有 Github Copilot 账号，就能无限制使用 ChatGPT 的 GPT-4 模型。（[@aaamoon](https://github.com/ruanyf/weekly/issues/3820) 投稿）

---

### [第 285 期] Bluestone Markdown

- 来源: docs/issue-285.md
- 链接: https://www.bluemd.me/
- 描述: （青石） 一个所见即所得的 Markdown 桌面编辑器，集成了 Mermaid 图形与 Katex 公式，支持明亮和暗黑风格。（[@1943time](https://github.com/ruanyf/weekly/issues/3821) 投稿）

---

### [第 285 期] resume-json-pdf

- 来源: docs/issue-285.md
- 链接: https://github.com/RylanBot/resume-json-pdf
- 描述: 通过 JSON 文件，在线生成 PDF 简历。（[@RylanBot](https://github.com/ruanyf/weekly/issues/3826) 投稿） 这里还有一个类似的工具 [Faultier-CV](https://github.com/i5heu/Faultier-CV)，通过 Markdown 格式编写简历，并能[实时预览](https://i5heu.github.io/Faultier-CV/dist/index.html)。

---

### [第 285 期] schedule-x

- 来源: docs/issue-285.md
- 链接: https://schedule-x.dev/demos/calendar
- 描述: 谷歌日历的[开源](https://github.com/schedule-x/schedule-x)模仿品。

---

### [第 285 期] fabritor

- 来源: docs/issue-285.md
- 链接: https://github.com/sleepy-zone/fabritor-web
- 描述: 一款基于 fabric.js 的创意图片编辑器，支持自己部署。（[@sleepy-zone](https://github.com/ruanyf/weekly/issues/3831) 投稿）

---

### [第 285 期] Nostalgist.js

- 来源: docs/issue-285.md
- 链接: https://github.com/arianrhodsandlot/nostalgist
- 描述: 一个在浏览器中运行怀旧游戏主机模拟器的 JavaScript 库，比如运行任天堂FC 模拟器、世嘉 MD 模拟器、街机模拟器等等。（[@arianrhodsandlot](https://github.com/ruanyf/weekly/issues/3830) 投稿）

---

### [第 285 期] stt

- 来源: docs/issue-285.md
- 链接: https://github.com/jianchang512/stt
- 描述: 离线运行的本地语音识别转文字工具，基于 fast-whisper 模型。（[@jianchang512](https://github.com/ruanyf/weekly/issues/3829) 投稿）

---

### [第 285 期] Vue TSX Admin

- 来源: docs/issue-285.md
- 链接: https://github.com/manyuemeiquqi/vue-tsx-admin
- 描述: 一款开源的后台管理系统的前端模版，基于 Vue3 + TSX。（[@manyuemeiquqi](https://github.com/ruanyf/weekly/issues/3833) 投稿）

---

### [第 285 期] HTTPS Certification generator

- 来源: docs/issue-285.md
- 链接: https://selfcertificationhub.github.io/selfcertificationhub/generate
- 描述: 这个在线工具可以一键生成 IP 地址的自签名 HTTPS 证书，适合用于开发环境。（[@selfcertificationhub](https://github.com/ruanyf/weekly/issues/3839) 投稿）

---

### [第 285 期] cmd-wrapped

- 来源: docs/issue-285.md
- 链接: https://github.com/YiNNx/cmd-wrapped
- 描述: 这个工具可以读取你的命令行操作的历史记录，生成一份年度总结。支持 Zsh 和 Bash，并可指定年份。（[@YiNNx](https://github.com/ruanyf/weekly/issues/3840) 投稿）

---

### [第 285 期] mainonly

- 来源: docs/issue-285.md
- 链接: https://github.com/jerrylususu/mainonly
- 描述: 一个浏览器 Bookmarklet（书签工具），用户选中一个页面元素，它可以隐藏其他元素，适合用来专注阅读。（[@jerrylususu](https://github.com/ruanyf/weekly/issues/3845) 投稿）

---
### [第 286 期] VisActor

- 来源: docs/issue-286.md
- 链接: https://visactor.io/
- 描述: 一个字节出品的前端数据可视化解决方案，分成图表库 [VChart](https://visactor.io/vchart) 和表格库 [VTable](https://visactor.io/vtable)。（[@airgeek](https://github.com/ruanyf/weekly/issues/3849) 投稿）

---

### [第 286 期] h5player for tampermonkey

- 来源: docs/issue-286.md
- 链接: https://github.com/xxxily/h5player
- 描述: 一个油猴脚本，为 H5 视频网站增强功能（多级播放速度、截图、画中画、调节亮度、饱和度、对比度等），支持各大主流视频网站。（[@xxxily](https://github.com/ruanyf/weekly/issues/3852) 投稿）

---

### [第 286 期] 照片修复小小助手

- 来源: docs/issue-286.md
- 链接: https://github.com/shifu-group/inpaint_wechat
- 描述: 一个开源的微信小程序，用来消除图片中指定的人和物，纯客户端实现，无服务端。（[@wangqmshf](https://github.com/ruanyf/weekly/issues/3853) 投稿）

---

### [第 286 期] Pacman 游戏复刻

- 来源: docs/issue-286.md
- 链接: https://github.com/mumuy/pacman
- 描述: 开源的吃豆人游戏网页版复刻，[试玩 Demo](https://passer-by.com/pacman/)。（[@mumuy](https://github.com/ruanyf/weekly/issues/3855) 投稿）

---

### [第 286 期] UShare

- 来源: docs/issue-286.md
- 链接: https://share.aitimi.cn/
- 描述: 一款生成代码和文本分享卡片的网页工具，可以设定字体和字型大小。（[@szmxx](https://github.com/ruanyf/weekly/issues/3856) 投稿）

---

### [第 286 期] mdcat

- 来源: docs/issue-286.md
- 链接: https://github.com/swsnr/mdcat
- 描述: 一个`cat`命令的替代品，可以在命令行显示 Markdown 文件渲染后的内容。（[@lengyijun](https://github.com/ruanyf/weekly/issues/3859) 投稿）

---

### [第 286 期] SuperCopy

- 来源: docs/issue-286.md
- 链接: https://github.com/ruanyf/weekly/issues/3862
- 描述: （超级复制） 一个浏览器插件，用来解除网页限制（比如禁用右键），然后复制网页内容。（[@WFANG12719](https://github.com/ruanyf/weekly/issues/3862) 投稿）

---

### [第 286 期] Vue DevTools Next

- 来源: docs/issue-286.md
- 链接: https://github.com/vuejs/devtools-next
- 描述: Vue 官方开发者工具的下一个迭代，旨在增强 Vue 开发者体验。（[@webfansplz](https://github.com/ruanyf/weekly/issues/3864) 投稿）

---

### [第 286 期] yft-design

- 来源: docs/issue-286.md
- 链接: https://yft.design/
- 描述: 基于 fabric.js 的名片编辑应用。（[@more-strive](https://github.com/ruanyf/weekly/issues/3865) 投稿）

---

### [第 286 期] ant-codeAI

- 来源: docs/issue-286.md
- 链接: https://github.com/sparrow-js/ant-codeAI/blob/main/README-zh_CN.md
- 描述: 通过 OpenAI、Gemini 等模型，生成 Web（React，Vue，Tailwind CSS）和 native（react native）代码。（[@sparrow-js](https://github.com/ruanyf/weekly/issues/3860) 投稿）

---

### [第 286 期] Read Copilot

- 来源: docs/issue-286.md
- 链接: https://apps.apple.com/us/app/read-copilot-beyond-summarizer/id6449242676
- 描述: 一个苹果设备的阅读器 App，支持 RSS 和 Read It Later 功能，并可以用 AI 生成总结、文章大纲和翻译。（[@dongsuo](https://github.com/ruanyf/weekly/issues/3868) 投稿）

---

### [第 286 期] 海豹 D2C

- 来源: docs/issue-286.md
- 链接: https://music.163.com/st/seal/
- 描述: 一款 Figma/MasterGo 的插件，将设计稿导出为 React、Vue、RN、微信小程序代码。（[@Kinasha](https://github.com/ruanyf/weekly/issues/3869) 投稿）

---

### [第 286 期] vscode-common-intellisense

- 来源: docs/issue-286.md
- 链接: https://github.com/Simon-He95/vscode-common-intellisense
- 描述: VS Code 插件，为主流的前端框架提供代码提示（intellisense）。（[@Simon-He95](https://github.com/ruanyf/weekly/issues/3873) 投稿）

---

### [第 286 期] Screenshot Beautifier

- 来源: docs/issue-286.md
- 链接: https://github.com/CH563/shot-easy-website
- 描述: 开源的页面截图美化工具，试用 Demo。（[@CH563](https://github.com/ruanyf/weekly/issues/3876) 投稿）

---

### [第 286 期] Apache Answer

- 来源: docs/issue-286.md
- 链接: https://answer.apache.org/
- 描述: 一款基于 Golang 和 ReactJS 的开源问答平台软件，帮你快速建立问答社区，也可用来搭建社区论坛、支持中心、知识库等。（[@PrimmaAnna](https://github.com/ruanyf/weekly/issues/3877) 投稿）

---

### [第 286 期] Yazi

- 来源: docs/issue-286.md
- 链接: https://github.com/sxyazi/yazi/
- 描述: 一款运行在终端里面的文件管理器，跨平台，支持图片预览，使用 Rust 语言开发，速度快。（[@lengyijun](https://github.com/ruanyf/weekly/issues/3879) 投稿）

---

### [第 286 期] AI 换脸

- 来源: docs/issue-286.md
- 链接: https://www.changeface.online/
- 描述: 上传图片和视频，可以对里面的人物进行换脸。（[@CNHarrySun](https://github.com/ruanyf/weekly/issues/3882) 投稿）

---
### [第 287 期] Amazing AI

- 来源: docs/issue-287.md
- 链接: https://apps.apple.com/us/app/amazing-ai/id1660147028
- 描述: 著名程序员 Sindre Sorhus 推出的一款 mac 和 iPhone App，能够在本地运行 Stable Diffusion 模型，完成文生图。

---

### [第 287 期] memory spy

- 来源: docs/issue-287.md
- 链接: https://memory-spy.wizardzines.com/
- 描述: 用户在这个网站上提交 C 程序，可以按行查看变量在内存的表示方式，比如整数、浮点数占用多少内存，详见[介绍文章](https://jvns.ca/blog/2023/05/25/new-playground--memory-spy/)。

---

### [第 287 期] Penrose

- 来源: docs/issue-287.md
- 链接: https://github.com/penrose/penrose
- 描述: 一个开源工具，可以根据文本指令，生成可视化图形，类似于 Mermaid 和 PlantUML，但是图形能力更强大。

---

### [第 287 期] IP-Adapter-FaceID AI

- 来源: docs/issue-287.md
- 链接: https://ipadapterfaceid.com/
- 描述: 很多科技媒体都报道了 [IP-Adapter-FaceID](https://huggingface.co/h94/IP-Adapter-FaceID) 这个模型，可以克隆照片人物的脸部，然后通过文生图，将克隆的脸用于生成的图片。作者感觉这个模型效果不错，做了这个网站接入了该模型。（[@MuYiBo](https://github.com/ruanyf/weekly/issues/3888) 投稿）

---

### [第 287 期] Gitblog

- 来源: docs/issue-287.md
- 链接: https://gitblog.io/
- 描述: 这个工具可以将 GitHub Issues 转成一个静态的博客网站，单个博客使用免费。（[@blackstorm](https://github.com/ruanyf/weekly/issues/3890) 投稿）

---

### [第 287 期] Kamera

- 来源: docs/issue-287.md
- 链接: https://github.com/besscroft/kamera
- 描述: 一个开源的照片展示网站，点击可以查看 EXIF 信息，支持 Docker 一键部署。（[@besscroft](https://github.com/ruanyf/weekly/issues/3892) 投稿）

---

### [第 287 期] weapp-tailwindcss

- 来源: docs/issue-287.md
- 链接: https://github.com/sonofmagic/weapp-tailwindcss
- 描述: 小程序使用 tailwindcss 的全面解决方案。（[@sonofmagic](https://github.com/ruanyf/weekly/issues/3889) 投稿）

---

### [第 287 期] ICONCE

- 来源: docs/issue-287.md
- 链接: https://iconce.com/
- 描述: SVG 图标编辑生成工具。（[@yesmore](https://github.com/ruanyf/weekly/issues/3895) 投稿）

---

### [第 287 期] STranslate

- 来源: docs/issue-287.md
- 链接: https://github.com/ruanyf/weekly/issues/3899
- 描述: Windows 桌面软件，支持文本翻译和离线 OCR。（[@ZGGSONG](https://github.com/ruanyf/weekly/issues/3899) 投稿）

---

### [第 287 期] SmartExcel.cc

- 来源: docs/issue-287.md
- 链接: https://github.com/weijunext/smart-excel-ai
- 描述: 一个开源的 SaaS [程序示例](https://www.smartexcel.cc/)，演示登录和支付功能的实现。（[@weijunext](https://github.com/ruanyf/weekly/issues/3887) 投稿）

---

### [第 287 期] vscode-eslint-disable

- 来源: docs/issue-287.md
- 链接: https://github.com/lvjiaxuan/vscode-eslint-disable
- 描述: VS Code 插件，当某行代码在 VS Code 里面显示不符合 ESlint 规则时，允许使用快捷键，将这个（或这些）规则禁止。（[@lvjiaxuan](https://github.com/ruanyf/weekly/issues/3883) 投稿）

---

### [第 287 期] FigureToCartoon

- 来源: docs/issue-287.md
- 链接: https://ai-cartoon-figure.club/home
- 描述: 一键将图片转换成日漫风、3D 风、手绘风等等。（[@handsometong](https://github.com/ruanyf/weekly/issues/3901) 投稿）

---

### [第 287 期] Gemini ChatUp

- 来源: docs/issue-287.md
- 链接: https://github.com/loo-y/GeminiChatUp
- 描述: 基于 Gemini Pro 和 Gemini Pro Vision API 的开源聊天应用。支持一键部署至 Vercel，需要 Gemini API Key。（[@loo-y](https://github.com/ruanyf/weekly/issues/3900) 投稿）

---

### [第 287 期] Imgae matting

- 来源: docs/issue-287.md
- 链接: https://github.com/ihmily/image-matting
- 描述: 基于开源模型的在线抠图，支持人像和物体抠图，可以 docker 运行 ，无需 GPU。（[@ihmily](https://github.com/ruanyf/weekly/issues) 投稿）

---

### [第 287 期] 优雅简历

- 来源: docs/issue-287.md
- 链接: https://www.elegantresume.pro/
- 描述: 免费的在线简历生成工具，集成 ChatGPT，可以让 AI 修改、定制简历。（[@WilliamLoveSoccer](https://github.com/ruanyf/weekly/issues/3907) 投稿）

---

### [第 287 期] GPUPixel

- 来源: docs/issue-287.md
- 链接: https://github.com/pixpark/gpupixel/blob/main/README_cn.md
- 描述: C++11 编写的图像和视频处理库，内置美颜滤镜，适合为直播提供美颜，目前支持 iOS、Mac、Android。（[@gezhaoyou](https://github.com/ruanyf/weekly/issues/3908) 投稿）

---

### [第 287 期] Gemini-OpenAI-Proxy

- 来源: docs/issue-287.md
- 链接: https://github.com/zuisong/gemini-openai-proxy
- 描述: 这个工具可以起一个服务，将 OpenAI 的 API 调用转为 Gemini Pro API 的 API 调用，从而可以使用现有的 ChatGPT 客户端，体验 Gemini Pro。（[@zuisong](https://github.com/ruanyf/weekly/issues/3910) 投稿）

---

### [第 287 期] Calendar Remark

- 来源: docs/issue-287.md
- 链接: https://github.com/xyxc0673/calendar-remark
- 描述: 这个工具可以标记日历，并生成分享图，适合说明私有的日程安排（比如公司活动），参见[介绍文章](https://xym.craft.me/qxAl6skGDFeVsR)和 [Demo](https://calendar.xym.im/)。（[@xyxc0673](https://github.com/ruanyf/weekly/issues/3911) 投稿）

---
### [第 288 期] Gemini Pro Chat

- 来源: docs/issue-288.md
- 链接: https://github.com/lchh5/GeminiPro-Next-Web
- 描述: 作者修改了 ChatGPT Next Web 的源码，使其可以用于 Gemini Pro，这里是 [demo](https://chat.googlegemini.co/)。（[@lchh5](https://github.com/ruanyf/weekly/issues/3923) 投稿）

---

### [第 288 期] WoodenFish

- 来源: docs/issue-288.md
- 链接: https://github.com/jwenjian/wooden-fish
- 描述: 一个敲木鱼的网页 App，移动端打开时，只有侦测到手机陀螺仪的角度变化，才算一次敲击动作，这时可以把手机想象成敲木鱼的棒子。（[@jwenjian](https://github.com/ruanyf/weekly/issues/3929) 投稿）

---

### [第 288 期] Moodist

- 来源: docs/issue-288.md
- 链接: https://github.com/geekyouth/moodist
- 描述: 一个开源的 Docker 镜像文件，提供50多种[背景声](https://moodist.java666.cn/)，比如风声、雨声、咖啡馆的声音。（[@geekyouth](https://github.com/ruanyf/weekly/issues/3943) 投稿）

---

### [第 288 期] Echo UI

- 来源: docs/issue-288.md
- 链接: https://echoui.dev/zh/
- 描述: 一款专为 Web Audio API 设计的 UI 库，适合用来搭建基于 Web 的音频应用。（[@codeacme17](https://github.com/ruanyf/weekly/issues/3946) 投稿）

---

### [第 288 期] Photor

- 来源: docs/issue-288.md
- 链接: https://www.photor.fun/
- 描述: 截图美化工具，可以在线使用，也可以通过浏览器插件使用。（[@sleepy-zone](https://github.com/ruanyf/weekly/issues/3948) 投稿）

---

### [第 288 期] Message Nest

- 来源: docs/issue-288.md
- 链接: https://github.com/engigu/Message-Push-Nest
- 描述: 开源的消息推送平台，整合邮件、钉钉、企业微信等多种通知方式。（[@engigu](https://github.com/ruanyf/weekly/issues/3947) 投稿）

---

### [第 288 期] Tiny RDM

- 来源: docs/issue-288.md
- 链接: https://redis.tinycraft.cc/zh/
- 描述: Redis 桌面管理客户端，支持 Mac、Windows、Linux。（[@tiny-craft](https://github.com/ruanyf/weekly/issues/3955) 投稿）

---

### [第 288 期] Frigate

- 来源: docs/issue-288.md
- 链接: https://github.com/blakeblackshear/frigate
- 描述: 开源的摄像头固件，具有实时目标物体侦测。

---

### [第 288 期] InstantID

- 来源: docs/issue-288.md
- 链接: https://github.com/InstantID/InstantID
- 描述: 只使用一张图片，就可以提取人脸，用于个性化图像合成，并支持各种不同的风格，试用 [Demo](https://instantid.org/#playground)。（[@zinc1234596](https://github.com/ruanyf/weekly/issues/3959) 投稿）

---

### [第 288 期] HandBrake

- 来源: docs/issue-288.md
- 链接: https://handbrake.fr/
- 描述: 一个跨平台的桌面应用，用于转换视频编码。

---

### [第 288 期] Animotion

- 来源: docs/issue-288.md
- 链接: https://cssanimotion.pages.dev/
- 描述: 一个网页 CSS 动画生成器，可视化设定动画，自动生成代码。

---

### [第 288 期] Ada

- 来源: docs/issue-288.md
- 链接: https://github.com/ada-url/ada
- 描述: 一个 URL 解析器，符合最新规范，使用 C++ 编写，可以快速处理 URL。

---

### [第 288 期] Inpaint-web

- 来源: docs/issue-288.md
- 链接: https://github.com/lxfater/inpaint-web
- 描述: 开源的图片修复和超分辨率工具, 纯浏览器端实现。（[@lxfater](https://github.com/ruanyf/weekly/issues/3964) 投稿）

---

### [第 288 期] 人像生成工具

- 来源: docs/issue-288.md
- 链接: https://sinqi.tools/zh/avatar
- 描述: 基于手绘风 SVG 人物画像集合 [Open Peeps](https://www.openpeeps.com/)，一个人物画像的在线定制工具。（[@zerosoul](https://github.com/ruanyf/weekly/issues/3968) 投稿）

---
### [第 289 期] Noi

- 来源: docs/issue-289.md
- 链接: https://github.com/lencx/Noi
- 描述: 跨平台的桌面应用，在一个界面里面集成了多个 AI 网站，支持复用提示，以及同时向多款 AI 提问。（[@lencx](https://github.com/ruanyf/weekly/issues/3976) 投稿）

---

### [第 289 期] xcp

- 来源: docs/issue-289.md
- 链接: https://github.com/tarka/xcp/
- 描述: 使用 rust 重写的 cp 命令，针对多核、大内存、固态磁盘、nfs 挂载目录等情况进行了优化。（[@lengyijun](https://github.com/ruanyf/weekly/issues/3972) 投稿） 同一作者还有一个相关项目 [Smartscp](https://github.com/lengyijun/smartscp)，用来替代同步命令 scp，但会排除 .gitignore 和 node_modules 目录。

---

### [第 289 期] xiaomusic

- 来源: docs/issue-289.md
- 链接: https://github.com/hanxi/xiaomusic
- 描述: 小爱音箱播放本地音乐的一个工具。（[@hanxi](https://github.com/ruanyf/weekly/issues/3980) 投稿）

---

### [第 289 期] UtilMeta

- 来源: docs/issue-289.md
- 链接: https://github.com/utilmeta/utilmeta-py
- 描述: 一个用于快速生成 RESTful API 的 Python 框架。（[@voidZXL](https://github.com/ruanyf/weekly/issues/3978) 投稿）

---

### [第 289 期] Home Infra

- 来源: docs/issue-289.md
- 链接: https://github.com/homeinfra-org/infra
- 描述: 一个 Docker 镜像，提供个人或小团队使用的 DevOps 实验环境。（[@NoCLin](https://github.com/ruanyf/weekly/issues/3977) 投稿）

---

### [第 289 期] AITDK

- 来源: docs/issue-289.md
- 链接: https://aitdk.com/zh-CN/extension/
- 描述: 一款浏览器插件，提供当前网站的流量/Whois/SEO 等信息。（[@typewe](https://github.com/ruanyf/weekly/issues/3990) 投稿）

---

### [第 289 期] 轻松传

- 来源: docs/issue-289.md
- 链接: https://easychuan.cn/
- 描述: 局域网内的文件互传工具，只需双方打开网页，基于 WebRTC 技术。（[@AndySpider](https://github.com/ruanyf/weekly/issues/3986) 投稿） 另有命令行程序 [croc](https://github.com/schollz/croc)，可在任意两台电脑之间传送文件。

---

### [第 289 期] AI 红包封面

- 来源: docs/issue-289.md
- 链接: https://github.com/all-in-aigc/aicover
- 描述: 输入提示词，一键生成精美的 AI 红包封面图，上传到微信红包封面开放平台，试用 [Demo](https://aicover.design)。（[@idoubi](https://github.com/ruanyf/weekly/issues/3991) 投稿）

---

### [第 289 期] Offine-Text-Translate

- 来源: docs/issue-289.md
- 链接: https://github.com/jianchang512/ott
- 描述: 本地离线翻译的 API 工具，不联网就可以翻译多种语言，基于 LibreTranslate 的封装，支持 Mac/Linux/Win。（[@jianchang512](https://github.com/ruanyf/weekly/issues/3992) 投稿）

---

### [第 289 期] Process Explorer

- 来源: docs/issue-289.md
- 链接: https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer
- 描述: 微软官方工具，可以查看 Windows 所有进程的详细信息，免费下载。

---

### [第 289 期] winlator

- 来源: docs/issue-289.md
- 链接: https://github.com/brunodev85/winlator
- 描述: 一个安卓 App，让安卓手机可以运行 Windows 应用程序。

---
### [第 290 期] Zed

- 来源: docs/issue-290.md
- 链接: https://zed.dev/
- 描述: 一个速度极快的代码编辑器，跨平台，来自 Atom 原团队的最新作品。 另外，Atom 项目关闭后，代码开源了。基于原始代码的新项目叫做 [Pulsar](https://optimizedbyotto.com/post/pulsar-best-text-file-and-code-editor/)，也是一个非常优秀的代码编辑器。

---

### [第 290 期] TCPView

- 来源: docs/issue-290.md
- 链接: https://learn.microsoft.com/en-us/sysinternals/downloads/tcpview
- 描述: 微软的官方工具，用来查看 Windows 系统所有 TCP 和 UDP 连接的详细信息。（[@meq1986](https://github.com/ruanyf/weekly/issues/4013) 投稿）

---

### [第 290 期] EasyDevo

- 来源: docs/issue-290.md
- 链接: https://easydevo.boringboring.design/
- 描述: Mac 桌面应用，用来清理系统的垃圾文件，以及监控系统指标（网络、CPU、RAM 和电池等），参见[介绍文章](https://medium.com/@hi_caicai/easydevo-the-developer-tool-you-might-need-a70dfd6ee3e1)。（[@hi-caicai](https://github.com/ruanyf/weekly/issues/4018) 投稿）

---

### [第 290 期] FontMagic

- 来源: docs/issue-290.md
- 链接: https://github.com/leibnizli/fontmagic
- 描述: 字体工具软件，可以将字体文件的某个字形导出为 SVG 格式，还可以转化字体格式，支持 macOS 和 Windows。（[@leibnizli](https://github.com/ruanyf/weekly/issues/4028) 投稿）

---

### [第 290 期] uv

- 来源: docs/issue-290.md
- 链接: https://astral.sh/blog/uv
- 描述: Rust 语言写的 Python 包管理器，速度非常快，可以替代 pip 和pip-tools。（[@qiaouchicago](https://github.com/ruanyf/weekly/issues/4030) 投稿）

---

### [第 290 期] Keep Screen On

- 来源: docs/issue-290.md
- 链接: https://www.keepscreenon.com/
- 描述: 打开这个网页，就可以让电脑屏幕保持常亮，对 PC、Mac、Android、iOS 均有效。（[@tufucheung](https://github.com/ruanyf/weekly/issues/4033) 投稿）

---

### [第 290 期] background-erase.xyz

- 来源: docs/issue-290.md
- 链接: https://background-erase.xyz/
- 描述: 去除图片背景的免费网站，使用最新的删除图片背景的 AI 模型 RMBG-v1.4，所有计算都在本地完成，不用上传图片。（[@janily](https://github.com/ruanyf/weekly/issues/4040) 投稿）

---

### [第 290 期] browserscan.net

- 来源: docs/issue-290.md
- 链接: https://www.browserscan.net/
- 描述: 该网站检测浏览器指纹、IP 地址、WebRTC 泄露，DNS 泄露等信息。（[@BrowserScan](https://github.com/ruanyf/weekly/issues/4045) 投稿）

---

### [第 290 期] NPMprune

- 来源: docs/issue-290.md
- 链接: https://github.com/xthezealot/npmprune
- 描述: 一个 Shell 脚本，删除 node_modules 目录里面各个模块的多余文件（比如 markdown 文件），有利于容器打包时减少体积。

---

### [第 290 期] Localtunnel

- 来源: docs/issue-290.md
- 链接: https://theboroer.github.io/localtunnel-www/
- 描述: 一个 npm 软件包，为你的本地服务分配一个公网的 URL，使得公网可以访问这个本地服务。

---

### [第 290 期] SirTunnel

- 来源: docs/issue-290.md
- 链接: https://github.com/anderspitman/SirTunnel
- 描述: 一个开源软件，只需要50行代码，就能建立一条隧道，将你的内网电脑可以被公网访问，这里有一篇[教程](https://eighty-twenty.org/2023/01/27/sirtunnel-personal-ngrok)。

---
### [第 291 期] Spacedrive

- 来源: docs/issue-291.md
- 链接: https://www.spacedrive.com/
- 描述: 一个跨桌面平台的文件管理器，将不同设备、云端的文件放在一个窗口里面管理。

---

### [第 291 期] LightMirrors

- 来源: docs/issue-291.md
- 链接: https://github.com/NoCLin/LightMirrors
- 描述: 一个开源的软件包缓存镜像站工具，用于在内网加速软件包下载和镜像拉取，目前支持 DockerHub、PyPI、PyTorch、NPM 等镜像缓存服务，需要自己架设。（[@NoCLin](https://github.com/ruanyf/weekly/issues/4059) 投稿）

---

### [第 291 期] 捕风记录仪

- 来源: docs/issue-291.md
- 链接: https://github.com/yuka-friends/Windrecorder
- 描述: （Windrecorder） 一款开源的 Windows 应用，自动在后台以小尺寸记录出现过的所有屏幕内容，并对文本或图像描述进行 OCR，以便查询。（[@Antonoko](https://github.com/ruanyf/weekly/issues/4067) 投稿）

---

### [第 291 期] ApFree WiFiDog

- 来源: docs/issue-291.md
- 链接: https://github.com/liudf0716/apfree-wifidog
- 描述: 路由器操作系统 OpenWRT 的一个模块，用来为自己架设的 WiFi 服务提供认证。（[@liudf0716](https://github.com/ruanyf/weekly/issues/4074) 投稿）

---

### [第 291 期] AI 图像音乐生成器

- 来源: docs/issue-291.md
- 链接: https://imagetomusic.top/
- 描述: 这个 Web 服务可以将上传的图像，转换为一段音乐，适合为图文视频配背景音乐。（[@lesliele](https://github.com/ruanyf/weekly/issues/4055) 投稿）

---

### [第 291 期] WeWe RSS

- 来源: docs/issue-291.md
- 链接: https://github.com/cooderl/wewe-rss
- 描述: 全文订阅微信公众号的一个本地服务，可以生成公众号的 RSS，基于微信读书。（[@cooderl](https://github.com/ruanyf/weekly/issues/4076) 投稿）

---

### [第 291 期] Marker

- 来源: docs/issue-291.md
- 链接: https://github.com/VikParuchuri/marker
- 描述: 一个命令行工具，将 PDF、EPUB、MOBI 文档转成 Markdown 文件，必要时会进行 OCR（文字识别）。

---

### [第 291 期] Omnivore

- 来源: docs/issue-291.md
- 链接: https://github.com/omnivore-app/omnivore
- 描述: 一个开源的“稍后阅读”（read-it-later）解决方案，可以收藏网址、RSS 和邮件列表的文章，提供 Web 和手机客户端。

---

### [第 291 期] Kysely

- 来源: docs/issue-291.md
- 链接: https://kysely.dev/
- 描述: 一个 TypeScript 的 SQL 查询生成库。

---

### [第 291 期] chasquid

- 来源: docs/issue-291.md
- 链接: https://blitiri.com.ar/p/chasquid/
- 描述: 一个简单的、主要供个人使用的 SMTP 软件，用来发送电子邮件。

---

### [第 291 期] TSDiagram

- 来源: docs/issue-291.md
- 链接: https://tsdiagram.com/
- 描述: 一个在线工具，让你用 TypeScript 写类型关系，自动生成图表。

---

### [第 291 期] How I get there

- 来源: docs/issue-291.md
- 链接: https://how-did-i-get-here.net/
- 描述: 这个页面可以显示，你的 IP 地址到该网站所经过的路由。

---
### [第 292 期] Ente

- 来源: docs/issue-292.md
- 链接: https://github.com/ente-io/ente
- 描述: 一个云相册软件，Google Photos 和 iCloud Photos 的替代品，以前是闭源产品，最近刚刚开源。 它的主要特点是提供端对端加密。其他的云相册软件，还有 [Immich](https://immich.app/) 和 [PhotoPrism](https://github.com/photoprism/photoprism)。

---

### [第 292 期] Earthly

- 来源: docs/issue-292.md
- 链接: https://earthly.dev/
- 描述: 一个开源的 CI/CD 框架，可以在本地架设自动构建服务。

---

### [第 292 期] Vikunja

- 来源: docs/issue-292.md
- 链接: https://vikunja.io/
- 描述: 一个开源的代办事项（to-do）App，提供多种视图，有 Web 版和桌面版，还可以自己架设。

---

### [第 292 期] 日语短文排版小工具

- 来源: docs/issue-292.md
- 链接: https://miusuncle.github.io/japen/
- 描述: 一个在线工具，生成漂亮的日文排版，支持横竖版式、自动假名标注、深浅两种主题、字体配置、高亮、下划线、字体等。（[@miusuncle](https://github.com/ruanyf/weekly/issues/4080) 投稿）

---

### [第 292 期] Web-Check

- 来源: docs/issue-292.md
- 链接: https://github.com/Lissy93/web-check
- 描述: 开源的网站分析工具, 可以分析网站的 IP 信息、SSL 链、DNS 记录、Cookie、域名信息、服务器位置、网站性能等，查看 [Demo](https://web-check.xyz/)。（[@WFANG12719](https://github.com/ruanyf/weekly/issues/4086) 投稿）

---

### [第 292 期] ImageTools

- 来源: docs/issue-292.md
- 链接: https://ai-image.tools/home
- 描述: AI 一键抠图（去除背景）的在线工具。（[@handsometong](https://github.com/ruanyf/weekly/issues/4087) 投稿）

---

### [第 292 期] zz-plan

- 来源: docs/issue-292.md
- 链接: https://zz-plan.com/
- 描述: 甘特图/横道图的在线制作工具。（[@lizhichao](https://github.com/ruanyf/weekly/issues/4088) 投稿）

---

### [第 292 期] Windows in container

- 来源: docs/issue-292.md
- 链接: https://github.com/dockur/windows
- 描述: Docker 容器里运行 Windows 系统，可选择 Win7，Win10，Win11 等，支持自动激活，还支持远程桌面连接。（[@wrenashe](https://github.com/ruanyf/weekly/issues/4091) 投稿）

---

### [第 292 期] Rsdoctor

- 来源: docs/issue-292.md
- 链接: https://github.com/web-infra-dev/rsdoctor
- 描述: 一个 JS 构建器的分析工具，能够查看构建产物的模块关系，并分析构建器对代码的更改，支持 Rspack 和 Webpack。（[@easy1090](https://github.com/ruanyf/weekly/issues/4095) 投稿）

---

### [第 292 期] Photo Relay

- 来源: docs/issue-292.md
- 链接: https://github.com/zobor/photo-relay
- 描述: 一个封面图片制作的在线工具。 [Demo](https://www.duelpeak.com/pages/poster)。（[@zobor](https://github.com/ruanyf/weekly/issues/4094) 投稿）

---

### [第 292 期] opfs-tools

- 来源: docs/issue-292.md
- 链接: https://github.com/hughfenghen/opfs-tools
- 描述: 浏览器私有文件系统 OPFS API 的一个封装库，提供更简单好用的 API。（[@hughfenghen](https://github.com/ruanyf/weekly/issues/4099) 投稿）

---

### [第 292 期] ast-grep VSCode

- 来源: docs/issue-292.md
- 链接: https://marketplace.visualstudio.com/items?itemName=ast-grep.ast-grep-vscode
- 描述: 一个使用正则表达式进行代码搜索、替换的 VSCode 插件。（[@HerringtonDarkholme](https://github.com/ruanyf/weekly/issues/4100) 投稿）

---
### [第 293 期] Rot

- 来源: docs/issue-293.md
- 链接: https://github.com/candiddev/rot
- 描述: 一个命令行工具，用来对密码进行加密/解密，这样就可以把密码保存在公开的代码库了。

---

### [第 293 期] Angie

- 来源: docs/issue-293.md
- 链接: https://angie.software/en/
- 描述: 一个 nginx 的分叉版本，由原始团队成员开发，增加了一些功能。类似的项目还有 [free nginx](https://freenginx.org/)。

---

### [第 293 期] LaVague

- 来源: docs/issue-293.md
- 链接: https://github.com/lavague-ai/LaVague
- 描述: 一个很有意思的概念产品，使用文字指令来操作网站，比如输入文字“点击按钮”，它就自动点击网页按钮，底层用的是浏览器自动化框架 Selenium。

---

### [第 293 期] LapisCV

- 来源: docs/issue-293.md
- 链接: https://github.com/BingyanStudio/LapisCV
- 描述: 基于 Obsidian / Typora 编辑器的 Markdown 简历模板，可以导出 PDF 文件。（[@YiNNx](https://github.com/ruanyf/weekly/issues/4111) 投稿）

---

### [第 293 期] OpenAPI-UI

- 来源: docs/issue-293.md
- 链接: https://github.com/rookie-luochao/openapi-ui
- 描述: 该工具生成 Swagger 或 OpenAPI 3 格式的 API 接口文档，也可当作简洁的 Postman 使用。（[@rookie-luochao](https://github.com/ruanyf/weekly/issues/4114) 投稿）

---

### [第 293 期] git-diff-view

- 来源: docs/issue-293.md
- 链接: https://github.com/MrWangJustToDo/git-diff-view
- 描述: 一个 React/Vue 组件，用来显示 git diff 的结果，类似于 GitHub 的样式。（[@MrWangJustToDo](https://github.com/ruanyf/weekly/issues/4105) 投稿）

---

### [第 293 期] AI 时间线

- 来源: docs/issue-293.md
- 链接: http://www.ai-timeline.top/
- 描述: 一个有意思的网站，输入一个关键词，自动生成该词的时间线，上图是输入“github”的生成结果，它的代码仓库在 [GitHub](https://github.com/zhugezifang/ai_timeline)。（[@zhugezifang](https://github.com/ruanyf/weekly/issues/4115) 投稿）

---

### [第 293 期] Earthworm

- 来源: docs/issue-293.md
- 链接: https://github.com/cuixueshe/earthworm
- 描述: 一个开源的 Web 程序，通过连词造句的方式，经过不断重复练习英语，[线上体验](https://earthworm.cuixueshe.com/)。（[@cuixiaorui](https://github.com/ruanyf/weekly/issues/4120) 投稿）

---

### [第 293 期] Postal

- 来源: docs/issue-293.md
- 链接: https://github.com/postalserver/postal
- 描述: 一个开源的电子邮件服务器，自带 Web 界面。

---

### [第 293 期] briefsky

- 来源: docs/issue-293.md
- 链接: https://briefsky.app/
- 描述: 一个开源的天气预报前端，可以接入各种天气数据源。

---

### [第 293 期] Qaul

- 来源: docs/issue-293.md
- 链接: https://qaul.net/
- 描述: 一个可以离线通信的软件，允许一群用户在不联网的情况下，通过本机的共享 WiFi 发送消息。

---

### [第 293 期] Piped

- 来源: docs/issue-293.md
- 链接: https://github.com/TeamPiped/Piped
- 描述: 一个开源的 Youtube 网页前端 UI。

---

### [第 293 期] Riffusion

- 来源: docs/issue-293.md
- 链接: https://www.riffusion.com/
- 描述: 一个免费的 AI 工具，给出一段提示，它会生成相应的歌曲，并且是带有歌词、人声演唱的。

---
### [第 294 期] Frogmouth

- 来源: docs/issue-294.md
- 链接: https://github.com/Textualize/frogmouth
- 描述: 命令行的 Markdown 阅读器。

---

### [第 294 期] SSH3

- 来源: docs/issue-294.md
- 链接: https://github.com/francoismichel/ssh3
- 描述: 使用 QUIC + TLS 重新实现的 SSH 加密登陆工具，支持 UDP 端口转发。

---

### [第 294 期] X-Hiring

- 来源: docs/issue-294.md
- 链接: https://github.com/hehehai/x-hiring
- 描述: 每日自动抓取于 V2EX 和电鸭社区的招聘信息，使用 Google AI 提取摘要。（[@hehehai](https://github.com/ruanyf/weekly/issues/4127) 投稿）

---

### [第 294 期] pear-rec

- 来源: docs/issue-294.md
- 链接: https://github.com/027xiguapi/pear-rec/blob/main/README.zh-CN.md
- 描述: 一个在线的 GIF 编辑工具，也可以对 MP4 视频进行解析导入。（[@027xiguapi](https://github.com/ruanyf/weekly/issues/4128) 投稿）

---

### [第 294 期] Y-TOC

- 来源: docs/issue-294.md
- 链接: https://github.com/struy-cn/Y-TOC
- 描述: 一个内容目录海报美化生成工具。（[@StruggleYang](https://github.com/ruanyf/weekly/issues/4130) 投稿）

---

### [第 294 期] emgithub

- 来源: docs/issue-294.md
- 链接: https://github.com/yusanshi/emgithub
- 描述: 打开 GitHub 仓库某个文件的页面，将地址栏的 github.com 改成 emgithub.com，就可以获得当前文件的嵌入代码，像嵌入 GitHub Gist 代码一样嵌入到页面中。（[@yusanshi](https://github.com/ruanyf/weekly/issues/4131) 投稿）

---

### [第 294 期] Calorie Calculator

- 来源: docs/issue-294.md
- 链接: https://github.com/mggger/Calorie-Calculator
- 描述: 上传食物图片，自动计算卡路里，基于 Google Gemini AI。（[@mggger](https://github.com/ruanyf/weekly/issues/4138) 投稿）

---

### [第 294 期] 壁纸样机生成器

- 来源: docs/issue-294.md
- 链接: https://mjcn.club/
- 描述: 一个在线工具，图片套 iPhone、iPad、Mac 的模板，生成样机图片。（[@CheckCoder](https://github.com/ruanyf/weekly/issues/4140) 投稿）

---

### [第 294 期] Searchable

- 来源: docs/issue-294.md
- 链接: https://www.engineerdraft.com/en/searchable/
- 描述: 一款 Mac 应用，利用 OpenAI 的 Clip 模型在本地对图片进行索引和搜索，可以本地搜索图片文字、语义化搜索和以图搜图。（[@yujinqiu](https://github.com/ruanyf/weekly/issues/4142) 投稿）

---

### [第 294 期] Vmail.dev

- 来源: docs/issue-294.md
- 链接: https://github.com/yesmore/vmail
- 描述: 使用 Cloudflare email worker 实现的临时邮箱服务，可以[自己部署](https://dev.yesmore.cc/projects/vmail)。（[@yesmore](https://github.com/ruanyf/weekly/issues/4133) 投稿）

---

### [第 294 期] VidHub

- 来源: docs/issue-294.md
- 链接: https://apps.apple.com/us/app/vidhub-video-library-player/id1659622164
- 描述: 苹果设备的视频播放器，可以管理和播放本地、网盘、NAS、Cloud Drive 来源的视频。（[@julycamera](https://github.com/ruanyf/weekly/issues/4143) 投稿）

---

### [第 294 期] VideoSora

- 来源: docs/issue-294.md
- 链接: https://videosora.app/zh-cn/
- 描述: 一款将文本或语音转化成图文短视频的在线工具。（[@tangpanqing](https://github.com/ruanyf/weekly/issues/4150) 投稿）

---

### [第 294 期] Segment Anything web UI

- 来源: docs/issue-294.md
- 链接: https://github.com/Kingfish404/segment-anything-webui
- 描述: Segment Anything 模型的前端交互 UI，包括了最基本的点击，画框和自动分割等功能，还引入了 CLIP 实现语义选择分割。（[@Kingfish404](https://github.com/ruanyf/weekly/issues/4154) 投稿）

---

### [第 294 期] Toolong

- 来源: docs/issue-294.md
- 链接: https://github.com/Textualize/toolong
- 描述: 一个终端工具，可以查看和搜索非常长的文本文件（比如日志）。（[@WFANG12719](https://github.com/ruanyf/weekly/issues/4158) 投稿）

---

### [第 294 期] Notion Flow

- 来源: docs/issue-294.md
- 链接: https://notion-flow.xheldon.com/
- 描述: 一个浏览器插件，可以在 Notion 页面显示文章目录，并将内容发送到 GitHub Pages。（[@Xheldon](https://github.com/ruanyf/weekly/issues/4163) 投稿）

---

### [第 294 期] Side Browser

- 来源: docs/issue-294.md
- 链接: https://www.sidebrowser.xyz/
- 描述: 一个浏览器插件，允许在浏览器的侧边栏打开网页。（[@extrastu](https://github.com/ruanyf/weekly/issues/4159) 投稿） 有读者反映，该插件可能借鉴了另一个相同功能的 [Sidebar 插件](https://chromewebstore.google.com/detail/sidebartab-pin-chatgpt-or/acghhljehhigfeinngmggkpgbacpikfe)。（[@vinebyte](https://github.com/ruanyf/weekly/issues/4164) 投稿）

---
### [第 295 期] Garnet

- 来源: docs/issue-295.md
- 链接: https://github.com/microsoft/garnet
- 描述: 上周，著名的缓存服务器 Redis 宣布更改许可证，未经许可不得基于它对外提供云服务。 此前两天，微软发布了一个兼容 Redis 的缓存服务器 Garnet，不知道两件事之间是否存在关联。 另外，Redis 现在也被分叉了，诞生了两个全新的项目 [Redict](https://redict.io/) 和 [Valkey](https://github.com/valkey-io/valkey)，目标是成为自由软件版本的 Redis。

---

### [第 295 期] Superjson

- 来源: docs/issue-295.md
- 链接: https://github.com/blitz-js/superjson
- 描述: 一个 JavaScript 模块，用于字符串和 JSON 数据的互相转换，支持多种 JSON 不支持的数据格式。

---

### [第 295 期] Copilot for obsidian

- 来源: docs/issue-295.md
- 链接: https://github.com/logancyang/obsidian-copilot
- 描述: Obsidian 编辑器的一个开源插件，使其可以用上本地的 AI 助手，参见[介绍文章](https://mp.weixin.qq.com/s/at7K_8lEfVzQJq5qnpzvUg)。（[@ivone-liu](https://github.com/ruanyf/weekly/issues/4171) 投稿）

---

### [第 295 期] LunarLink

- 来源: docs/issue-295.md
- 链接: https://github.com/tahitimoon/LunarLink
- 描述: 一个基于 Web 的接口自动化测试平台，可以快速编写和运行接口自动化测试用例。（[@tahitimoon](https://github.com/ruanyf/weekly/issues/4173) 投稿）

---

### [第 295 期] text2video

- 来源: docs/issue-295.md
- 链接: https://github.com/bravekingzhang/text2video
- 描述: 一个开源的文本转图文视频的软件。（[@bravekingzhang](https://github.com/ruanyf/weekly/issues/4187) 投稿）

---

### [第 295 期] simple-mind-map

- 来源: docs/issue-295.md
- 链接: https://github.com/wanglin2/mind-map
- 描述: （思绪思维导图） 一个开源的 Web 思维导图，试用 [Demo](https://wanglin2.github.io/mind-map/)。（[@wanglin2](https://github.com/ruanyf/weekly/issues/4190) 投稿）

---

### [第 295 期] Shap-E

- 来源: docs/issue-295.md
- 链接: https://github.com/openai/shap-e
- 描述: 一个生成式 AI 模型，从文本生成 3D 动画图片。

---

### [第 295 期] blog-cells

- 来源: docs/issue-295.md
- 链接: https://github.com/rameshvarun/blog-cells
- 描述: 这个工具可以在网页插入互动式区块，用来展示和执行 JavaScript 代码，类似于 Jupyter。

---

### [第 295 期] Magic Wormhole

- 来源: docs/issue-295.md
- 链接: https://github.com/magic-wormhole/magic-wormhole
- 描述: 一个文件传输协议，可以在任意两台计算机（不必在同一局域网）之间传输文件。上传方会获得一个密码，下载方只要输入密码就能获取文件。 它有很多第三方客户端（包括手机 App），比如[这个](https://github.com/LeastAuthority/destiny)和[这个](https://github.com/pavelsof/mobile-wormhole)。

---

### [第 295 期] Mist

- 来源: docs/issue-295.md
- 链接: https://mist-project.github.io
- 描述: 这个工具可以在图片上面添加水印底纹，使得该图片无法再被 AI 模型作为训练材料。上图是添加水印后的效果（左图），以及放大的水印（右图）。

---
### [第 296 期] DOOM 验证码

- 来源: docs/issue-296.md
- 链接: https://vivirenremoto.github.io/doomcaptcha/
- 描述: DOOM 游戏被用作网页验证码，只有消灭指定数目的敌人，才能通过验证。

---

### [第 296 期] OneUptime

- 来源: docs/issue-296.md
- 链接: https://github.com/OneUptime/oneuptime
- 描述: 一个开源的服务可用性检查工具，记录服务的健康状态，如果发现服务下线，立刻发送通知，可以替代 [StatusPage.io](https://www.statuspage.io/)。

---

### [第 296 期] DashPress

- 来源: docs/issue-296.md
- 链接: https://github.com/dashpresshq/dashpress
- 描述: 一个开源工具，只需执行一个命令，就会自动分析数据库结构，生成管理后台，号称不用写代码。

---

### [第 296 期] Landing page boilerplate

- 来源: docs/issue-296.md
- 链接: https://github.com/weijunext/landing-page-boilerplate
- 描述: 开源的项目落地页模板，参见[介绍文章](https://juejin.cn/post/7350200488455520267)。（[@weijunext](https://github.com/ruanyf/weekly/issues/4197) 投稿）

---

### [第 296 期] GitHub Custom Notifier

- 来源: docs/issue-296.md
- 链接: https://github.com/qiweiii/github-custom-notifier
- 描述: 一个开源的浏览器插件，用来监听 GitHub 官方没有提供的一些事件（比如创建 label），事件发生时，浏览器就会发送通知。（[@qiweiii](https://github.com/ruanyf/weekly/issues/4199) 投稿）

---

### [第 296 期] HeyForm

- 来源: docs/issue-296.md
- 链接: https://github.com/heyform/heyform
- 描述: 一个开源的表单生成器，创建调查、问卷、投票等，可以不编写一行代码。（[@iMuFeng](https://github.com/ruanyf/weekly/issues/4207) 投稿）

---

### [第 296 期] Youdeyiwu

- 来源: docs/issue-296.md
- 链接: https://github.com/dafengzhen/youdeyiwu
- 描述: 一个开源的轻量级论坛，追求界面简洁和使用方便，后端使用 Java，前端使用 Next.js。（[@dafengzhen](https://github.com/ruanyf/weekly/issues/4211) 投稿）

---

### [第 296 期] Markdown Genji

- 来源: docs/issue-296.md
- 链接: https://genji-md.dev/
- 描述: VitePress 的一个插件，用于在 Markdown 文档插入可以执行的代码块，创建交互式文档。（[@pearmini](https://github.com/ruanyf/weekly/issues/4212) 投稿）

---

### [第 296 期] Mutative

- 来源: docs/issue-296.md
- 链接: https://github.com/ruanyf/weekly/issues/4222
- 描述: 一个操作不可变状态的 JS 库，追求高效。（[@unadlib](https://github.com/ruanyf/weekly/issues/4222) 投稿）。

---

### [第 296 期] Fusion

- 来源: docs/issue-296.md
- 链接: https://github.com/0x2E/fusion
- 描述: 一个轻量、简洁的 RSS 聚合和阅读器，使用 Go + Svelte 开发。（[@0x2E](https://github.com/ruanyf/weekly/issues/4223) 投稿）

---

### [第 296 期] node-screenshots

- 来源: docs/issue-296.md
- 链接: https://github.com/nashaofu/node-screenshots
- 描述: 一个跨平台、零依赖的 Node.js 模块，用于截图和录屏。（[@nashaofu](https://github.com/ruanyf/weekly/issues/4224) 投稿）

---

### [第 296 期] 流畅阅读

- 来源: docs/issue-296.md
- 链接: https://github.com/Bistutu/FluentRead
- 描述: 一款浏览器翻译插件，支持人工智能引擎。（[@Bistutu](https://github.com/ruanyf/weekly/issues/4230) 投稿）

---

### [第 296 期] keynavish

- 来源: docs/issue-296.md
- 链接: https://github.com/lesderid/keynavish
- 描述: 使用键盘控制鼠标运动的 Windows 软件。（[@NomandChan](https://github.com/ruanyf/weekly/issues/55) 投稿）

---

### [第 296 期] K8Z

- 来源: docs/issue-296.md
- 链接: https://github.com/k8zdev/k8z
- 描述: 管理 Kubernetes 的开源工具，有手机客户端和桌面客户端。（[@kofj](https://github.com/ruanyf/weekly/issues/4246) 投稿）

---
### [第 297 期] sshx

- 来源: docs/issue-297.md
- 链接: https://sshx.io/
- 描述: 这个工具可以通过链接，与其他人共享你的终端。

---

### [第 297 期] Hyphen

- 来源: docs/issue-297.md
- 链接: https://github.com/00000o1/-
- 描述: 一个 Web 组件的基类，你可以在它的基础上定义自己的 Web Component。类似的工具还有 [Cami.js](https://github.com/kennyfrc/cami.js)。

---

### [第 297 期] Hono

- 来源: docs/issue-297.md
- 链接: https://github.com/honojs/hono
- 描述: 一个 Node.js 的轻量级 Web 框架，专注于边缘节点的使用场景。

---

### [第 297 期] Shiro

- 来源: docs/issue-297.md
- 链接: https://github.com/Innei/Shiro
- 描述: 一个极简主义的个人网站，作为 [Mix Space](https://github.com/mx-space) 架设的站点的前端。（[@Innei](https://github.com/ruanyf/weekly/issues/4274) 投稿）

---

### [第 297 期] Cover your tracks

- 来源: docs/issue-297.md
- 链接: https://firstpartysimulator.org/
- 描述: 这个工具可以查看，服务器能够拿到多少客户端信息，从而生成你的指纹。

---

### [第 297 期] TeleMonitor

- 来源: docs/issue-297.md
- 链接: https://github.com/bboysoulcn/telemonitor
- 描述: Python 写的系统监控工具，监控 CPU、内存和磁盘的使用情况，并通过 Telegram 发送警告。（[@bboysoulcn](https://github.com/ruanyf/weekly/issues/4260) 投稿）

---

### [第 297 期] Amprobe

- 来源: docs/issue-297.md
- 链接: https://github.com/amuluze/amprobe
- 描述: 一个 Go + Vue3 开发的轻量级主机及容器监控工具。（[@amuluze](https://github.com/ruanyf/weekly/issues/4261) 投稿）

---

### [第 297 期] ElemSnap

- 来源: docs/issue-297.md
- 链接: https://chromewebstore.google.com/detail/elemsnap/mblkhbaakhbhiimkbcnmeciblfhmafna
- 描述: Chrome 浏览器截图 + 美化插件。（[@AydenGen](https://github.com/ruanyf/weekly/issues/4273) 投稿）

---

### [第 297 期] stokado

- 来源: docs/issue-297.md
- 链接: https://github.com/KID-joker/stokado
- 描述: 浏览器存储对象（比如 localStorage、IndexDB）的包装库，提供统一的 API，以及一些便利的功能（比如过期时间）。（[@KID-joker](https://github.com/ruanyf/weekly/issues/4279) 投稿）

---

### [第 297 期] PPResume

- 来源: docs/issue-297.md
- 链接: https://ppresume.com/
- 描述: 一个基于 LaTeX 的简历生成器，可以生成精美的简历，并提供极高质量的 PDF 输出。（[@xiaohanyu](https://github.com/ruanyf/weekly/issues/4285) 投稿）

---

### [第 297 期] 自律石头

- 来源: docs/issue-297.md
- 链接: https://apps.apple.com/cn/app/%E8%87%AA%E5%BE%8B%E7%9F%B3%E5%A4%B4-%E8%B5%B0%E8%B7%AF%E8%AF%BB%E4%B9%A6%E6%8D%A2%E6%97%B6%E9%97%B4-%E4%B8%8D%E5%81%9A%E6%89%8B%E6%9C%BA%E6%8E%A7/id6479392365
- 描述: 一个 iOS 手机应用，可以限制指定 App 的使用时间，防止过度沉迷手机。（[@tuesda](https://github.com/ruanyf/weekly/issues/4284) 投稿）

---

### [第 297 期] 音虫

- 来源: docs/issue-297.md
- 链接: https://www.soundbug.com/
- 描述: （SoundBug） 一款国产的音频工作站，用来音乐编曲和录音的制作工具，追求简洁直观的用户界面和易于上手的操作。（[@asoiso](https://github.com/ruanyf/weekly/issues/4286) 投稿）

---

### [第 297 期] 极简朋友圈

- 来源: docs/issue-297.md
- 链接: https://github.com/kingwrcy/moments
- 描述: 一个仿照微信朋友圈 UI 的个人短博客网站，参见 [Demo](https://m.mblog.club/)。（[@kingwrcy](https://github.com/ruanyf/weekly/issues/4288) 投稿）

---

### [第 297 期] Newcar

- 来源: docs/issue-297.md
- 链接: https://github.com/dromara/newcar
- 描述: 一个 JS 语言的前端动画引擎，基于 Skia 的WebAssembly 版本，在 Canvas 画布上生成动画。（[@sheepbox8646](https://github.com/ruanyf/weekly/issues/4287) 投稿）

---
### [第 298 期] Lan Mouse

- 来源: docs/issue-298.md
- 链接: https://github.com/feschber/lan-mouse
- 描述: 一个开源软件，使用同一个鼠标和键盘，控制局域网的多台电脑。

---

### [第 298 期] UnoCssUi

- 来源: docs/issue-298.md
- 链接: https://github.com/cherryful/unocss-ui
- 描述: 一个基于 Vue3、UnoCSS、Tailwindcss 的组件库，原子化设计，没有任何依赖。（[@szluyu99](https://github.com/ruanyf/weekly/issues/4294) 投稿）

---

### [第 298 期] drawDB

- 来源: docs/issue-298.md
- 链接: https://github.com/drawdb-io/drawdb
- 描述: 开源的数据库结构图和 SQL 生成工具。（[@yingming006](https://github.com/ruanyf/weekly/issues/4314) 投稿）

---

### [第 298 期] vscode-highlight-text

- 来源: docs/issue-298.md
- 链接: https://github.com/Simon-He95/vscode-highlight-text
- 描述: 一个 VS Code 插件，可以自定义任意语言和框架的高亮规则。（[@Simon-He95](https://github.com/ruanyf/weekly/issues/4302) 投稿）

---

### [第 298 期] Easy GitHub 2FA authentication

- 来源: docs/issue-298.md
- 链接: https://github.com/Dolov/chrome-github-2fa
- 描述: 一款开源的浏览器插件，自动填写 GitHub 双因素认证的验证码。（[@Dolov](https://github.com/ruanyf/weekly/issues/4328) 投稿）

---

### [第 298 期] JavaVision

- 来源: docs/issue-298.md
- 链接: https://gitee.com/giteeClass/java-vision
- 描述: 一个视觉识别项目，具备物体识别、人脸识别、以图搜图等核心功能，使用 Java 开发，需要本地部署，然后通过 Web API 调用。（[@javpower](https://github.com/ruanyf/weekly/issues/4343) 投稿）

---

### [第 298 期] Shion

- 来源: docs/issue-298.md
- 链接: https://github.com/shion-app/shion
- 描述: 开源的 Windows 软件，用来追踪统计个人的时间消耗，自动记录各种软件的使用时间，以及同步浏览器历史。（[@hanaTsuk1](https://github.com/ruanyf/weekly/issues/4350) 投稿）

---

### [第 298 期] Chat2DB

- 来源: docs/issue-298.md
- 链接: https://github.com/chat2db/Chat2DB
- 描述: 开源的数据库管理工具，有桌面端和 Web 端，用来浏览操作各种数据库。（[@JerryFan626](https://github.com/ruanyf/weekly/issues/4349) 投稿）

---

### [第 298 期] Teable

- 来源: docs/issue-298.md
- 链接: https://github.com/teableio/teable
- 描述: 开源的 Airtable 替代品，无代码搭建数据库应用，建立在 PostgreSQL 之上，界面友好、响应快速。（[@yingming006](https://github.com/ruanyf/weekly/issues/4352) 投稿）

---

### [第 298 期] main-thread-scheduling

- 来源: docs/issue-298.md
- 链接: https://github.com/astoilkov/main-thread-scheduling
- 描述: 这个 JS 模块号称可以把计算量大的任务放到主进程，同时又不会阻塞主进程，UI 界面保持对用户的随时响应。它的源码有学习价值。

---
### [第 299 期] ElysiaJS

- 来源: docs/issue-299.md
- 链接: https://elysiajs.com/
- 描述: JS 语言的 Web 框架，专门为 Bun 运行环境开发。

---

### [第 299 期] mcfly

- 来源: docs/issue-299.md
- 链接: https://github.com/cantino/mcfly
- 描述: Shell 操作历史的搜索工具，提供神经网络搜索功能，可以替代 ctrl-r 快捷键。

---

### [第 299 期] DocKit

- 来源: docs/issue-299.md
- 链接: https://github.com/geek-fun/dockit
- 描述: Elasticsearch/OpenSearch 的跨平台桌面客户端，集成了 OpenAI，可以用自然语言与数据库交互。（[@Blankll](https://github.com/ruanyf/weekly/issues/4374) 投稿）

---

### [第 299 期] IMaker 创客

- 来源: docs/issue-299.md
- 链接: https://github.com/slince-zero/IMaker
- 描述: 一款开源的封面设计工具，基于 JS 的 Web 应用，有[试用 Demo](https://img-maker.vercel.app/)。（[@slince-zero](https://github.com/ruanyf/weekly/issues/4385) 投稿）

---

### [第 299 期] VideoSubtitleGenerator

- 来源: docs/issue-299.md
- 链接: https://github.com/buxuku/VideoSubtitleGenerator
- 描述: 一个命令行工具，通过语音识别，批量为本地的视频文件生成字幕，并支持翻译。（[@buxuku](https://github.com/ruanyf/weekly/issues/4393) 投稿）

---

### [第 299 期] vmr

- 来源: docs/issue-299.md
- 链接: https://github.com/gvcgo/version-manager
- 描述: 一个跨平台的通用版本管理器，目前支持40多种编程语言和工具。（[@moqsien](https://github.com/ruanyf/weekly/issues/4398) 投稿） 另有一个类似工具 [vfox](https://github.com/version-fox/vfox)。（[@aooohan](https://github.com/ruanyf/weekly/issues/4233) 投稿）

---

### [第 299 期] Pichome

- 来源: docs/issue-299.md
- 链接: https://github.com/zyx0814/Pichome
- 描述: 一款开源网盘程序，使用 PHP 开发。（[@fhxsnabi](https://github.com/ruanyf/weekly/issues/4405) 投稿）

---

### [第 299 期] 笔.COOL

- 来源: docs/issue-299.md
- 链接: https://bi.cool/bi
- 描述: CodePen 的国产替代品，实时预览 HTML、CSS 和 JavaScript 代码的渲染结果。（[@uovol](https://github.com/ruanyf/weekly/issues/4407) 投稿）

---

### [第 299 期] vue-styled-components

- 来源: docs/issue-299.md
- 链接: https://github.com/v-vibe/vue-styled-components
- 描述: 一款类似 styled-components 的 CSS 工具，支持 vue 3。（[@akinocccc](https://github.com/ruanyf/weekly/issues/4409) 投稿）

---

### [第 299 期] MonsterMusic

- 来源: docs/issue-299.md
- 链接: https://github.com/ZTFtrue/MonsterMusic
- 描述: 一款开源的安卓音乐播放器。（[@ZTFtrue](https://github.com/ruanyf/weekly/issues/4411) 投稿）

---

### [第 299 期] 豆瓣图书馆查询助手

- 来源: docs/issue-299.md
- 链接: https://github.com/wyj0605/douban_library
- 描述: 一款浏览器插件，在豆瓣读书页面上，查看该书在指定图书馆的藏书情况。（[@wyj0605](https://github.com/ruanyf/weekly/issues/4424) 投稿）

---
### [第 300 期] GitUI

- 来源: docs/issue-300.md
- 链接: https://github.com/extrawurst/gitui
- 描述: 终端里面的 Git 图形界面，将各种 git 操作可视化，使用 Rust 语言开发。

---

### [第 300 期] Outline

- 来源: docs/issue-300.md
- 链接: https://github.com/outline/outline
- 描述: 一个开源的在线知识库软件，支持多人合作。

---

### [第 300 期] Vnt

- 来源: docs/issue-300.md
- 链接: https://github.com/lbl8603/vnt
- 描述: 一个开源工具，将不同网络下的多个设备虚拟到一个局域网下，类似与 tailscale、zerotier、n2n。（[@lbl8603](https://github.com/ruanyf/weekly/issues/4444) 投稿）

---

### [第 300 期] DashPlayer

- 来源: docs/issue-300.md
- 链接: https://github.com/solidSpoon/DashPlayer
- 描述: 一款专为英语学习打造的开源视频播放器，支持生成双语字幕，进行精听或泛听练习。（[@solidSpoon](https://github.com/ruanyf/weekly/issues/4454) 投稿）

---

### [第 300 期] 字幕工具箱

- 来源: docs/issue-300.md
- 链接: https://zm.i8k.tv/
- 描述: 这个网站收集了一些字幕相关的工具，纯前端处理，无需安装任何插件或软件。（[@mzhren](https://github.com/ruanyf/weekly/issues/4464) 投稿）

---

### [第 300 期] 封面图片生成器

- 来源: docs/issue-300.md
- 链接: https://spacexcode.com/coverview/
- 描述: 一个制作简单封面图的 Web 工具。（[@fantingsheng](https://github.com/ruanyf/weekly/issues/4439) 投稿） 另外，还有一个类似的 Logo 制作工具“[Logo 厨师](https://www.logocook.shop/)”。（[@gdfsdjj145](https://github.com/ruanyf/weekly/issues/4455) 投稿）

---

### [第 300 期] Easy Voice Toolkit

- 来源: docs/issue-300.md
- 链接: https://github.com/Spr-Aachen/Easy-Voice-Toolkit
- 描述: 一个简易的语音工具箱，提供音频处理、语音识别、合成等音频工具，使用 Python 语言开发。（[@Hao4Wang](https://github.com/ruanyf/weekly/issues/4471) 投稿）

---

### [第 300 期] Segmentify

- 来源: docs/issue-300.md
- 链接: https://segmentify.app/zh
- 描述: 一个 Figma 插件，使用浏览器 GPU 能力运行 AI SAM 模型，快速分割图片，从图片中提取元素至 Figma 文件。（[@janily](https://github.com/ruanyf/weekly/issues/4472) 投稿）

---

### [第 300 期] Web-Tracing

- 来源: docs/issue-300.md
- 链接: https://github.com/M-cheng-web/web-tracing
- 描述: 一个开源的前端埋点工具，提供项目监控。（[@M-cheng-web](https://github.com/ruanyf/weekly/issues/4451) 投稿）

---

### [第 300 期] Technitium DNS

- 来源: docs/issue-300.md
- 链接: https://technitium.com/dns/
- 描述: 一款开源 DNS 服务器，带有 Web 管理面板。

---

### [第 300 期] QR code designer

- 来源: docs/issue-300.md
- 链接: https://github.com/kochrt/qr-designer
- 描述: 一个 Web 工具，用来设计二维码，可以嵌入各种文字和图形，另有一个[类似工具](http://jsfiddle.net/lachlan/r8qWV/)。

---

### [第 300 期] BullMQ

- 来源: docs/issue-300.md
- 链接: https://github.com/taskforcesh/bullmq
- 描述: Redis 的 JS 客户端，号称强大且快速。

---
