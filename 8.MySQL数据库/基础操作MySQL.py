from pymysql import Connection

# 构建数据库的连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
print(conn.get_server_info())  # 返回数据库版本

conn.select_db("world")  # 选择数据库
cursor = conn.cursor()  # 使用cursor类
cursor.execute("select * from student")  # 查询数据库指令

results = cursor.fetchall()  # 接受返回数据

for r in results:
    # 遍历输出
    print(r)

conn.close()
