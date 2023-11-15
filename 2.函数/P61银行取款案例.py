money = 5000000
name = input("你的姓名是：")


def bank_deposit(deposit):
    global money
    money = money + deposit
    print("————————————————存款————————————————")
    print(f"{name}，您好，您存款：{deposit} 元。success")
    print(f"{name}，您好，您余额还有：{money} 元")
    bank_help()


def bank_withdrawal(withdrawal):
    global money
    money = money - withdrawal
    print("————————————————取款————————————————")
    print(f"{name}，您好，您取款：{withdrawal} 元。success")
    print(f"{name}，您好，您取款还有：{money} 元")
    bank_help()


def bank_balance():
    print("————————————————查询余额————————————————")
    print(f"{name}，您好，您的余额剩余：{money} 元")
    bank_help()


def bank_help():
    print("————————————————主菜单————————————————")
    print(f"{name}，您好，欢迎来到银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    count = int(input("请输入你的选择："))
    if count == 1:
        bank_balance()
    elif count == 2:
        deposit = int(input("请问您要存多少钱："))
        bank_deposit(deposit)
    elif count == 3:
        withdrawal = int(input("请问您要取多少钱："))
        bank_withdrawal(withdrawal)
    else:
        exit()


bank_help()
