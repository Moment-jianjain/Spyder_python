import requests
from bs4 import BeautifulSoup
 
 
def get_cast_names(url1):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
    }
    # 发送请求获取网页内容
    response = requests.get(url1, headers=headers)
 
    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 查找主演信息所在的标签
    cast_section = soup.find_all("span", class_="attrs")
 
    # 提取主演名字
    cast_names1 = []
    if cast_section:
        for i in range(0, len(cast_section)):
            for cast_link in cast_section[i].find_all("a"):
                cast_names1.append(cast_link.get_text())
 
    return cast_names1
 
 
# 要爬取的豆瓣电影链接
url = "https://movie.douban.com/subject/24852545/"
 
# 调用函数获取主演名字列表
cast_names = get_cast_names(url)
 
# 打印主演名字列表
for name in cast_names:
    print(name)