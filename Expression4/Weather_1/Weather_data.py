import requests
from lxml import etree
import csv


def getWeather(url):  # 新建一个列表，将爬取的每月数据放入
    weather_info = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    }
    response = requests.get(url, headers=headers)
    # 预处理数据
    response_html = etree.HTML(response.text)
    # xpath提取所有的数据
    response_list = response_html.xpath("//ul[@class='thrui']/li")
    for li in response_list:
        day_weather_info = {}
        day_weather_info['date_time'] = li.xpath("./div[1]/text()")[0].split(' ')[0]
        # 最高温度
        high = li.xpath("./div[2]/text()")[0]
        day_weather_info['high'] = high[:high.find('℃')]
        low = li.xpath("./div[3]/text()")[0]
        day_weather_info['low'] = low[:low.find('℃')]
        # 天气
        day_weather_info['weather'] = li.xpath("./div[4]/text()")[0]
        weather_info.append(day_weather_info)
    return weather_info


weathers = []
# for 循环生成有顺序的1-12
for month in range(1, 13):  # 获取某一月的天气信息，三元表达式
    weather_time = '2024' + ('0' + str(month) if month < 10 else str(month))
    print(weather_time)
    url = f'https://lishi.tianqi.com/shanghai/{weather_time}.html'
    weather = getWeather(url)  # 爬取当前页面数据
    weathers.append(weather)  # 存到列表中
print(weathers)

# 写入数据
with open("weather.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['日期', '最高气温', '最低气温', '天气'])  # 写入列名
    # 用writerows一次写入多行
    writer.writerows(
        [list(day_weather_dict.values()) for month_weather in weathers for day_weather_dict in month_weather])