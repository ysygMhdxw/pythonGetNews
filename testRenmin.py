import requests						# 发起网络请求
from bs4 import BeautifulSoup		# 解析HTML文本
import pandas as pd					# 处理数据
import os
import time			# 处理时间戳

'''
用于发起网络请求
url : Request Url
kw  : Keyword
page: Page number
'''
#爬取人民网数据尝试


def fetchUrl(url, kw, page):
    # 请求头
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        'Referer': 'http://search.people.cn/s/?keyword=%E5%87%8F%E8%B4%AB&st=0&_=1647664351335',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    }

    # 请求参数
    payloads = {
        'endTime': 0,
        'hasContent': True,
        'hasTitle': True,
        'isFuzzy': True,
        'key': kw,
        'limit': 10,
        'page': page,
        'sortType': 2,
        'startTime': 0,
        'type': 0,
    }

    # 发起 post 请求
    r = requests.post(url, headers=headers, data=json.dumps(payloads))
    print(r.text)
    return r.json()


def parseJson(jsonObj):
    # 解析数据
    print(jsonObj)
    # records = jsonObj["data"]["records"];
    # print(records)
    # for item in records:
    #     # 这里示例解析了几条，其他数据项如末尾所示，有需要自行解析
    #     pid = item["id"]
    #     originalName = item["originalName"]
    #     belongsName = item["belongsName"]
    #     content = BeautifulSoup(item["content"], "html.parser").text
    #     displayTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["displayTime"] / 1000))
    #     subtitle = item["subtitle"]
    #     title = BeautifulSoup(item["title"], "html.parser").text
    #     url = item["url"]
    #
    #     yield [[pid, title, subtitle, displayTime, originalName, belongsName, content, url]]


if __name__ == "__main__":
    # 起始页，终止页，关键词设置
    start = 1
    end = 3
    kw = "春节"

    # 保存表头行
    headline = [["文章id", "标题", "副标题", "发表时间", "来源", "版面", "摘要", "链接"]]
    # saveFile("./data/", kw, headline)
    # 爬取数据
    for page in range(start, end + 1):
        url = "https://search.people.cn/search-platform/front/search"
        html = fetchUrl(url, kw, page)
        parseJson(html)
        # for data in parseJson(html):
        #     saveFile("./data/", kw, data)
        print("第{}页爬取完成".format(page))

    # 爬虫完成提示信息
    print("爬虫执行完毕！数据已保存至以下路径中，请查看！")
    print(os.getcwd(), "\\data")
