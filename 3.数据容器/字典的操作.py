my_data = {"小红": 99, "小李": 56, "小刚": 88}
# 更新
my_data["小红"] = 100
# 新增
my_data["小张"] = 66
# 更新和新增都可以使用这个方法
print(my_data)

# 删除 接收value值
delete = my_data.pop("小红")
print(f"删除后为{my_data},小红分数{delete}")
# 清空
my_data.clear()
print(my_data)

# 获取全部key
my_data = {"小红": 99, "小李": 56, "小刚": 88}
en = my_data.keys()
print(en)
# 遍历字典 (两种一样的方法)
# 第一种方法
for x in en:
    print(f"姓名：{x}，成绩：{my_data[x]}")
# 第二种方法
for x in my_data:
    print(f"姓名：{x}，成绩：{my_data[x]}")
# 统计字典内的元素数量
num = len(my_data)
print(f"字典内的元素数量:{num}")
