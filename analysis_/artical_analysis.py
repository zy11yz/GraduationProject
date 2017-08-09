import pandas as pd
import os
path = '..\\file'
os.chdir(path)
df = pd.read_csv('df.csv', encoding='gbk')


def artical_anls():
    # 查看评论最多的一篇comment的文章名
    df_comment = df.sort_values('comment_count', ascending=[0])
    # 删除原来的索引,重新建立索引
    df_comment = df_comment.reset_index(drop=True)
    return(df_comment.iloc[0])

    return(df_comment['comment_count'].head(3))
    # print(df_comment.head(3))

if __name__ == '__main__':
    artical_anls()
