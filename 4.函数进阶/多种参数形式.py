def user_han(name, age, gender="男孩"):  # 默认传参
    print(f"姓名：{name} 年龄：{age} 性别：{gender}")


# 第一种：位置传参
user_han("小明", 21)
# 第二种：关键字传参（位置可以随意）（但传参必须在最后）
user_han("小明", 22, gender="男孩")


# 第三种：不定长参数
# 1.位置不定长-元组 *（规范：args）
def user_han(*args):
    print(f"类型{type(args)} 元组{args}")


user_han(1, "你好", True, "世界")


# 2.关键字不定长-字典 ** （规范：kwargs）
def user_han(**kwargs):
    print(f"类型{type(kwargs)} 字典{kwargs}")


user_han(name="张三", age=25, gender="男孩")
