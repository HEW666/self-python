import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("数据/疫情.json", "r", encoding="UTF-8")  # 读取数据文件
data = f.read()  # 获取全部文数据
f.close()  # 关闭文件
# 将json转换为Python字典
data_dict = json.loads(data)
# 从字典中取出各省的数据
province_data_list = data_dict['areaTree'][0]['children']
data_list = []  # 绘图所需要的数据
for province_data in province_data_list:
    province_name = province_data["name"]  # 各省名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_confirm))


# 创建图形对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局配置,定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100~999人", "color": "#5cb3cc"},
            {"min": 1000, "max": 4999, "label": "1000~4999人", "color": "#1ba784"},
            {"min": 5000, "max": 9999, "label": "5000~9999人", "color": "#bec936"},
            {"min": 10000, "max": 99999, "label": "10000~99999人", "color": "#887322"},
            {"min": 100000,  "label": "1000000+", "color": "#b7511d"},  # 最大没有上限,可以不写
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")
