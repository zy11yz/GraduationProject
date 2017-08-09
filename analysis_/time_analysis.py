import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import copy
import time
import os
path = '..\\file'
os.chdir(path)
df = pd.read_csv('df.csv', encoding='gbk')


def time_anls():
    mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    font_size = 10  # 字体大小
    fig_size = (12, 9)  # 图表大小
    mpl.rcParams['font.size'] = font_size  # 更新字体大小
    mpl.rcParams['figure.figsize'] = fig_size  # 更新图表大小

    # 按照日期的字符串进行排序
    df_time = df.sort_values('date', ascending=[0])
    # 删除原来的索引,重新建立索引
    df_time = df_time.reset_index(drop=True)

    df_time1 = copy.deepcopy(df_time)
    df_time1['time'] = [time.strftime("%Y-%m-%d %H", time.strptime(str(postTime), '%Y-%m-%d %H:%M:%S')) for postTime in
                        df_time1['date']]
    time_count = (df_time1.loc[:, ['time', 'title']]).groupby(['time']).count()
    time_count.index = pd.to_datetime(time_count.index)
    # 查看每个时间段发布次数，作图
    time_count['title'][:70].plot()
    plt.show()

if __name__ == '__main__':
    time_anls()
