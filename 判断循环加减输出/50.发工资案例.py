money = 10000
for i in range(1, 21):
    import random
    performance = random.randint(1, 10)
    if performance < 5:
        print(f"员工{i}，绩效分{performance}，低于5分，不发工资，下一位。")
        continue
    if money >= 1000:
        money -= 1000
        print(f"向员工{i}发放1000元，账户余额剩余{money}")
    else:
        print(f"账户余额不足，余额为：{money} ，请下个月领取")
        break
