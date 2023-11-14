def log(age):
    if age >= 18:
        return None
    else:
        print("你未满18")

ren = log(18)
if not ren:  # 进入if表示是None值
    print(type(ren))
