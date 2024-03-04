class Phone:
    IMEI = None
    producer = "tx"

    def call_by_5g(self):
        print("使用5G网络进行通话")


# 定义子类,复写父类成员
class MyPhone(Phone):
    producer = "hw"

    def call_by_5g(self):
        print("开启CPU单核模式")
        # 方式1
        print(f"父类的厂商是{Phone.producer}")
        Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式")


phone = MyPhone()
print(phone.producer)
phone.call_by_5g()
