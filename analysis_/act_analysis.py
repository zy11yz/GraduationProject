import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
path = '..\\file'
os.chdir(path)
df = pd.read_csv('df.csv', encoding='gbk')


def act_anls():
    # 构建作图格式
    channel_id = ['c2', 'c3', 'c5', 'c7', 'c9']
    tuple_c = []
    for j in range(len(channel_id)):
        # print(tuple([like['like'].iloc[j], comment_count['comment_count'].iloc[j], up['up'].iloc[j]]))
        tuple_c.append(tuple([df['like'].iloc[j], df['comment_count'].iloc[j], df['up'].iloc[j]]))
    # 设置柱形图宽度
    bar_width = 0.15
    index = np.arange(3)
    # c2为体育，c3为娱乐，c5为财经，c7为军事，c9为社会，
    channel_name = ['体育', '娱乐', '财经', '军事', '社会']
    count_name = ['like', 'comment_count', 'up']
    # 绘制c2
    rects1 = plt.bar(index, tuple_c[0], bar_width, color='#0072BC', label=channel_name[0])
    # 绘制c3
    rects2 = plt.bar(index + bar_width, tuple_c[1], bar_width, color='#4E1C2D', label=channel_name[1])
    # 绘制c5
    rects3 = plt.bar(index + bar_width * 2, tuple_c[2], bar_width, color='g', label=channel_name[2])
    # 绘制c7
    rects4 = plt.bar(index + bar_width * 3, tuple_c[3], bar_width, color='#ED1C24', label=channel_name[3])
    # 绘制c9
    rects5 = plt.bar(index + bar_width * 4, tuple_c[4], bar_width, color='c', label=channel_name[4])
    # X轴标题
    plt.xticks(index + bar_width, count_name)
    # Y轴范围
    # plt.ylim(ymax=100, ymin=0)
    # 图表标题
    plt.title(u'like,comment,up 对比')
    # 图例显示在图表下方
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5)

    # 添加数据标签
    def add_labels(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
            # 柱形图边缘用白色填充，纯粹为了美观
            rect.set_edgecolor('white')

    add_labels(rects1)
    add_labels(rects2)
    add_labels(rects3)
    add_labels(rects4)
    add_labels(rects5)
    plt.show()

if __name__ == '__main__':
    act_anls()
