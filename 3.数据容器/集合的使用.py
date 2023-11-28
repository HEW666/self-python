# 添加新元素
data = {"天心网络", "过客网络", "畫未网络"}
data.add("原神启动")
print(data)

# 移除指定元素
data.remove("原神启动")
print(data)

# 清空元素
data.clear()
print(data)

# 两个集合的差集:得到一个新集合，h1比对h2，保留h1
h1 = {1, 5, 6}
h2 = {1, 2, 3}
sun = h1.difference(h2)
print(sun)

# 删除集合2中的存在的元素：修改集合1，集合2不变
j1 = {1, 2, 6}
j2 = {1, 3, 3}
j1.difference_update(j2)
print(j1)

# 得到一个新集合，含两个集合的全部元素：原有的集合不变
x1 = {1, 2, 6}
x2 = {1, 3, 3}
sun = x1.union(x2)
print(sun)  # 去除重复元素 {1, 2, 3, 6}

# len()得到一个整数，元素数量：去除重复
z1 = {1, 2, 3, 4, 5, 6}
print(len(z1))

# for循环：由于顺序不能保证，所以不能用while
for a in z1:
    print(a)
