def list_while():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = []
    num = 0
    while num < len(data):
        digit = data[num]
        num += 1
        if digit % 2 == 0:
            sum.append(digit)
    print(f"while从列表{data}取出的偶数{sum}")


def list_for():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = []
    for digit in data:
        if digit % 2 == 0:
            sum.append(digit)
    print(f"for从列表{data}取出的偶数{sum}")


# 通过while循环取出data里的偶数
list_while()

# 通过for循环取出data里的偶数
list_for()