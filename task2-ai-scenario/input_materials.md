# 原始输入材料

## 1. 我输入给 AI 的原始材料是什么？

本次任务有三类原始输入材料：

### 材料 A：GitHub 仓库实时数据

通过 `gh api` 直接从 GitHub API 抓取的 4 个仓库元数据：

**CrewAI:**
```
stars: 54,539 | forks: 7,639 | open_issues: 579
language: Python | license: MIT
description: "Framework for orchestrating role-playing, autonomous AI agents"
topics: [agents, ai, ai-agents, aiagentframework, llms]
updated: 2026-06-29
```

**MetaGPT:**
```
stars: 69,104 | forks: 8,819 | open_issues: 136
language: Python | license: MIT
description: "The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming"
topics: [agent, gpt, llm, metagpt, multi-agent]
updated: 2026-06-29
```

**AutoGen:**
```
stars: 59,345 | forks: 8,942 | open_issues: 922
language: Python | license: CC-BY-4.0
description: "A programming framework for agentic AI"
topics: [agentic, autogen, llm-agent, llm-framework]
updated: 2026-06-29
```

**Microsoft Agent Framework:**
```
stars: 11,744 | forks: 1,978 | open_issues: 674
language: Python | license: MIT
description: "A framework for building, orchestrating and deploying AI agents and multi-agent workflows"
topics: [agent-framework, multi-agent, orchestration, python, dotnet]
updated: 2026-06-29
```

### 材料 B：WebSearch 搜索结果

搜索关键词：`"CrewAI vs MetaGPT vs AutoGen vs Microsoft Agent Framework comparison 2026 multi-agent"`

返回的对比文章列表（部分）：
- futureagi.com — "Best Multi-Agent Frameworks 2026: 7 Platforms Ranked"
- softwareseni.com — "Navigating the Multi-Agent Framework Landscape"
- cnblogs.com — "AI Agent 框架全景指南：LangChain、AutoGen、CrewAI 深度对比（2026）"
- dev.to — "Microsoft Agent Framework 1.0: Build AI Agents in .NET and Python"

### 材料 C：Task 1 自身产出

- `information_gap.md`（信息差观察——Multi-Agent 框架爆发这一条）
- `personal_barrier_map.md`（自评矩阵——Multi-Agent 编排 1/5）

## 2. 这些材料来自哪里？

| 材料 | 来源 | 获取方式 |
|------|------|---------|
| GitHub 仓库数据 | github.com 各仓库主页 | `gh api` CLI 工具 |
| 对比文章 | futureagi.com, softwareseni.com, cnblogs.com 等 | WebSearch 内置工具 |
| Task 1 产出 | D:\CC\DEEP\第一期\ai壁垒001\task1-ai-barrier\ | 本地文件读取 |

## 3. 哪些是我自己提供的？

- **Task 1 的全部分析内容**（信息差观察、自评矩阵）——这是我之前的产出，不是外部数据
- **搜索关键词的选择**——我决定搜什么、怎么搜（用 "vs" 串联对比而非单独搜每个框架）
- **分析维度的定义**——我决定从"学习曲线、Token 效率、场景灵活性、长期维护"等维度对比，而不是照搬别人的对比框架

## 4. 哪些来自外部资料？

- GitHub API 返回的 star/fork/issue 数据（实时抓取）
- WebSearch 返回的对比文章（外部作者）

## 5. 如果有外部资料，是否附上来源？

✅ 全部来源已记录在 `sources/references.md` 中，包含 URL 和访问日期。每个外部数据点都可以被独立核查。

---

## 原始材料的意义

> 这次任务不是"让 AI 凭空生成一份 Multi-Agent 框架分析"。我给了 AI 三类明确的原始输入：实时 API 数据 + 社区对比文章 + 我自己的 Task 1 分析。AI 的作用是把这些分散的材料组织成统一的对比框架，但**数据是我找的、维度是我定的、最终判断是我做的。**
