import time
t = time.time()
print(t)

t = time.localtime(t)
print(t)

t = time.localtime()
print(f"今年是:{t.tm_year}年{t.tm_mon}月{t.tm_mday}日")
