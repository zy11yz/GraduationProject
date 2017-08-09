import requests
import urllib
import re
import time
import json
import pandas as pd
from lxml import etree
from random import choice
import os

def spider():
    path = '..\\file'

    agents = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"
    headers = {'Host': 'www.yidianzixun.com', 'Referer': 'http://www.yidianzixun.com/', 'User-Agent': agents}

    def getQueryString(data):
        return urllib.parse.urlencode(data)

    def getNews(c_id):
        key_name = ['title', 'source', 'url', 'channel_id', 'category', 'dtype', 'ctype', 'content_type',
                    'date', 'like', 'comment_count', 'up', 'tags', 'pageid', 'itemid', 'docid', 'meta',
                    'auth', 'is_gov', 'b_political', 'image_urls', ]
        # 单独添加detail_fulltext特征，此为新闻详细内容
        key_name.append('detail_fulltext')
        news = pd.DataFrame(columns=key_name)

        PageNumber = 20
        for pNumber in range(PageNumber):
            print('正在抓取第%d页信息，敬请关注！----------------------------------' % pNumber)
            cstart = pNumber * 20
            cend = cstart + 20
            query_data = {
                'channel_id': c_id,
                'cstart': cstart,
                'cend': cend,
                'infinite': 'false',
                'refresh': '1',
            }

            baseurl = 'http://www.yidianzixun.com/home/q/news_list_for_channel?'
            url = baseurl + getQueryString(query_data)
            request = requests.get(url, headers=headers)
            html = request.text
            news_data = json.loads(html)
            # 获取到json中的result字段信息，因为信息都藏在这个下面
            news_list = news_data['result']
            for n_item in news_list:
                news_item = []
                if len(n_item) > 8:
                    for every_key in key_name[:-1]:
                        if every_key in n_item.keys():
                            item_content = n_item[every_key]
                        else:
                            item_content = ''
                        # 把原本的item_key拼接到news_item中
                        news_item.append(item_content)

                    try:
                        if len(n_item['url']) != 0:
                            try:
                                # 得到内页链接
                                news_content_url = n_item['url']
                                # print('正在抓取的新闻链接为：%s' %news_content_url)
                                # 去网站首页地址
                                Host = news_content_url[0:news_content_url.find('/', 7) + 1]
                                # 查看编码格式
                                item_pattern = re.compile(r'content="text/html; charset=(.*?)"', re.S)
                                # 默认的web_encoding是'utf-8'
                                web_encoding = 'utf-8'
                                # 有些网站不用headers
                                headers2 = {'Accept': 'text/css,*/*;q=0.1',
                                            'Accept-Encoding': 'gzip, deflate, sdch',
                                            'Accept-Language': 'zh-CN,zh;q=0.8',
                                            'Connection': 'keep-alive',
                                            'Host': Host,
                                            'Referer': Host,
                                            # 'Upgrade-Insecure-Requests:':'1',
                                            'User-Agent': choice(agents)}
                                detail_request = requests.get(news_content_url, timeout=20)
                                # 先读取网页（不论格式）
                                detail_content = detail_request.text
                                # 找到网页所对应的编码格式
                                try:
                                    web_encoding = re.findall(item_pattern, detail_content)[0]
                                except:
                                    web_encoding = 'utf-8'
                                detail_content = detail_request.content.decode(web_encoding)

                                if len(detail_content) < 2:
                                    detail_request = requests.get(news_content_url, headers=headers2)
                                    detail_content = detail_request.content.decode(web_encoding)
                                    if len(detail_content) < 2:
                                        detail_content = ''
                                print('\tdetail_content的len为：%d' % len(detail_content))
                                try:
                                    selector = etree.HTML(detail_content)
                                    detail_text = selector.xpath(u"//div[@id='yidian-content']/p//text()")
                                    # 防止出现匹配不正确的情况,考虑不同类型的格式提取方式

                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='imedia-article']/p//text()")
                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='article-cont']/p//text()")
                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='post-page-content']/p//text()")
                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='content']/p//text()")
                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='content-bd']/p//text()")
                                    # 昆明信息港
                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='detailbg']/p//text()")
                                    # 丝路明珠网
                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='article-main']/p//text()")
                                    # 投资界
                                    if len(detail_text) < 1:
                                        detail_text = selector.xpath(u"//div[@class='news-content']/p//text()")
                                    detail_fulltext = ''
                                    for text in detail_text:
                                        detail_fulltext = detail_fulltext + text
                                    detail_fulltext = detail_fulltext.strip().replace('\xa0', '').replace('\n', '')
                                    detail_fulltext = detail_fulltext.replace('\r', '').replace('\u3000', '')

                                except:
                                    detail_fulltext = ''
                                    print('\tdetail_fulltext存在问题，报错了！')

                            except:
                                detail_fulltext = ''
                                print('\t读取新闻详细信息失败！')
                            # 单独拼接 detail_fulltext
                            news_item.append(detail_fulltext)
                    except:
                        continue

                    if len(detail_fulltext) != 0:
                        news_entry = pd.DataFrame([news_item], columns=key_name)
                        news = news.append(news_entry)
                    else:
                        print('\t\t由于detail_fulltext无内容，所以此条信息不保存到数据中！')
                        print('\t\t此条数据的地址为：%s' % news_content_url)
                else:
                    print('\t此条信息不符合新闻规则，不予抓取！')

            time.sleep(0.2)
        file_dir = '%s\\%s\\' % (path, c_id)
        if os.path.exists(file_dir):
            print('***********')
            print('*文件已存在*')
            print('***********')
        else:
            os.mkdir(file_dir)
        news_name = file_dir + c_id + '.csv'
        news.to_csv(news_name)

    start_all_time = time.time()

    channel_id = ['c2', 'c3', 'c5', 'c7', 'c9']
    for c_id in channel_id:
        print('----------正在执行%s----------' % c_id)
        getNews(c_id)

    end_all_time = time.time()
    work_all_time = end_all_time - start_all_time
    print("\n试验总共所花时间为：%.6f s\n" % work_all_time)

if __name__ == '__main__':
    spider()
