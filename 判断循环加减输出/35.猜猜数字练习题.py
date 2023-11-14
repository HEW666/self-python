num = 100
if int(input("请输入猜想的数字：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜：")) == num:
    print("猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("猜对了")
else:
    print("全部猜错了，我想的是：%s" % num)
