# 获取1-100的随机数字
import random
num = random.randint(1, 100)
# 定义一个变量，记录共猜了多少次
count = 0

flag = True
while flag:
    guess_num = int(input(f"请输入你猜的数字:"))
    count += 1
    if guess_num == num:
        print("猜对了")
        # 终止循环False
        flag = False
    else:
        if guess_num > num:
            print("你猜的大了")
        else:
            print("你猜的小了")

print(f"你总共猜了{count}次")
