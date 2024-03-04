class Student:
    name = None

    def say_hi(self, msg):
        print(f"大家好,我是{self.name},{msg}")


stu = Student()
stu.name = "李四"
stu.say_hi("有事报我名")

stu1 = Student()
stu1.name = "王五"
stu1.say_hi("多多关照")
