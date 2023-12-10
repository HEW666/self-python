"""
Python的缓冲机制和自动关闭文件的特性
不一定要调用flush()和close()方法来保存数据
但在某些情况下，为了确保数据的完整性，建议使用这两个方法。
"""
import time

f = open('写入文件.txt', 'w', encoding="UTF-8")
# write写入
f.write("你好世界")  # 关闭文件自动保存
time.sleep(1000)

# flush刷新
f.flush()  # 将内存写入硬盘

# close关闭
f.close()  # 内置flush功能
