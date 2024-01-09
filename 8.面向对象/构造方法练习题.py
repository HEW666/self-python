"""
 学习笔记/Excalidraw/学习/8.面向对象/构造方法练习题.png
"""


class Student:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for i in range(1, 11):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    stu = Student(input("请输入学生的姓名:"), input("请输入学生的年龄:"), input("请输入学生的地址:"))
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{stu.name}，年龄{stu.age}，地址{stu.address}】")
