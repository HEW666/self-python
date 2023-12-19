# 文件处理
def print_file_info(file_name):
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f.read())
        f.fileno()
    except FileNotFoundError as a:
        print(f"文件不存在：{a}")


def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.close()

