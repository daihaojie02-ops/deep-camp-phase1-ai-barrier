# 基础练习二：列表与循环
# DEEP营 Python 零基础入门 - 戴昊杰

tools = ["ChatGPT", "Claude Code", "Codex", "Python", "GitHub"]
print("我正在学习的工具：")
for tool in tools:
    print("-", tool)

# 我的 DEEP 营任务版本：
deep_tasks = [
    "完成 AI 壁垒方向卡 (001)",
    "完成 AI 真实场景应用实验 (002)",
    "完成 AI 工作流与 Agent 雏形任务 (003)",
    "完成 Claude Code 真实问题解决选修 (B2)",
    "完成 Python 零基础入门选修 (B3)",
    "整理 GitHub 仓库",
    "提交任务复盘"
]
print("\n我的 DEEP 营任务清单：")
for task in deep_tasks:
    print("[ ]", task)

# 我的理解：
# 列表 = 用方括号 [] 把多个数据放在一起，像一个购物清单
# for 循环 = 按顺序逐个取出列表里的每一项，重复执行相同的操作
# 循环的价值 = 不用复制粘贴 print 语句，10个任务一行循环搞定
