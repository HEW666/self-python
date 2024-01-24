class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            return "5G开启"
        else:
            return "5G关闭，使用4G网络"

    def call_by_5g(self):
        print(self.__check_5g())
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
