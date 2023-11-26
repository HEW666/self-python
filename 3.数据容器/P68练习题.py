data = ('周杰伦', 11, ['football', 'music'])

# 查询其年龄所在的下标位置
print(f"1. {data.index(11)}")

# 查询学生的姓名
print(f"2. {data[0]}")

# 删除学生爱好中的football
del data[2][0]
print(data)

# 增加爱好:coding到爱好list内
data[2].append("coding")
print(data)