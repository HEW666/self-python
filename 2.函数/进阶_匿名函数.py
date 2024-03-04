# 示例1
def add(compute):
    result = compute(2, 2)
    print(f"{result}")


add(lambda x, y: x + y)

# 示例2
addition = lambda x, y: x + y

print(addition(3, 5))
