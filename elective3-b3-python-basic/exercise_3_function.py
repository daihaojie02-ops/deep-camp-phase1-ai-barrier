# 基础练习三：简单函数
# DEEP营 Python 零基础入门 - 戴昊杰

def make_task(task_name):
    return "今天需要完成的任务是：" + task_name

result = make_task("完成 DEEP 营 Python 零基础入门任务")
print(result)

# 尝试把自己的任务传进去：
print(make_task("提交 B1 信息壁垒报告"))
print(make_task("完成 B2 Claude Code 任务"))
print(make_task("GitHub push 所有选做任务"))

# 我的理解：
# 函数 = 一段可重复使用的代码块，给它输入 → 它处理 → 返回输出
# def 是用来"定义"（创建）一个函数的关键字
# make_task 这个函数接受一个任务名，拼上一句前缀，然后返回完整句子
# 函数的价值 = 写一次逻辑，无限次复用——调3次就是3行，调100次也只写1次逻辑
