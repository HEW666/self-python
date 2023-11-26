data = ("菜鸟", "菜鸟", True, "菜鸟")
# type类型
print(f"data元组的类型{type(data)}")

# len数量
print(f"data元组的数量{len(data)}")

# count统计
print(f"data元素的数量是{data.count("菜鸟")}")

# index索引
print(f"data的元素的索引{data.index(True)}")

# while
num = 0
while num < len(data):
    print(f"while输出{data[num]}")
    num += 1

# for
for x in data:
    print(f"for输出{x}")
