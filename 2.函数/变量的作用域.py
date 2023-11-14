num = 200
gay = 200
"""
    全局变量数值为 200
    局部变量数值为 100
"""


def data_1():
    num = 100
    print(num)


def data_2():
    global gay  # 设置为全局变量
    gay = 100
    print(gay)


print(num)  # 全局变量
print(gay)  # 全局变量
data_1()  # 输出函数 data_1
data_2()  # 输出函数 data_2
print(f"已把局部设置为全局{gay}")  # 需引用变量所在的函数，否则将输出全局
