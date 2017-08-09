import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import jieba
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator
mpl.use('Agg')
path = '..\\file'
os.chdir(path)
df = pd.read_csv('df.csv', encoding='gbk')
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def word_cld():
    # 去停用词
    segment = []
    words_df = pd.DataFrame({'segment': segment})
    ancient_chinese_stopwords = pd.Series(['我们', '没有', '可以', '什么', '还是', '一个', '就是', '这个',
                                           '怎么', '但是', '不是', '之后', '通过', '所以', '现在',
                                           '如果', '为什么', '这些', '需要', '这样', '目前', '大多',
                                           '时候', '或者', '这样', '如果', '所以', '因为', '这些',
                                           '他们', '那么', '开始', '其中', '这么', '成为', '还有',
                                           '已经', '可能', '对于', '之后', '10', '20', '很多', '其实',
                                           '自己', '当时', '非常', '表示', '不过', '出现', '认为',
                                           '利亚', '罗斯', '" "'])

    contentAll = ""
    for item in df['detail_fulltext']:
        contentAll = contentAll + item

    wordlist_after_jieba = jieba.cut(contentAll, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    bimg = np.array(Image.open('..\\pic\\tree1.jpg'))
    my_wordcloud = WordCloud(
        background_color='white',  # 设置背景颜色
        mask=bimg, # 设置背景图片
        max_words=250,  # 设置最大现实的字数
        stopwords=ancient_chinese_stopwords,  # 设置停用词
        font_path='C:\\Windows\\Fonts\\Microsoft YaHei UI\\msyh.ttc',  # 设置字体格式
        max_font_size=150,  # 设置字体最大值
        random_state=25,  # 设置有多少种随机生成状态，即有多少种配色方案
        scale=1.5
    ).generate(wl_space_split)
    # 根据图片生成词云颜色
    image_colors = ImageColorGenerator(bimg)
    my_wordcloud.recolor(color_func=image_colors)

    # 以下代码显示图片
    plt.figure(figsize=(12, 9))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    word_cld()
