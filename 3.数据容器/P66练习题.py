# 1.定义这个列表，并用变量接收它
ege = [21, 25, 21, 23, 22, 20]

# 2.追加一个数字31，到列表的尾部
ege.append(31)
print(ege)

# 3.追加一个新列表[29，33，30]，到列表的尾部
ege1 = [29, 33, 30]
ege.extend(ege1)
print(ege)
# 4.取出第一个元素(应是:21)
num = ege.pop(0)
print(num)
# 5.取出最后一个元素(应是:30)
num = ege[-1]
print(num)
# 6.查找元素31，在列表中的下标位置
num = ege.index(31)
print(num)
