def list_while():
    my_list = [1, 2, 3, 4, 5]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        index += 1
        print(f"列表的元素有{element}")


def list_for():
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表的元素有{element}")


list_while()

list_for()
