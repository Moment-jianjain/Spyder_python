# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 20:44
# @Author  : jianjian
# @File    : Language_Kshihua.py
# @Software: PyCharm
from matplotlib import pyplot as plt
import pandas as pd
import pynimate as nim   ###前面这个包需要Requires-Python >=3.9;

plt.rcParams['font.family'] = 'SimHei'  # 显示中文
df = pd.read_csv("Language_data.csv").set_index("time")


def post_update(ax, i, datafier, bar_attr):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.set_facecolor("#001219")


# Canvas类是动画的基础
cnv = nim.Canvas(figsize=(12, 7), facecolor="#001219")
# 使用Barplot模块创建一个动态条形图, 插值频率为10天 post_update美化格式 n_bars最大显示多少条默认为10
bar = nim.Barplot(df, "%Y-%m-%d", "10d", xticks=False, post_update=post_update, rounded_edges=True, grid=False,
                  n_bars=5)
# 编程热度值
bar.set_title(title="01-24年编程语言热度的占比变化(%)", size=20, color="w", weight=800)
# 使用了回调函数, 返回以年、月为单位格式化的datetime
bar.set_time(callback=lambda i, datafier: datafier.data.index[i].strftime("%Y,%m"), color="w", y=0.1)
bar.set_bar_annots(color="w", size=30)  # 显示热度占比值
bar.set_xticks(colors="w", length=0, labelsize=20)
bar.set_yticks(colors="w", labelsize=20)
bar.set_bar_border_props(edge_color="black", pad=0.1, mutation_aspect=1, radius=0.2, mutation_scale=0.6)
# 将条形图添加到画布中
cnv.add_plot(bar)
cnv.animate()
# plt.show()
cnv.save("file", 24, "mp4")	# 保存视频
# 两种格式存储，git和mp4
#cnv.save("Language_hot", 24, "gif")
