import json
from pyecharts.charts import Line

# 打开文件
f_us = open("数据/美国.txt", "r", encoding="UTF-8")
# 获取全部内容
us_data = f_us.read()
# 去除不符json规范的内容
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
# json转python字典
us_dict = json.loads(us_data)
# 获取 trend 值
trend_data = us_dict['data'][0]['trend']
# 获取日期数据，用于X轴（到314下标结束）
x_data = trend_data['updateDate'][:314]
# 获取日期数据，用于Y轴（到314下标结束）
y_data = trend_data['list'][0]['data'][:314]

# 生成图表
