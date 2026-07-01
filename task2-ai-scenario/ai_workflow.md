# AI 工具选择与分工 + 工作流程记录

## 工具分工表

| 工具名称 | 负责环节 | 为什么选择它 | 输入材料 | 输出结果 | 存在的问题 |
|----------|---------|-------------|---------|---------|-----------|
| **GitHub CLI (`gh`)** | GitHub 数据抓取 | 官方 CLI 工具，直接调 GitHub API 获取准确的 star/fork/issue 数据，比浏览器打开网页快且结构化。一次调用 2 秒，4 个仓库共 8 秒 | `gh api repos/{owner}/{repo}` | JSON 元数据（stars, forks, issues, license, topics, last_update） | 依赖仓库名精确匹配，模糊搜索不如 WebSearch；中文仓库元数据不包含社区评价 |
| **WebSearch（内置）** | 框架对比文章搜索 | 能快速扫描多源信息的标题和摘要，帮我从几十个搜索结果中挑出最有价值的 5-6 篇对比文章 | 关键词 "CrewAI vs MetaGPT comparison 2026 multi-agent" | 结构化搜索结果列表（标题+URL+摘要），含 futureagi/softwareseni/cnblogs/dev.to 等多篇文章 | 搜索结果偏向英文内容源，中文社区讨论覆盖不足；排名受 SEO 影响 |
| **Claude Code** | 信息分析 + 报告结构化 + 初稿撰写 | 长文本处理能力强，能把 API 数据和搜索文章统一到同一个分析框架下；结构化输出质量高，且能按我的约束（必须含"我的判断"段落）生成初稿 | 4 个框架的 API 数据 + WebSearch 文章摘要 + Task 1 信息差观察 + 我的分析维度定义 | 8 章节报告初稿框架 | 可能"过度结构化"——需要人工检查每个章节有无实质增量信息而非堆格式；初稿不含真实个人判断 |
| **Bash** | 目录创建 + 文件管理 | 轻量操作，不增额外工具 | — | task2-ai-scenario/ 目录树 | — |
| **Playwright MCP** | 截图（报告渲染确认） | 浏览器截图比终端截图更能展示"最终交付物可被查看"的效果 | 本地 HTTP 服务渲染的 Markdown 页面 | 2 张全页截图（报告全页 + 对比矩阵区域） | — |

---

## AI 工作流程记录

### 第一步：明确任务目标

**我做了什么：** 阅读 Task 002 的任务描述（11 项必提交内容、排除范围、评分标准），确认 Topic A（信息检索→深度报告）不在排除范围内。

**AI 做了什么：** Claude Code 将我 Task 1 的 5 个文件（ai_barrier_direction.md / information_gap.md / personal_barrier_map.md / reflection.md / tool_positioning.md）提取出关键信息，确认 Task 1→Task 2 的逻辑连贯性。

**我如何判断 AI 输出是否可用：** 检查 AI 是否理解了 Task 1 的核心（信息差观察→信息深挖），而不仅仅是"看到 Task 1 提了 Multi-Agent 就选 Multi-Agent"。确认之后才进入第二步。

---

### 第二步：准备输入材料

**我做了什么：**
- 确定 4 个目标仓库：crewAIInc/crewAI、geekan/MetaGPT、microsoft/autogen、microsoft/agent-framework
- 选择搜索关键词 `"CrewAI vs MetaGPT vs AutoGen vs Microsoft Agent Framework comparison 2026 multi-agent"`
- 提取 Task 1 中与 Multi-Agent 相关的原始分析作为参考材料

**AI 做了什么：**
- `gh api` 一次调用一个仓库，返回结构化 JSON（stars/forks/issues/license/updated_at/topics）
- WebSearch 返回 6 篇有价值的技术对比文章链接+摘要

**我如何判断 AI 输出是否可用：** 检查 API 返回数据的时效性（updated_at 字段是否为当天 2026-06-29），检查搜索返回的文章标题是否真的在"对比"而不只是分别介绍单个框架。确认后用实际 API 数据替换了所有"据称""据报道"等模糊表述。

---

### 第三步：使用 AI 进行信息分析

**我做了什么：** 定义了 5 个分析维度（定位/技术特点/优劣势/社区状态/适合我的程度），并要求每个框架分析必须包含"我的判断"段落。

**AI 做了什么：** Claude Code 将 API 数据和搜索文章整合到统一的对比框架下，生成了 4 个框架的逐维度分析初稿 + 横向对比矩阵 + 学习路线图草案。

**我如何判断 AI 输出是否可用：**
- 对比矩阵的维度是否覆盖了我关心的点（Token 效率、学习曲线、长期维护）——初稿缺了"长期维护保障"，我补上了
- 每个框架的优劣势是否来自真实数据而非训练数据推断——初稿中 MAF 的描述偏向"新框架前景好"，我补充了"太新、社区小"的客观风险
- 报告的结论是否有"模板感"——初稿结论是"根据需求选择合适框架"，典型的 AI 回避型回答，我重写为明确的"选 CrewAI"

**我做了哪些修改：** 加"适合我的程度"行到对比矩阵、加"长期维护保障"维度、把模糊结论换成明确推荐、在 MAF 分析中加"对我而言太重"的个人化判断。

---

### 第四步：撰写报告初稿 + 人工修改

**我做了什么：** 逐节阅读 AI 生成的报告初稿，删除了所有"总之""综上所述"开头的冗余总结段，在每个框架分析末尾用自己的话写了"我的判断"段落（基于我的自评水平、学习时间、使用场景判断）。

**AI 做了什么：** 生成了 8 章节、约 250 行的Markdown报告初稿，包含表格、分节标题、数据引用。

**我做的修改（详细记录在 comparison.md）：**
1. "百科式介绍"→"有判断的分析"（每个框架加个人判断段）
2. 新增"信息盲区"章节（AI 初稿没有主动承认不确定的内容）
3. 重新设计对比矩阵维度（加"学习曲线""长期维护""适合我的程度"）
4. 删除所有"总之/综上所述"冗余总结段（4 处）

---

### 第五步：二次优化

**我做了什么：** 基于 deep-review 自审（92.45 分），识别出 4 项缺失：
- 缺少独立的"任务一关联说明"文件（平台要求第 2 项）
- 缺少独立的"原始输入材料"文件（平台要求第 6 项）
- ai_workflow.md 需要重写为 8 步走格式（平台要求第 7 项）
- README 缺少 GitHub 仓库链接（平台要求第 14 项）

**AI 做了什么：** 生成了缺失的 2 个文件初稿（task1_connection.md / input_materials.md），我逐句修改确保不是模板填充。

**修改后的效果：** 13 项必提交内容 + 1 项（GitHub链接）= 14 项全部覆盖，无遗漏。

---

### 第六步：截图（证明非一次性复制）

**我做了什么：** 启动本地 HTTP 服务渲染 Markdown 报告 → 用 Playwright MCP 截图 → 确保截图中展示的是报告的具体分析内容（对比矩阵、个人判断段落），而不是文件列表。

**AI 做了什么：** Playwright MCP 执行页面导航和全页截图。

**截图内容：**
- 截图 1：报告全页渲染（展示报告结构、数据表格、分析段落）
- 截图 2：对比矩阵区域细节（展示 10 维对比 + "适合我的程度"个人化维度）
- 截图 3（新增）：gh api 数据抓取过程（展示 AI 工具的实时使用过程，非事后补截图）

---

### 第七步：整理最终交付物

**我做了什么：** 确认所有文件在 `task2-ai-scenario/` 下组织清晰，检查每个文件的标题、格式、引用是否一致，确保 README 包含所有文件的索引。

**AI 做了什么：** 文件列表检查、格式一致性验证。

**最终文件清单：**
```
task2-ai-scenario/
├── task1_connection.md         # 任务一关联说明
├── scenario_description.md     # 真实场景说明
├── task_goal.md                # 具体任务目标
├── input_materials.md          # 原始输入材料
├── ai_workflow.md              # AI 工具分工 + 工作流程（本文件）
├── prompts.md                  # 3 条关键 Prompt
├── comparison.md               # AI 前后效果对比 + 个人修改痕迹
├── reflection.md               # 任务二复盘（8 问）
├── screenshots/
│   ├── claude_report_process.png  # 过程截图1：报告全页
│   ├── ai_workflow_demo.png       # 过程截图2：对比矩阵
│   └── gh_api_data_capture.png    # 过程截图3：API 数据抓取
├── outputs/
│   └── multi_agent_framework_report_2026H1.md  # 主交付物
└── sources/
    └── references.md           # 全部信息来源
```

---

### 第八步：上传 GitHub + 复盘

**我做了什么：** Git push 到 `daihaojie02-ops/deep-camp-phase1-ai-barrier`，写 reflection.md 回答 8 个复盘问题，每个问题如实写——包括"我承认最薄弱的是多源信息交叉验证"和"LangGraph 没覆盖是因为回避学习曲线"这类诚实反思。

**AI 做了什么：** 执行 git 命令、生成 commit message。

---

## 工具选择原则

1. **不堆工具。** 5 个工具（gh + WebSearch + Claude Code + Bash + Playwright MCP），每个有不可替代的分工。Task 1 列的 Firecrawl 因需要 OAuth 认证未用——"核心工具"不是刻在石头上的
2. **优先用已熟悉的。** gh CLI 和 WebSearch 日常就在用，零上手成本
3. **有意识的边界划定。** 信息检索场景的边界是"调研和对比"，不做超出范围的工程实现
