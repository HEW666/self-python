# 打开两个文件对象
fr = open("bl.txt", "r", encoding="UTF-8")
fw = open("bl.txt.bak", "w", encoding="UTF-8")

# for循环写入
for line in fr:
    line_user = line.strip().split(",")
    if line_user[4] == "测试":
        continue
    fw.write(line)

# 关闭两个文件
fr.close()
fw.close()
