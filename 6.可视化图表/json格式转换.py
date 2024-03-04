import json

data_list = [{"name": "张三", "ege": "20"}, {"name": "李四", "ege": "24"}, {"name": "王五", "ege": "25"}]
# 把Python数据转为json数据
data = json.dumps(data_list, ensure_ascii=False)
print(type(data))
print(data)

# 把json数据转为Python数据
data = json.loads(data)
print(type(data))
print(data)
