# 查询字符所在位置 查找不到将会报错
data = ["home", "auth", "red"]
index = data.index("auth")
print(f"auth的下标是：{index}")

# 在指定下标位置插入新元素
data.insert(2, "hello")
print(f"插入后的列表：{data}")

# 在列表的尾部追加单个新元素
data.append("apple")
print(f"追加后的列表：{data}")

# 追加一批新元素
data1 = {1, "black", "world"}
data.extend(data1)
print(f"追加一批后的列表：{data}")

# 删除元素
print("————————————")
# 方法1 ：del 列表[下标]
data = ["home", "auth", "hello", "red"]
del data[3]  # 删除red
print(f"删除元素后列表：{data}")

# 方法2 ：列表.pop(下标)
data = ["home", "auth", "hello", "red"]
element = data.pop(3)
print(f"取出来的元素列表:{data},取出来的元素是{element}")

# 匹配删除元素
data = ["home", "auth", "hello", "red", "apple", 1, "black", "world"]
data.remove("apple")
print(f"通过remove方法删除apple后，列表：{data}")

# 列表清空
data.clear()
print(f"清空后的列表：{data}")

# 统计列表
data = ["home", "auth", "hello", "auth", "apple", "auth", "world"]

# 统计列表内某元素的数量
count = data.count("auth")
print(f"列表中auth的数量是：{count}")

# 统计列表中全部的元素数量
count = len(data)
print(f"列表中元素数量总共有{count}")
