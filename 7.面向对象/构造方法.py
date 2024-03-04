class Student:

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("创建一个类对象")


stu = Student("周杰伦", 31, "1300086371")
print(stu.name)
print(stu.age)
print(stu.tel)
