# for循环输出99乘法表
for c in range(1, 10):

    for x in range(1, c + 1):
        print(f"{x}*{c}={x * c}\t", end='')

    print()
