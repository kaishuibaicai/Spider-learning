import  requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo
from lxml.etree import XMLSyntaxError
client = pymongo.MongoClient('localhost')
db = client['weixin']

base_url = 'http://weixin.sogou.com/weixin?'
keyword = '风景'
proxy_pool_url = 'http://127.0.0.1:5000/get'
proxy = None
max_count = 5
headers = {
            'Cookie':'CXID=1A72C7A31ECD4F481ED3762D709637C3; SUV=00AC555501B4EB29582BD0A6EAF7B184; ad=5neL9kllll2YMbXDlllllV0iZCZllllltR2SPlllllylllllVylll5@@@@@@@@@@; SUID=D2B10B756573860A5808292C000B1D63; ABTEST=3|1492928180|v1; weixinIndexVisited=1; IPLOC=CN3200; sct=1; SNUID=66B0D093E2E7AF2C7B6B5CC5E3947125; JSESSIONID=aaamGL5S23ems6PjQ-ESv',
            'Host':'weixin.sogou.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.113 Safari/537.36'
            }
def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url, count=1):
    print('Crawling:', url)
    print('Trying Count:', count)
    global proxy
    if count>max_count:
        print('Tried too many counts')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            print('200')
            return response.text
        if response.status_code == 302:
            #need proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using proxy:', proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred', e.args)
        count += 1
        proxy = get_proxy()
        return get_html(url, count)

def get_index(keyword, page):
    data = {
        'query':keyword,
        'type':2,
        'page':page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def parse_index():
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickname = doc('#js_profile_qrcode > div > strong').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title':title,
            'content':content,
            'date':date,
            'nickname':nickname,
            'wechat':wechat
        }
    except XMLSyntaxError:
        return None

def save_to_mongo(data):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print('Saved to mongo :', data['title'])
    else:
        print('Saved to Mongo Failed', data['tittle'])

def main():
    for page in range(1, 101):
        html = get_index(keyword, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_url)
                    print(article_data)
                    if article_data:
                        save_to_mongo(article_data)


if __name__ == '__main__':
    main()
