"""
将MySQL数据写到TXT文件中
"""
from pymysql import Connection

# 连接数据库
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)
# 游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 执行SQL语句
cursor.execute("select * from orders")
# 接收数据
results = cursor.fetchall()
# 处理数据
f = open('MySQL数据.txt', 'w', encoding="UTF-8")
for x in results:
    dica = {"date": f"{x[0]}", "order_id": f"{x[1]}", "money": x[2], "province": f"{x[3]}"}
    # 输出数据
    f.write(str(dica))
    f.write("\n")

# 关闭数据库
conn.close()
