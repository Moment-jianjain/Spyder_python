#request
#bs4
import csv
import requests#获取response对象
from bs4 import BeautifulSoup#获取解析对象
#接收url，解析url
def getCommentByPage(url):
    #1.添加请求头（程序模拟用户浏览器，向服务器发送请求）
    headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    #2.请求url；获得response对象
    response=requests.get(url,headers=headers)
    #3.判断是否获取到
    if response.status_code==200:
        #创建bs4解析对象
        soup=BeautifulSoup(response.content.decode("utf-8"),"lxml")
        #5.获取存放所有评价的标签对象
        #print(soup)
        comments=soup.find_all("div",attrs={"class":"comment-item"})
        #print(comments)
        for c in comments:
            #目标：用户 时间 评分
            cominfo = c.find("span",attrs={"class":"comment-info"})
            #爬取评价人网名
            name = cominfo.find("a").text
 
            if(len(cominfo.select("span"))==3):
                # 是否看过
                look =cominfo.select("span")[0].text
                #评分
                start =cominfo.select("span")[1].get("title")
                #时间
                time =cominfo.select("span")[2].get("title")
            else:
                # 是否看过
                look = cominfo.select("span")[0].text
                # 评分
                start="null"
                # 时间
                time = cominfo.select("span")[1].get("title")
            #对应评价
            short =c.find("span",attrs={"class","short"}).text
            print("{},{},{},{}".format(look, start, time,short))
            comlist.append([look,start,time,short])
 
 
 
    else:
        print("请求失败！")
 
 
def writeComment(comlist):
    with open(r"D:\Python Workspace\Test01\HTTP\NewSmallexpression\NewSmallexpression\Expression2\Move.csv","w",newline="",encoding="utf-8-sig") as file:
        csvWrite =csv.writer(file)
        csvWrite.writerows(comlist)
if __name__ == '__main__':
    print("get")
    #定义全局变量
    comlist=[]
    for i in range(0,10):
        baseurl = "https://movie.douban.com/subject/30170847/comments?status=P".format(i*20)
        getCommentByPage(baseurl)
    for item in comlist:
        print(item)
    writeComment(comlist)