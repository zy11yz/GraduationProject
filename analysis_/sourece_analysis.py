import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import os

path = '..\\file'
os.chdir(path)
df = pd.read_csv('df.csv', encoding='gbk')


def src_anal():
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

    # 通过source聚类发现哪个信息源被引用的次数较多
    source_count = (df_time.loc[:, ['source', 'title']]).groupby(['source']).count()
    source_count_sort = source_count.sort_values(['title'], ascending=[0])
    # 观察哪些信息源被引用的较多
    print(source_count_sort['title'][:10])
    # 查看每个时间段发布次数，作图
    source_count_sort['title'][:10].plot()
    plt.show()

if __name__ == '__main__':
    src_anal()
