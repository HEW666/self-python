from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

# 读取数据
f = open("C:/Users/ken/Desktop/python/7.可视化图表/数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转字典
# 定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

timeline = Timeline({"theme": ThemeType.LIGHT})
# 排序年份
sorted_year_list = sorted(data_dict.keys())

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 去除本年份前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # X轴数据-国家
        y_data.append(country_gdp[1] / 100000000)  # Y轴数据-gdp
    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转X轴Y轴
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )

    timeline.add(bar, str(year))

# 创建时间线对象
timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 绘图
timeline.render("1960-2019全球GDP前8.html")
