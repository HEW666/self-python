import random
num = random.randint(1, 10)
print("你有三次机会猜测1-10以内的数字")
digit = int(input("请输入第一次要猜的数字："))
if digit == num:
    print("恭喜你，第一次就猜对了")
else:
    if digit > num:
        print("你猜的数大了")
    else:
        print("你猜的数小了")

    digit = int(input("请输入第二次要猜的数字："))

    if digit == num:
        print("恭喜你，第二次猜对")
    else:
        if digit > num:
            print("你猜的数大了")
        else:
            print("你猜的数小了")

        digit = int(input("请输入最后一次要猜的数字："))

        if digit == num:
            print("恭喜你，最后一次猜对")
        else:
            print("没有机会了，游戏失败")
