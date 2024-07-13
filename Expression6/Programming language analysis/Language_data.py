# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 20:42
# @Author  : jianjian
# @File    : Language_data.py
# @Software: PyCharm
import pandas as pd
import requests
import re

url = "https://www.tiobe.com/tiobe-index/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
htmlText = response.text

d = dict()
datas = re.findall('{name : .*?}', htmlText)
dates = re.findall('Date.UTC\((.*?)\)', datas[0])
# 时间
date_list = []
for date in dates:
    t = date.replace(" ", "").split(",")
    t[1] = str(int(t[1]) + 1)
    y_m_d = "-".join(t)
    date_list.append(y_m_d)
d["time"] = date_list

for i in datas:
    name = re.findall("name : '(.*?)'", i)[0]
    value_list = []
    values = re.findall('\), (.*?)]', i)
    for value in values:
        value_list.append(eval(value))
    if len(value_list) != len(date_list):   # 有些编程语言缺少近20年数据，为了方便直接不要
        print(name, len(value_list))
        continue
    d[name] = value_list

df = pd.DataFrame(d).set_index("time")
df.to_csv("Language_data.csv")
