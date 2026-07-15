# B3 Claude Code 辅助学习记录

> 戴昊杰 (DEEP007) | 2026.07.15

## 记录 1：让 Claude Code 解释 Python 对 AI 学习的作用

**我向 Claude Code 输入了什么：**
```
我是一名 DEEP 营学员，正在做 Python 零基础入门任务。
请帮我解释：Python 和 AI 学习之间到底有什么关系？
为什么不能只停留在用 ChatGPT 聊天，还需要学一点 Python？
重点面向非编程背景的学习者，不要用太多术语。
```

**Claude Code 帮我完成了什么：**
解释了 Python 是 AI 时代的"执行工具"——AI 聊天帮你思考，Python 帮你执行。给出了具体场景：自动化重复操作、数据分析、Agent 工具开发。帮我理清了"学 Python 不是学编程，是学一种和 AI 配合使用的执行能力"。

**我是否运行了结果：** 不需要运行——这是解释性的回答。

**我是否理解代码：** 不涉及代码。

**我自己修改了什么：** 把 Claude Code 的解释整理成了 B3 why_python.md——加入了 Task 002（Firecrawl→Claude→人工判断）的真实使用经验。

---

## 记录 2：让 Claude Code 生成基础练习代码

**我向 Claude Code 输入了什么：**
```
请帮我生成 4 个 Python 练习文件，放在 D:\CC\DEEP\第一期\ai壁垒001\elective3-b3-python-basic\ 目录下：

1. exercise_1_print_variable.py —— print 和变量练习
2. exercise_2_list_loop.py —— 列表和 for 循环练习
3. exercise_3_function.py —— 简单函数练习
4. deep_camp_task_list.py —— DEEP 营任务清单生成器（综合练习）

要求：
- 每个文件用中文注释解释代码
- 用 DEEP 营相关的示例（不要用"Hello World"这种无意义例子）
- 代码简单易懂，每行不超过 80 字符
- 在文件末尾加一个"我的理解"注释块，用我自己的话解释关键概念
```

**Claude Code 帮我完成了什么：** 生成了 4 个完整的 Python 文件，包含中文注释、"我的理解"块、DEEP 营相关示例数据。

**我是否运行了结果：** ✅ 已运行——4 个文件全部成功运行。

**我是否理解代码：** 
- print/变量/列表/循环 ✅ 完全理解
- enumerate() 函数 ⚠️ 会查文档才能理解
- f-string（f"..."） ⚠️ 大致理解，能改参数

**我自己修改了什么：**
1. 修复了 emoji 字符在 Windows GBK 编码下的乱码问题（把 "✅" 改成 "[DONE]"）
2. 调整了 deep_camp_task_list.py 中的任务列表——换成我自己的真实任务
3. 在"我的理解"注释中用自己的话重写了概念解释

---

## 记录 3：让 Claude Code 帮我修改报错

**我向 Claude Code 输入了什么：**
```
运行 exercise_2_list_loop.py 时报错：
UnicodeEncodeError: 'gbk' codec can't encode character '✅' in position 0

这是什么原因？怎么修复？
```

**Claude Code 帮我完成了什么：** 解释了 GBK 编码不支持 emoji 字符，建议替换为 ASCII 字符或添加 UTF-8 编码声明。

**我是否运行了结果：** ✅ 修改后重新运行成功。

**我是否理解代码：** ✅ 理解了——Windows 终端默认 GBK 编码，emoji 不在 GBK 字符集中，需要转为纯文本。

**我自己修改了什么：** 选择把 "✅" 改为 "[DONE]"（ASCII 安全），而不是添加 UTF-8 编码声明——因为我想让代码在任何 Windows 终端都能跑，不依赖编码设置。
