# 关键 Prompt 记录

## Prompt 1：信息检索启动

**使用工具：** Claude Code（WebSearch 触发）

**内容：**
```
搜索 "CrewAI vs MetaGPT vs AutoGen vs Microsoft Agent Framework comparison 2026 multi-agent"，
关注框架对比、社区讨论、最新动态
```

**作用：** 把模糊的"我想了解一下 Multi-Agent 框架"需求转化为一次系统检索。这个 Prompt 的关键在于**要求对比而非介绍**——如果只搜单个框架名称，返回的会是官方 README；搜对比才能挖出社区的真实评价和取舍逻辑。

**我的判断：** 这个搜索词的选择本身就是一种信息素养——用"vs"串联关键词比用"review""tutorial"更容易找到有判断力的内容。

---

## Prompt 2：GitHub 数据批量抓取

**使用工具：** Claude Code（Bash `gh api` 触发）

**内容：**
```
用 gh api 分别获取以下 4 个仓库的 stars/forks/open_issues/updated_at/language/license/topics：
- crewAIInc/crewAI
- geekan/MetaGPT
- microsoft/autogen
- microsoft/agent-framework
输出 JSON 格式的数据
```

**作用：** 把"打开 4 个 GitHub 页面看数据"变成一次 API 调用 + 结构化输出。**时间从 20 分钟降到 2 分钟**——而且 API 返回的数据比页面爬虫准确。

**我的判断：** 这个 Prompt 的价值不在于"高级"，而在于"意识到可以用 API 而不是浏览器"。很多人在做调研时第一反应是打开 GitHub 页面一个一个人工看——这就是 AI 使用意识的分水岭。

---

## Prompt 3：生成结构化对比报告

**使用工具：** Claude Code（直接对话）

**内容（摘要）：**
```
基于以下数据，生成一份"2026 H1 Multi-Agent 框架生态深度报告"：
[4 个框架的 GitHub API 数据 + WebSearch 返回的对比文章摘要]

要求：
1. 生态全景概览（含 2026 关键变化）
2. 逐框架分析（每个框架的定位、技术特点、优劣势）
3. 横向对比决策矩阵（表格）
4. 每个框架包含"我的判断"段落——不是官方介绍再写一遍，而是我个人的选择逻辑
5. 最终推荐 + 学习路线
6. 承认信息盲区

注：输出初稿，我会补充个人判断和修改
```

**作用：** 把分散的 API 数据和搜索文章整合为一份统一框架的报告。关键约束是**第 4 条——"我的判断"段落**——这迫使 AI 不是在写百科，而是在按我的分析框架组织信息。

**我的判断：** 这个 Prompt 的核心设计是"先给数据 → 再定结构 → 最后强求个人声音"。如果反向操作（先让 AI 自由发挥 → 再改），结果会是一篇 AI 风格的泛泛介绍，没有任何个人判断。

---

## Prompt 使用心得

1. **好的 Prompt ≠ 复杂的 Prompt。** 三条 Prompt 都很直白，关键是把"要什么数据、什么结构、什么语气"说清楚
2. **Prompt 之间是有逻辑链的。** Prompt 1 搜什么 → Prompt 2 拿到数据 → Prompt 3 整合成报告，不是三条独立的指令
3. **"个人判断"不能靠 Prompt 生成。** AI 可以写"我认为"但内容空洞——真正的个人判断是我改出来的，不是 AI 生成的
