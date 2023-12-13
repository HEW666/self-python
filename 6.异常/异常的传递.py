def fun01():
    print("这是fun01开始")
    num = 1 / 0
    print("这是fun01结束")


def fun02():
    print("这是fun02开始")
    fun01()
    print("这是fun02结束")


def main():
    try:
        fun02()
    except Exception as e:
        print(f"异常{e}")


main()
