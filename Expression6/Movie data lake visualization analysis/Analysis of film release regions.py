# -*- coding: utf-8 -*-
# @Time    : 2024/7/3 9:08
# @Author  : jianjian
# @File    : Analysis of film release regions.py
# @Software: PyCharm
import jieba
import pandas as pd  #读取csv文件以及操作数据
from pyecharts.charts import *  #可视化库

data=pd.read_csv('电影数据.csv', encoding='utf-8')

title_list = []
# 遍历电影上映地这一列
for name in data['电影上映地']:

    # 进行精准分词
    lcut = jieba.lcut(name, cut_all=False)
    #     print(lcut)

    for i in lcut:
        #         print(i)

        # 去除无意义的词

        # 打开停用词表文件
        file_path = open('停用词表.txt', encoding='utf-8')

        # 将读取的数据赋值给stop_words变量
        stop_words = file_path.read()

        # 遍历后的值 如果没有在停用词表里面 则添加到net_data列表里面
        if i not in stop_words:
            title_list.append(i)
# print(title_list)


# 计算词语出现的频率
from nltk import FreqDist  # 该模块提供了计算频率分布的功能

# FreqDist对象将计算net_data中每个单词的出现频率，,并将结果存储在freq_list中
freq_list = FreqDist(title_list)
print(freq_list)  # 结果：FreqDist 有1321个样本和5767个结果

# 该方法返回一个包含最常出现单词及其出现频率的列表。将该列表赋值给most_common_words变量。
most_common_words = freq_list.most_common()
print(most_common_words)  # 结果：('单人这个词',出现185次)

# 电影名 使用列表推导式来提取most_common_words中每个元素中的第一个元素，即出现次数，然后将它们存储在一个新的列表中
map_data_title = [count[0] for count in most_common_words]
print(map_data_title)

# 电影数
map_data = [count[1] for count in most_common_words]
print(map_data)

# 获取map_data_title的长度，决定循环次数，赋值给遍历i 在通过下标取值
result = [[map_data_title[i], map_data[i]] for i in range(len(map_data_title))]
print(result)

# 创建Pie实例
chart = Pie()

# 添加标题和数据   radius=['圆形空白处百分比','色块百分比（大小）'] 可不写
chart.add('电影上映数饼图（单位：个）', result, radius=['50%', '60%'])

# 显示
chart.render("电影上映地区饼状图占比分析.html")