import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 打开文件
f_us = open("数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()

f_jb = open("数据/日本.txt", "r", encoding="UTF-8")
jb_data = f_jb.read()

f_in = open("数据/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

# 去除不符json规范的内容
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jb_data = jb_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

us_data = us_data[:-2]
jb_data = jb_data[:-2]
in_data = in_data[:-2]

# json转python字典
us_dict = json.loads(us_data)
jb_dict = json.loads(jb_data)
in_dict = json.loads(in_data)

# 获取 trend 值
us_trend_data = us_dict['data'][0]['trend']
jb_trend_data = jb_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于X轴（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jb_x_data = jb_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取日期数据，用于Y轴（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jb_y_data = jb_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表 - 构建折线图对象
line = Line()
# 添加X轴数据 - X轴是公用的，所以使用一个国家数据即可
line.add_xaxis(us_x_data)
# 添加Y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jb_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%"),
)
# 调用 render 方法,生成图表
line.render()
# 关闭文件对象
f_us.close()
f_jb.close()
f_in.close()
