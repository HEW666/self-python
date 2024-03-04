class User:
    name = None
    age = None

    def say_hi(self):
        print(f"Hi大家好,我是{self.name},今年{self.age}岁.")


use = User()
use.name = "张三"
use.age = 28
use.say_hi()
