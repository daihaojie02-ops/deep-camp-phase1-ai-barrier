# 🧠 Personal Knowledge Management Toolkit — "你的第二个大脑"

> DEEP 营内部工程项目 | 个人知识体系搭建 | 戴昊杰

## 一句话

**用 Markdown + Git + Python 脚本 + Claude Code 搭建个人知识管理系统，所有笔记永不丢失，AI 自动关联。**

## 为什么做这个项目

我在 DEEP 营写了很多笔记——任务复盘、工具使用心得、避坑规则、平台配置……它们分散在 `deep-camp-phase1/` 和 `.claude/memory/` 两个地方。当我想找"之前那个关于 Agent 的笔记"时，只能靠记忆翻文件。

这个工具解决的就是 **"我知道我写过，但我找不到"** 的问题。

## 为什么这么选

| 选择 | 为什么选它 | 帮我省了什么 | 别人可能忽略的用法 |
|------|-----------|-------------|-------------------|
| **Markdown** | 纯文本，任何编辑器都能打开。100年后也能读。不绑定 Notion/Obsidian/飞书 | 不用学任何新工具，写代码时顺便写笔记 | Markdown 的 YAML frontmatter 可以做结构化元数据——标题/标签/日期/描述——这就是轻量数据库 |
| **Git** | 每次修改都有记录，换电脑 `git clone` 即可 | 不用手动备份，不用注册任何云盘账号 | `git log --stat` 可以看到知识增长的轨迹——哪个月写得最勤、什么主题最多 |
| **Python CLI** | 一键索引/搜索/统计，不需要打开任何 GUI | 比手动翻文件夹快 100 倍 | 可以和 Claude Code 的 Skills 集成——让 AI 自动调 `km search` 来找答案 |
| **无平台依赖** | 不绑定第三方服务，不会因为平台倒闭/收费而丢失数据 | 不需要每月付费，不需要担心服务关停 | 知识库本身就是 Git 仓库 — `git push` 到 GitHub 就是天然的多端同步 |

## 技术架构

```
km.py                          # 主工具 (320+ lines)
├── parse_frontmatter()        # YAML 元数据解析
├── extract_title()            # 智能标题提取 (frontmatter > h1 > filename)
├── extract_tags()             # 标签提取 (手动 + 自动检测)
│
├── cmd_index()                # 结构化索引生成
│   └── 输出: 按类别/标签分组 + Tag Cloud
├── cmd_search()               # 全文搜索 + 上下文展示
├── cmd_stats()                # 统计面板 (字数/大小/标签分布)
├── cmd_backup()               # Git 自动备份 + 提交信息生成
├── cmd_init()                 # 新知识库初始化 + 模板
└── run_demo()                 # 一键演示
```

## 实际效果

运行 `python km.py demo` 对我的真实笔记库（9个文件）的扫描结果：

### Index — 结构化索引
```
📚 Personal Knowledge Base Index
Total Notes: 9

📁 root/ (9 notes)
  ├─ agent-reach              #github #agent #python
  ├─ auth-to-aplusmax-strategy #github
  ├─ DEEP营任务提交 — 评审教训   #github #deep-camp #agent
  ├─ workflow-yaml-fix-pipeline #prompt #api #agent
  ├─ xfyun-agent-platform     #prompt #api #mcp
  └─ ...

🏷 Tag Cloud: #github(5) #agent(5) #api(5) #deep-camp(3) #workflow(3)
```

### Search — "Agent" 搜到 5 篇笔记，精确到行号
### Stats — 9 篇笔记 / 1328 字 / 11 个唯一标签
### Backup — Git 提交信息自动生成

## 复利效应

- **4 年大学 × 职业生涯** = 数千条笔记 → 变成了可搜索的知识资产
- **期末复习** = 搜 3 个关键词
- **面试准备** = 看过自己所有的思考
- **写论文** = 搜关键词 → 找到所有相关笔记 → 串成论证

## 改变什么

> "我知道我写过但找不到了" → "搜 3 个关键词，全部出来"

## 验证：运行 demo 完整输出

见 [demo/demo_output.txt](demo/demo_output.txt)

## 文件清单

```
knowledge-kit/
├── km.py              # 核心工具 (320+ lines Python)
├── README.md          # 本文件
└── demo/
    └── demo_output.txt # 完整演示输出
```

---
*Built with Claude Code — 2026-07-15*
