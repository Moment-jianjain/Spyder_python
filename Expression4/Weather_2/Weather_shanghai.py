# – coding: gbk –
import requests
from bs4 import BeautifulSoup
import pandas
import pandas as pd
from matplotlib import pyplot as plt


# def get_data(weather_url):
#     rseponse = requests.get(weather_url)
#
#     html = rseponse.content.decode('gbk')
#     soup = BeautifulSoup(html, 'html.parser')
#
#     tr_lsit = soup.find_all('tr')
#     # 寻找tr标签下的所有内容
#
#     print(tr_lsit)
#     dates, conditions, temp, fengxiang = [], [], [], []
#     for data in tr_lsit[1:]:
#         sub_data = data.text.split()
#         # ['2024年06月30日', '雷阵雨', '/雷阵雨', '27℃', '/', '32℃', '东风', '1-2级', '/东风', '1-2级']
#
#         dates.append(sub_data[0])
#         conditions.append(''.join(sub_data[1:3]))
#         temp.append(''.join(sub_data[3:6]))
#         fengxiang.append(''.join(sub_data[6:9]))
#         # join函数连接字符串
#
#     # 数据保存
#     _data = pandas.DataFrame()
#     _data['日期'] = dates
#     _data['天气情况'] = conditions
#     _data['气温'] = temp
#     _data['风向'] = fengxiang
#
#     return _data
#     # print(_data)
#     # _data.to_csv('anqing.csv',index=False,encoding='gbk')
#     # 获取数据并保存csv格式，进行下面的数据分析
#
#
# # 定义成函数形式进行封装
# data_month_1 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202405.html')
# data_month_2 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202406.html')
# data_month_3 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202407.html')
#
# # 使用drop参数来避免将旧索引添加为列：
# data = pandas.concat([data_month_1, data_month_2, data_month_3]).reset_index(drop=True)
# # 导出csv表格
# data.to_csv('shanghai.csv', index=False, encoding='utf-8')
# 读表
data1 = pd.read_csv('shanghai.csv')

# 画图
# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号的乱码问题
plt.rcParams['axes.unicode_minus'] = False
# 读表
datalsit = pandas.read_csv('shanghai.csv', encoding='utf-8')

# 数据处理
# 利用split分裂字符串‘/’取出最高最低气温
datalsit['最低气温'] = datalsit['气温'].str.split('/', expand=True)[0]
datalsit['最高气温'] = datalsit['气温'].str.split('/', expand=True)[1]
# 取出温度中的℃符号
datalsit['最低气温'] = datalsit['最低气温'].map(lambda x: int(x.replace('℃', '')))
datalsit['最高气温'] = datalsit['最高气温'].map(lambda x: int(x.replace('℃', '')))

dates = datalsit['日期']
highs = datalsit['最高气温']
lows = datalsit['最低气温']

# 画图
# 设置可视化图形规格
fig = plt.figure(dpi=128, figsize=(10, 6))
# 线形图的线条颜色粗细调整
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# 线条下方覆盖为蓝色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# 图表格式
# 设置图标的图形格式
plt.title('2024上海市5-7月天气情况', fontsize=24)
plt.xlabel('日期', fontsize=12)
# x轴标签倾斜  默认30度 可通过rotation=30改变
fig.autofmt_xdate()
plt.ylabel('气温', fontsize=12)
# 刻度线样式设置
plt.tick_params(axis='both', which='major', labelsize=10)
# 修改刻度 数据每10组显示1个
plt.xticks(dates[::10])
# 绘制图形的代码...
# 保存图形到本地
plt.savefig('2024上海市5-7月天气情况.png')


# 绘制风向扇形图
# 提取出风向的各类型占比  数据清洗
fengxiang = data1['风向'].value_counts()
fengxiang = fengxiang[fengxiang.values > 3]
plt.figure(figsize=(15, 5))
# 保住饼图是圆 不是默认椭圆
plt.axes(aspect='equal')
plt.pie(x=fengxiang.values,
        labels=fengxiang.index,
        autopct="%.2f%%",
        radius=1
        )
plt.title('风向占比')
plt.savefig('2024上海市5-7月风向占比.png')

# 直接显示
# plt.show()