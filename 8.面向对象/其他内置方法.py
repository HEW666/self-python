class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student类对象:,name:{self.name},age:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


# stu1 = Student("周杰伦", 36)
# stu2 = Student("周杰伦", 36)


# print(stu1 < stu2)  # 成立
# print(stu1 > stu2)  # 不成立

# print(stu1 <= stu2)  # 成立
# print(stu1 >= stu2)  # 不成立

stu1 = Student("周杰伦", 36)
stu2 = Student("周杰伦", 36)
print(stu1 == stu2)  # 成立
print(stu1)
print(str(stu1))
