name = "万过薪月，员序程马黑来，nohtyp学"
# 获得 黑马程序员

# 第一种方法：先倒序后切片
name1 = name[::-1]
name2 = name1[9:14]
print(name2)

# 第二种方法：先切片后倒序
name3 = name[5:10][::-1]
print(name3)

# 第三种方法：先用split成列表选中字符串，后用replace把来替换掉，再倒序
name4 = name.split("，")[1].replace("来", "")[::-1]
print(name4)
