import pandas as pd
import matplotlib as mpl
import os
mpl.use('Agg')

path = '..\\file'
os.chdir(path)

channel_id = ['c2', 'c3', 'c5', 'c7', 'c9']
df_name = ['df_c2', 'df_c3', 'df_c5', 'df_c7', 'df_c9']

def pro_data():
    # 读取体育新闻
    file_dir = '%s\\%s.csv' % (channel_id[0], channel_id[0])
    print('正在读取' + file_dir)
    df_c2 = pd.read_csv(file_dir, encoding='gbk')
    df_c2 = df_c2.drop(df_c2.columns[0], axis=1)
    df_c2['setType'] = 2
    # 读取娱乐新闻
    file_dir = '%s\\%s.csv' % (channel_id[1], channel_id[1])
    print('正在读取' + file_dir)
    df_c3 = pd.read_csv(file_dir, encoding='gbk')
    df_c3 = df_c3.drop(df_c3.columns[0], axis=1)
    df_c3['setType'] = 3
    # 读取财经新闻
    file_dir = '%s\\%s.csv' % (channel_id[2], channel_id[2])
    print('正在读取' + file_dir)
    df_c5 = pd.read_csv(file_dir, encoding='gbk')
    df_c5 = df_c5.drop(df_c5.columns[0], axis=1)
    df_c5['setType'] = 5
    # 读取军事新闻
    file_dir = '%s\\%s.csv' % (channel_id[3], channel_id[3])
    print('正在读取' + file_dir)
    df_c7 = pd.read_csv(file_dir, encoding='gbk')
    df_c7 = df_c7.drop(df_c7.columns[0], axis=1)
    df_c7['setType'] = 7
    # 读取社会新闻
    file_dir = '%s\\%s.csv' % (channel_id[4], channel_id[4])
    print('正在读取' + file_dir)
    df_c9 = pd.read_csv(file_dir, encoding='gbk')
    df_c9 = df_c9.drop(df_c9.columns[0], axis=1)
    df_c9['setType'] = 9

    # 整合数据
    df = pd.concat([df_c2, df_c3, df_c5, df_c7, df_c9], axis=0)
    df = df.reset_index(drop=True)
    df = df.fillna(0)
    df.to_csv('df.csv')

if __name__ == '__main__':
    pro_data()
