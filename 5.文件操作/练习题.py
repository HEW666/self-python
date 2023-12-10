"""
取文件中 world 单词出现次数
"""
# 第一种方法 - 循环
with open('练习题.txt', 'r', encoding="UTF-8") as f:
    sum = f.read().split()
    num = 0
    for x in sum:
        if x == "world":
            num += 1
    print(sum)
    print(f"出现次数为{num}")

# 第二种方法 - 统计 - count
with open('练习题.txt', 'r', encoding="UTF-8") as f:
    num = f.read().count("world")
    print(f"出现次数为{num}")
