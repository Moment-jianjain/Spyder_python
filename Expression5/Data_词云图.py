# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 9:23
# @Author  : jianjian
# @File    : Data_词云图.py
# @Software: PyCharm
import csv
import jieba
import numpy as np
from wordcloud import WordCloud
from PIL import Image

def redData():
    # 打开CSV文件，读取其中的数据
    with open(r"iPad_CommentData.csv", "r", encoding="utf-8-sig") as file:
        # 获取csv的读取对象
        csvReader = csv.reader(file)
        # 返回每行数据的最后一个元素（评价内容）组成的列表
        return [item[-1] for item in csvReader]

def genWordCloud():
    # 获取所有评价数据
    commenList = redData()
    # 将所有评价拼接成一个字符串
    finalComments = ""
    for c in commenList:
        # 去除一些无关词汇
        c = c.replace("的", "").replace("了", "").replace("我", "")\
            .replace("是", "").replace("和", "").replace("就", "")
        finalComments += c
    # 使用jieba库对评论进行分词处理
    finalComments = " ".join(jieba.cut(finalComments))
    # 使用PIL库将图片读取为numpy数组格式
    image = np.array(Image.open(r"D:\Python Workspace\Test01\HTTP\NewSmallexpression\NewSmallexpression\Expression2\background.jpg"))
    # 实例化一个词云对象，设置字体、背景颜色和轮廓图片
    wordCloud = WordCloud(
        font_path="msyhbd.ttc",
        width=1700,
        height=1206,
        background_color="white",
        mask=image
    ).generate(finalComments)
    # 将生成的词云图保存为文件
    wordCloud.to_file(r"D:\Python Workspace\Test01\HTTP\NewSmallexpression\NewSmallexpression\Expression5\iPad.jpg")

if __name__ == '__main__':
    redData()
    genWordCloud()