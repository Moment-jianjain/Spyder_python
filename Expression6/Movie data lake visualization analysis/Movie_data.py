# – coding: gbk –
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 21:13
# @Author  : jianjian
# @File    : Movie_data.py
# @Software: PyCharm
import requests,csv  #请求库和保存库
import pandas as pd  #读取csv文件以及操作数据
from lxml import etree #解析html库
from pyecharts.charts import *  #可视化库

# 请求的网址
url = 'https://ssr1.scrape.center/page/1'

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# 发起请求，获取文本数据
reponse = requests.get(url, url, headers=headers)
print(reponse)

# 创建csv文件
with open('电影数据.csv', mode='w', encoding='utf-8', newline='') as f:
    # 创建csv对象
    csv_save = csv.writer(f)

    # 创建标题
    csv_save.writerow(['电影名', '电影上映地', '电影时长', '上映时间', '电影评分'])

    for page in range(1, 11):  # 传播关键1到10页的页数

        # 请求的网址
        url = 'https://ssr1.scrape.center/page/{}'.format(page)
        print('当前请求页数：', page)

        # 请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        response = requests.get(url, url, headers=headers, verify=False)
        print(response)

        html_data = etree.HTML(response.text)

        # 获取电影名
        title = html_data.xpath(
            '//div[@class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]/a/h2/text()')

        # 获取电影制作地
        gbs = html_data.xpath(
            '//div[@class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]/div[2]/span[1]/text()')

        # 获取电影时长
        time = html_data.xpath('//div[@class="m-v-sm info"]/span[3]/text()')

        # 获取电影上映时间
        move_time = html_data.xpath(
            '//div[@class="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16"]/div[3]/span/text()')

        # 电影评分
        numder = html_data.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()')

        for name, move_gbs, times, move_times, numders in zip(title, gbs, time, move_time, numder):
            print('电影名：', name, '  电影上映地址：', move_gbs, '   电影时长：', times, '   电影上映时间：', move_times,
                  '   电影评分:', numders)
            # name,move_gbs,times,move_times,numders

            # 写入csv文件
            csv_save.writerow([name, move_gbs, times, move_times, numders])