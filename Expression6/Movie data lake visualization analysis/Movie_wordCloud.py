# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 21:19
# @Author  : jianjian
# @File    : Movie_wordCloud.py
# @Software: PyCharm
import pandas as pd  #读取csv文件以及操作数据
from pyecharts.charts import *  #可视化库
import jieba
#from win32comext.shell.demos.IActiveDesktop import opts

data=pd.read_csv('电影数据.csv', encoding='utf-8')
#print(data)

title_list = []

for name in data['电影名']:

    # 进行精准分词
    lcut = jieba.lcut(name, cut_all=False)
    #     print(lcut)

    for i in lcut:
        #         print(i)

        # 去除无意义的词

        # 打开停用词表文件
        file_path = open('停用词表.txt', encoding='utf-8')#使用jieba分词，nltk词频统计,这里的停用此表.txt可以自己创建一个 里面放无意义的字，比如：的、不是、不然这些,每个字独占一行即可

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
print(most_common_words)  # 结果：


####                        #####
######## <<<<词云可视化>>> ########
####                        #####

# 创建一个 WordCloud类（词云） 实例
word_cloud = WordCloud()

# 添加数据和词云大小范围    add('标题', 数据, word_size_range=将出现频率最高的单词添加到词云图中，并设置单词的大小范围为 20 到 100。)
word_cloud.add('词云图', most_common_words, word_size_range=[20, 100])

# # 渲染词云图
word_cloud.render()

# 也可以生成html文件观看
word_cloud.render('电影数据词云图.html')



# 设置全局选项，包括标题
#word_cloud.set_global_opts(title_opts=opts.TitleOpts(title='电影数据词云图'))













