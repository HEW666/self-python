my_list = [["a", 35], ["b", 20], ["c", 40]]

'''
# 排序,基于带名函数
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key, reverse=True)

'''


# 排序,基于 lambda 匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
