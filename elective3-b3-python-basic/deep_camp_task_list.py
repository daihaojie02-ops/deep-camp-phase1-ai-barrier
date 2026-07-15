# DEEP 营任务清单生成器
# DEEP营 Python 零基础入门 - 戴昊杰

tasks = [
    "完成 AI 壁垒方向卡",
    "完成 AI 真实场景应用实验",
    "完成 AI 工作流与 Agent 雏形任务",
    "完成 Claude Code 真实问题解决选修",
    "完成 Python 零基础入门选修",
    "整理 GitHub 仓库",
    "提交任务复盘"
]

print("=" * 40)
print("DEEP 营今日任务清单")
print("=" * 40)
for index, task in enumerate(tasks, 1):
    status = "[ ]"  # 未完成
    print(f"{index}. {status} {task}")

# 扩展：已完成的任务标记
print("\n----------- 已完成项 -----------")
completed = ["完成 AI 壁垒方向卡", "完成 AI 真实场景应用实验", "完成 AI 工作流与 Agent 雏形任务"]
for task in tasks:
    if task in completed:
        print(f"[DONE] {task}")
    else:
        print(f"[TODO] {task} (待完成)")

print("\n今日进度：", len(completed), "/", len(tasks))

# 这个工具解决的问题：
# 之前任务清单散落在各个文档里，每次都要靠记忆回想
# 现在一段 Python 代码集中展示，一目了然
#
# 未来可以升级的方向：
# 1. 把完成状态存到文件，每次打开能看到真实进度
# 2. 随机抽取一个任务督促自己
# 3. 用 Gradio 做一个简单的网页界面
