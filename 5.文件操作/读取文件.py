# 打开文件 - open()
import time

f = open('示范文件.txt', 'r', encoding="UTF-8")
print(type(f))

# 读取文件 - read()
print(f"读取10个字节的结果：{f.read(17)}")
# print(f"读取全部内容的结果：{f.read()}")  # 接着读取

# 读取文件 - readLines() - 读取全部行，得到列表
# print(f"{f.readlines()}")

# 读取文件 - readLine() - 读取一行
print(f"{f.readline()}")
print(f"{f.readline()}")

# 文件对象 - 一次循环得到一行数据
for line in f:
    print(line)

# 关闭文件对象 - close()
time.sleep(10)  # 休眠(秒)
f.close()  # 未关闭不可删除重命名文件
print("——————————————————————")
# with 语法 - 自动关闭文件
with open('示范文件.txt', 'r', encoding="UTF-8") as f:
    for lite in f:
        print(lite)
