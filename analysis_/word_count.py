import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import os
import jieba
mpl.use('Agg')
path = '..\\file'
os.chdir(path)
df = pd.read_csv('df.csv', encoding='gbk')
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def word_cnt():
    # 词频统计
    contentAll = ""
    for item in df['detail_fulltext']:
        contentAll = contentAll + item
    # 查看一共有多少字
    print('此次分析的数据中一共有 %d 个字。' % len(contentAll))

    # 分词
    segment = []
    segs = jieba.cut(contentAll)
    for seg in segs:
        if len(seg) > 1 and seg != '\r\n':
            segment.append(seg)

    # 去停用词
    words_df = pd.DataFrame({'segment': segment})
    ancient_chinese_stopwords = pd.Series(['我们', '没有', '可以', '什么', '还是', '一个', '就是', '这个',
                                           '怎么', '但是', '不是', '之后', '通过', '所以', '现在',
                                           '如果', '为什么', '这些', '需要', '这样', '目前', '大多',
                                           '时候', '或者', '这样', '如果', '所以', '因为', '这些',
                                           '他们', '那么', '开始', '其中', '这么', '成为', '还有',
                                           '已经', '可能', '对于', '之后', '10', '20', '很多', '其实',
                                           '自己', '当时', '非常', '表示', '不过', '出现', '认为',
                                           '利亚', '罗斯', '" "'])

    words_df = words_df[~words_df.segment.isin(ancient_chinese_stopwords)]

    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"number": np.size})
    words_stat = words_stat.reset_index().sort(columns="number", ascending=False)

    words_stat_sort = words_stat.sort_values(['number'], ascending=[0])
    sns.set_color_codes("muted")
    sns.barplot(x='segment', y='number', data=words_stat_sort[:11], color="b")
    plt.ylabel('出现次数')
    plt.title("前10个最常见词统计")
    plt.show()

if __name__ == '__main__':
    word_cnt()
