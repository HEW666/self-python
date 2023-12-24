# 导包，导入Line的功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 得到折线图对象
line = Line()
# 添加X轴数据
line.add_xaxis(["中国", "美国", "日本"])
# 添加Y轴数据
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置项 et_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title="GPD展示", pos_left="center", pos_bottom="1%"),  # 标题,左侧的距离,下侧的距离
    legend_opts=LegendOpts(is_show=True),  # 图例显示，默认显示
    toolbox_opts=ToolboxOpts(is_show=True),  # 工具箱是否显示
    visualmap_opts=VisualMapOpts(is_show=True),  # 视觉映射是否显示
)

# 通过render方法，将代码生成为图像
line.render()
