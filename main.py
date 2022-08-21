import pandas as pd
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3

titlelist=["name","url"]
filepath="coutput.xlsx"
newdf=pd.DataFrame(columns=titlelist)

def getData(baseurl):
    datalist1 = []  # 存储一个网页的没有分词的key-value
    html = askurl(baseurl, "utf8")
    bs = BeautifulSoup(html, "html.parser")
    # print(bs)
    t_list=bs.find_all(class_='news_item')
    print(t_list)
    #
    # for index,item in enumerate(t_list):
    #     rowdata = []
    #     line=item.get_text()
    #     rowdata.append(line)
    #     rowdata.append(item["href"])
    #     save(rowdata)

def save(rowlist):
    print(rowlist)
    df_rows = newdf.shape[0]
    newdf.loc[df_rows] = rowlist

    newdf.to_excel(filepath, sheet_name="sheet1", index=False, header=True)


def askurl(url, decode):
    # 模拟头部，像其发送信息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    # 用户代理，表示告诉浏览器是什么信息，表示我们可以接受什么水平的数据
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        responce = urllib.request.urlopen(request)
        html = responce.read().decode(decode)
        print(html)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        askurl(url, decode)
    return html


def main():
    url="http://sou.chinanews.com.cn/search.do?q=%E5%87%8F%E8%B4%AB"
    getData(url)

if __name__ == '__main__':
    main()
