import re
import pandas as pd
import matplotlib as mpl
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
mpl.use('Agg')
path = '..\\file'
os.chdir(path)
df = pd.read_csv('df.csv', encoding='gbk')
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
df_2 = df.loc[:, ['detail_fulltext', 'setType']]


class LanguageDetector(object):

    def __init__(self, classifier=LogisticRegression(penalty='l2')):
        self.classifier = classifier
        self.vectorizer = CountVectorizer(ngram_range=(1, 2), max_features=20000, preprocessor=self._remove_noise)

    def _remove_noise(self, document):
        noise_pattern = re.compile("|".join(["http\S+", "\@\w+", "\#\w+"]))
        clean_text = re.sub(noise_pattern, "", document)
        return clean_text

    def features(self, X):
        return self.vectorizer.transform(X)

    def fit(self, X, y):
        self.vectorizer.fit(X)
        self.classifier.fit(self.features(X), y)

    def predict(self, x):
        return self.classifier.predict(self.features([x]))

    def score(self, X, y):
        return self.classifier.score(self.features(X), y)


def lgt():
    x = df_2['detail_fulltext']
    y = df_2['setType']

    # 区分训练集与测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

    language_detector = LanguageDetector()
    language_detector.fit(x_train, y_train)
    print(language_detector.score(x_test, y_test))

if __name__ == '__main__':
    lgt()
