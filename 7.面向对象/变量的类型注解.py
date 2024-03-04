import random
# 基础数据类型注释
var_1: int = 10
var_2: str = "money"
var_3: bool = True


# 类对象类型注释
class Student:
    pass


stu: Student = Student()

# 基础容器类型注释
my_list: list = [1, 2, 3]

# 在注释中进行类型注解
var_4 = random.randint(1, 10)  # type: int
def func():
    return 10
ver_5 = func()  # type: int

