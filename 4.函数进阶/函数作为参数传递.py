def user_help(compute):
    result = compute(3, 4)  # 函数1
    print(f"compute的类型{type(compute)}")
    print(f"相加等于{result}")


def compute(x, y):  # 函数1
    return x + y


user_help(compute)
