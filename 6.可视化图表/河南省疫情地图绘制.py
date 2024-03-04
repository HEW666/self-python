import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("数据/疫情.json", "r", encoding="UTF-8")  # 读取数据文件
data = f.read()  # 获取全部文数据
f.close()  # 关闭文件
# 将json转换为Python字典
data_dict = json.loads(data)

cities_list = data_dict['areaTree'][0]['children'][3]['children']

data_list = []  # 绘图所需要的数据
for city_data in cities_list:
    city_name = city_data["name"] + "市"  # 各市名称
    city_confirm = city_data["total"]["confirm"]  # 确诊人数
    data_list.append((city_name, city_confirm))

data_list.append(("济源市", 5))
map = Map()
map.add("河南省疫情分布", data_list, "河南")


map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 199, "label": "100~199人", "color": "#5cb3cc"},
            {"min": 200, "max": 299, "label": "200~299人", "color": "#c02c38"},
        ]
    )
)
# 绘图
map.render("河南疫情分布.html")
