import requests
from lxml import etree
from urllib.request import urlretrieve
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

params = {
	"start":int(input('请输入电影开始数: ')),#控制电影开始数
	"limit":int(input('请输入返回电影数: '))#控制返回多少部电影
}
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

response = requests.get(url,headers=headers,params=params)

item = {} #用于存放json数据
f = open("movie.json", "a", encoding="utf-8")
res = response.json()
for i in res:
	title = i['title']
	actors = i['actors']
	item["电影名称"] = title
	item["演员列表"] = actors
	#print(title,actors)
	f.write(json.dumps(item,ensure_ascii=False,indent=4)+",\n")
f.close()
1