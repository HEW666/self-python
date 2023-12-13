"""
# 所有用法
try:
    f = open("1.txt", "r", encoding="UTF-8")  # 可能存在的异常
except Exception as e:
    f = open("1.txt", "w", encoding="UTF-8")  # 如果文件不存在执行
    print(e)  # 异常
else:
    print("没有异常")  # 没有异常执行
finally:
    f.close()  # 有没有异常都执行关闭文件

# 异常写法
try:
    f = open("1.txt", "r", encoding="UTF-8")  # 可能存在的异常
except FileNotFoundError as e:
    print(f"出现了错误，代码：{e}")
"""
try:
    # f = open("1.txt", "r", encoding="UTF-8")
    print(name)
except (FileNotFoundError, NameError) as e:
    print(f"出现了错误，代码：{e}")
