string = type("hello worlf")
int = type(555)  # 括号内填写内容
float = type(-96.3)
"""
print(string)
print(int)
print(float)
"""
# 以上是三种类型
print("————————")
print(type(565))
name = "325"
strint_name = type(name)
print(strint_name)
print("————————")
# ——————————

intxs = int(name)  # 转整数
print(type(intxs), intxs)

strzx = str(3.145)  # 转字符串
print(type(strzx), strzx)

flana = float("3")  # 转浮点数
print(type(flana), flana)

print(int(5.16))  # 浮点数转整数
