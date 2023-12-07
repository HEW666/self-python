"""
取文件中 world 单词出现次数
"""
# 第一种方法 - 循环
with open('练习题.txt', 'r', encoding="UTF-8") as f:
    sum = f.read().replace("\n", " ")
    data = sum.split(" ")
    num = 0
    for x in data:
        if x == "world":
            num += 1
    print(data)
    print(f"出现次数为{num}")

# 第二种方法 - 统计
with open('练习题.txt', 'r', encoding="UTF-8") as f:
    sum = f.read().replace("\n", " ")
    data = sum.split(" ")
    num = data.count("world")
    print(f"出现次数为{num}")
