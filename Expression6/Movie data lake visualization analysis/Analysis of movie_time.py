# -*- coding: utf-8 -*-
# @Time    : 2024/7/3 9:11
# @Author  : jianjian
# @File    : Analysis of movie_time.py
# @Software: PyCharm
import pandas as pd  #读取csv文件以及操作数据
from lxml import etree #解析html库
from pyecharts.charts import *  #可视化库

data=pd.read_csv('电影数据.csv', encoding='utf-8')

####################                              ################
####################<<<<<电影时长数据柱形图可视化>>>>>>################
####################                              ################

# 电影时长   去除分钟和,号这个 转为int  然后再转为列表  只提取20条数据，总共100条
move_time = data['电影时长'].apply(lambda x: x.replace('分钟', '').replace(',', '')).astype('int').tolist()[0:20]
# print(move_time)

# 电影名   只提取20条数据
move_name = data['电影名'].tolist()[0:20]
# print(move_name)

# 创建Bar实例
Bar_obj = Bar()

# 添加x轴数据标题
Bar_obj.add_xaxis(move_name)

# 添加y轴数据
Bar_obj.add_yaxis('电影时长数据（单位：分钟）', move_time)

# 设置标题
Bar_obj.set_global_opts(title_opts={'text': '电影时长数据柱形图可视化'})

# 显示图表
Bar_obj.render("电影时长数据柱形图可视化.html")
#
####################                              ################
####################<<<<<电影时长数据折线图可视化>>>>>>################
####################                              ################
# 去除分钟和,号这个 转为int  然后再转为列表  只提取25条数据
move_time = data['电影时长'].apply(lambda x: x.replace('分钟', '').replace(',', '')).astype('int').tolist()[0:25]
# print(move_time)

# 电影名   只提取25条数据
move_name = data['电影名'].tolist()[0:25]
# print(move_name)

# 创建Bar实例
Bar_obj = Line()

# 添加x轴数据标题
Bar_obj.add_xaxis(move_name)

# 添加y轴数据
Bar_obj.add_yaxis('电影时长数据（单位：分钟）', move_time)

# 设置标题
Bar_obj.set_global_opts(title_opts={'text': '电影时长数据折线图可视化'})

# 显示图表
Bar_obj.render("电影时长数据折线图可视化.html")
