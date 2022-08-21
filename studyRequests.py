import urllib.parse
import urllib.request as urllib2
import re
import json
import html
import time
from datetime import datetime

# 请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8"
}
# 南方网的url
url_nanfang = 'https://search.southcn.com/api/search/all'
# 人民网的url
url_renmin = "https://search.people.cn/search-platform/front/search"

# 南方网的参数
parm_nanfang = {
    "project_id": 5,
    "service_area": 1,
    'sort': 'smart',
    'position': 'title',
    'keywords': '减贫',
    'page_size': 10,
    'page': 2,
    'type': 'normal',
}
# 人民网的参数
parm_renmin = {
    'endTime': 0,
    'hasContent': True,
    'hasTitle': True,
    'isFuzzy': True,
    'key': "减贫",
    'limit': 10,
    'page': 1,
    'sortType': 2,
    'startTime': 0,
    'type': 0,
}


def parse_ajax_web(url, headers, parm):
    # 每个ajax请求要传递的参数
    data = urllib.parse.urlencode(parm).encode()
    req = urllib2.Request(url, data=data, headers=headers)
    responce = urllib2.urlopen(req).read().decode()
    return responce


# 南方网爬取数据
def cope_nan_fang(keyword):
    parm_nanfang['keywords'] = keyword
    for i in range(1, parm_nanfang['page_size'] + 1):
        parm_nanfang['page'] = i
        # 使用post方法爬取网页，返回json数据并解析
        responce = parse_ajax_web(url_nanfang, headers, parm_nanfang)
        json_dict = json.loads(responce)
        newsdata = json_dict.get('data').get("news").get('list')
        for item in newsdata:
            title = item.get('title')
            title = ''.join(title)
            title = re.sub('<[^<]+?>', '', title).replace('\n', '').strip()
            title = html.unescape(title)
            print(title)
            print(item.get('path'))
            print(item.get('created_at'))
            print(item.get('editor'))
            print(item.get('digest'))
            print("----------------------------------------")


# 南方网爬取数据
def cope_ren_min(keyword):
    parm_renmin['key'] = keyword
    for i in range(1, parm_renmin['limit'] + 1):
        parm_renmin['page'] = i
        # 使用post方法爬取网页，返回json数据并解析
        responce = parse_ajax_web(url_renmin, headers, parm_renmin)
        json_dict = json.loads(responce)
        newsdata = json_dict.get('data').get("records")
        for item in newsdata:
            title = item.get('title')
            title = ''.join(title)
            title = re.sub('<[^<]+?>', '', title).replace('\n', '').strip()
            title = html.unescape(title)
            print(title)
            print(item.get('url'))
            time = item.get('displayTime')
            dt_time = datetime.fromtimestamp(time)
            print(dt_time)
            print(item.get('editor'))
            print(item.get('content'))
            print("----------------------------------------")


def main():
    keywords = ["减贫", "扶贫", "乡村振兴"]
    for keyword in keywords:
        cope_nan_fang(keyword)
        # cope_ren_min(keyword)


if __name__ == '__main__':
    main()
