# 文件处理

def print_file_info(file_name):
    """
    将文件内容输出
    :param file_name:
    :return: 文件内容
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f.read())
    except FileNotFoundError as a:
        print(f"文件不存在：{a}")
    finally:
        if f:  # 如果变量是None，表示False，如果有任何内容，就是True
            f.close()  # 有内容就执行


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()
