import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Timeline

# 用pandas.read_csv()读取指点的excel文件
df = pd.read_csv('weather.csv', encoding='gb18030')
print(df['日期'])

df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x))
print(df['日期'])

# 新建一个月份数据，实际是将日期中的月份一项拿出来
df['month'] = df['日期'].dt.month
# 需要的数据，每个月中每种天气的出现次数
print(df['month'])

df_agg = df.groupby(['month', '天气']).size().reset_index()  # 返回dataframe groupby聚合对象，分组和统计的， size()能计算分组的大小
print(df_agg)

df_agg.columns = ['month', 'tianqi', 'count']
# 天气数据的形成  values numpy 数组 tolist 列表数据
print(df_agg[df_agg['month'] == 1][['tianqi', 'count']] \
      .sort_values(by='count', ascending=False).values.tolist())
# 画图 实例化一个时间序列的对象
timeline = Timeline()
timeline.add_schema(play_interval=1000)  # 设置播放时间间隔为1s

# 循环便利df_agg中['month']的唯一值
for month in df_agg['month'].unique():
    data = (
        df_agg[df_agg['month'] == month][['tianqi', 'count']]
        .sort_values(by='count', ascending=True)
        .values.tolist()
    )
    # 答应出时间，绘制柱状图
    bar = Bar()  # x轴是天气的名称，y轴是出现次数
    bar.add_xaxis([x[0] for x in data])
    bar.add_yaxis('', [x[1] for x in data])
    # 可视化图形样式设置
    bar.reversal_axis()  # 柱状图转向
    bar.set_series_opts(label_opts=opts.LabelOpts(position='right'))
    bar.set_global_opts(title_opts=opts.TitleOpts(title='上海2024年度每月天气的变化'))
    timeline.add(bar, f'{month}月')
timeline.render('weathers1.html')