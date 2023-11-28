data = "itheima itcast boxuegu"
num = data.count("it")
print(f"it出现次数{num}")  # it出现的次数

name = data.replace(" ", "|")
print(f"替换后{name}")  # 将空替换为|

sum = name.split("|")
print(sum)  # 输出列表
