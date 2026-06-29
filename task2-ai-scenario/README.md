# Task 002 — AI 真实场景应用实验

> **戴昊杰 (DEEP007)** | 2026.06.29 | 信息检索场景
> **GitHub 仓库：** https://github.com/daihaojie02-ops/deep-camp-phase1-ai-barrier

## 任务一关联

我在 Task 1 中确定了"AI Agent 系统工程化能力"作为壁垒方向，并识别出"Multi-Agent 编排框架爆发"是关键信息差。Task 2 将这个观察升级为系统深挖——对 4 个主流框架进行检索、对比、判断。

**Task 1 → Task 2 → Task 3 递进链：**
- Task 1: 观察到 Multi-Agent 框架在爆发（列出星数，但不懂差异）
- Task 2: 系统深挖各框架定位/优劣/适用场景 → 做出有依据的选型决策
- Task 3: 凭报告结论，用选定的框架搭建 Agent 工作流雏形

## 14 项提交内容逐项核查

| # | 要求 | 对应文件 | ✓ |
|---|------|---------|---|
| 1 | README.md 总说明 | `README.md`（本文件） | ✅ |
| 2 | 任务一关联说明 | `task2-ai-scenario/task1_connection.md` | ✅ |
| 3 | 真实场景说明 | `task2-ai-scenario/scenario_description.md` | ✅ |
| 4 | 具体任务目标 | `task2-ai-scenario/task_goal.md` | ✅ |
| 5 | AI 工具选择与分工表 | `task2-ai-scenario/ai_workflow.md` | ✅ |
| 6 | 原始输入材料 | `task2-ai-scenario/input_materials.md` | ✅ |
| 7 | AI 工作流程记录 | `task2-ai-scenario/ai_workflow.md`（8 步走，含"我做了什么/AI做了什么/我如何判断/我做了哪些修改"） | ✅ |
| 8 | 至少 3 条关键 Prompt | `task2-ai-scenario/prompts.md` | ✅ |
| 9 | 至少 2 张过程截图 | `task2-ai-scenario/screenshots/`（3 张） | ✅ |
| 10 | 最终交付物 | `task2-ai-scenario/outputs/multi_agent_framework_report_2026H1.md` | ✅ |
| 11 | AI 前后效果对比 | `task2-ai-scenario/comparison.md` | ✅ |
| 12 | 个人修改痕迹 | `task2-ai-scenario/comparison.md`（4 处修改，含改前/改后/原因/效果） | ✅ |
| 13 | 任务二复盘 | `task2-ai-scenario/reflection.md`（8 问全部回答） | ✅ |
| 14 | GitHub 仓库链接 | https://github.com/daihaojie02-ops/deep-camp-phase1-ai-barrier | ✅ |

**零缺项。**

## 提交材料清单

| 文件 | 内容 | 对应要求 |
|------|------|---------|
| `task1_connection.md` | 任务一关联说明 — 4 问全部回答 | #2 |
| `scenario_description.md` | 真实场景说明 — 信息检索场景 6 问 | #3 |
| `task_goal.md` | 具体任务目标 — 可检验的 5 项标准 | #4 |
| `input_materials.md` | 原始输入材料 — 3 类材料 + 来源说明 | #6 |
| `ai_workflow.md` | AI 工具分工（5 工具 × 6 列） + 8 步工作流（我做了/AI做了/我如何判断/我做了哪些修改） | #5, #7 |
| `prompts.md` | 3 条关键 Prompt + 每条的使用心得和个人判断 | #8 |
| `comparison.md` | AI 前后效果对比（7 项 × 3 列表格） + 个人修改痕迹（4 处改前/改后/原因/效果） | #11, #12 |
| `reflection.md` | 任务二复盘（8 问全部回答） | #13 |
| `outputs/multi_agent_framework_report_2026H1.md` | 主交付物 — 8 章深度报告 | #10 |
| `sources/references.md` | 信息来源列表 — 全部可核查 | — |
| `screenshots/` | 3 张过程截图 | #9 |

## 核心结论

**Multi-Agent 框架选型推荐：CrewAI（首选）> Microsoft Agent Framework（备选）**

理由：我是 Multi-Agent 新手（自评 1/5），CrewAI 的角色隐喻最直观、Token 效率最高、学习曲线最低。选"能最快上手"的框架比选"理论上最好"的框架更重要。

## 个人判断声明

这份报告中的 GitHub 数据通过 `gh api` 实时抓取（2026.06.29），每个框架分析末尾的"我的判断"段落是我独立撰写的，不是 AI 生成。报告的结论基于我的技术水平、学习目标和 Task 3 计划——其他读者的最优选择可能不同。
