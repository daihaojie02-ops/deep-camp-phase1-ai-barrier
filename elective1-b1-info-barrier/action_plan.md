# B1 对我个人的行动建议

> 戴昊杰 (DEEP007) | 2026.07.15

## 1. 这次信息整理后，我最应该关注哪个方向？

**AI 编程工具（特别是 Claude Code）的持续追踪 + MCP Server 的质量筛选。**

理由：
- 这两个方向直接支撑我的 Multi-Agent 壁垒（Task 001 的定义）
- 我已经有使用基础（Task 002/003 大量用了 Claude Code + Firecrawl MCP）
- 它们不是"新东西要学"，而是"已经在用的东西要深化"

不选 Agent 框架作为主追踪方向——框架竞争格局在 2026 年快速变化，但作为个人学习者，我已经选了 CrewAI，短期内不需要切换。

## 2. 我现在最应该学习或尝试哪个工具？

**Context7 MCP Server。**

Task 003 测试运行中我标注了"Context7 是我的最大缺口"——它解决了"AI 用过期 API 文档生成代码"的问题。Claude Code + Context7 = 代码生成时自动查最新文档 → 消灭 API 幻觉。

具体行动：本周末把 Context7 加入 CLAUDE.md 的 MCP 配置。

## 3. 哪些信息虽然热门，但暂时不适合我？

| 热门方向 | 为什么暂时不适合 |
|---------|---------------|
| Microsoft Agent Framework（刚 GA） | 我不用 Azure/.NET 栈——不符合我的工具生态 |
| Google ADK | 不用 GCP——且非 GCP 使用体验差（社区反馈） |
| Mastra | TypeScript 优先——我是 Python 方向 |
| AI 语音克隆/数字人（B8） | 和我的 Multi-Agent 壁垒方向不直接相关 |
| AI 视频生成（B7） | 同上——除非有具体比赛/项目需求 |

**不与我的工具栈和个人壁垒方向共振的，即使热门也先不碰。**

## 4. 哪些方向可能帮助我参加比赛或做项目？

| 方向 | 比赛/项目场景 |
|------|------------|
| CrewAI + Claude Code | Agent 类比赛——用 CrewAI 做 Multi-Agent 编排、Claude Code 辅助 Python 开发 |
| MCP Server 集成 | 任何需要 AI 调用外部工具的比赛——搜网页+截图+数据处理+GitHub |
| LangGraph | 如果比赛要求复杂状态管理的 Agent——LangGraph 比 CrewAI 更适合有环/持久化的流程 |

## 5. 哪些方向未来可能与创业有关？

| 方向 | 创业可能性 | 前提条件 |
|------|----------|---------|
| 垂直领域 Agent 开发（如"技术选型 Agent"） | 中——Task 003 reflection 已提 | 需要验证真实需求——有人愿意为"帮我选技术栈"买单吗？ |
| MCP Server 开发 | 中——如果发现某个高频场景没有好的 MCP Server | 需要 Python 能力进一步提升（B3 只是第一步） |
| AI 编程降门槛工具 | 低——竞争太激烈（Claude Code/Cursor/Codex 都在抢） | 除非找到非常特定的细分需求 |

## 6. 我下一步准备做什么？

**短期（本周）：**
1. ✅ B1 信息壁垒报告完成（本文件）
2. 🔄 B2 Claude Code 真实问题任务（做一个 DEEP 营任务展示网页）
3. 🔄 B3 Python 零基础入门（4 个练习 + DEEP 营清单生成器）

**中期（第二期）：**
1. 把 Context7 加入 MCP 配置
2. 用 Task 004（AI 辅助自动化）把 TechScout 工作流做成可运行脚本
3. 评估是否值得深入学习 LangGraph（看 Task 005/006 的需求）

**长期（第三期+）：**
1. 追踪 MCP 生态——至少每月扫一次新 Server
2. 持续用 Claude Code 做实际项目（不是练习，是真实产出）
3. 如果 Python 能力进阶到可以做 MCP Server，考虑做一个"DEEP 营任务管理 MCP Server"
