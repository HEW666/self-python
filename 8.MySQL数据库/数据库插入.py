from pymysql import Connection

# 构建数据库的连接
conn = Connection(
    host="localhost",   # 主机名（IP）
    port=3306,          # 端口
    user="root",        # 账户
    password="123456",  # 密码
    autocommit=True     # 自动提交（确认）
)
# 获取到游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 执行sql
cursor.execute("insert into student values(22, '赵明', 27, '男')")
# 通过commit确认。
# 也可以在 Connection 里写入 autocommit=True
# conn.commit()
# 关闭链接
conn.close()
