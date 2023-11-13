def temperature(data):
    print("欢迎来到学校")
    if data <= 37.5:
        print(f"你的体温是：{data},体温正常请进")
    else:
        print(f"你的体温是：{data},需要隔离")


temperature(37.6)
