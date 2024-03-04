from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()

# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("江苏省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]
# 添加数据
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#8fb2c9"},
            {"min": 100, "max": 199, "label": "100-199", "color": "#2486b9"},
            {"min": 200, "max": 299, "label": "200-299", "color": "#e2e7bf"},
            {"min": 300, "max": 399, "label": "300-399", "color": "#fa5d19"},
            {"min": 400, "max": 499, "label": "400-499", "color": "#f2481b"},
        ]

    )
)
# 绘图
map.render()
