class Phone:
    __current_voltage = 1

    def __keep_single_core(self):
        print("让CPU单核运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            return "5G通话已开启"
        else:
            self.__keep_single_core()
            return "电量不足,并已设置单核运行"


phone = Phone()
print(phone.call_by_5g())
