from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3

# 例如
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# httpbin.org 一个测试http的网站

import urllib.parse

# data = bytes(urllib.parse.urlencode({"key1":"val1"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=10)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print(e)


# try:
#     response = urllib.request.urlopen("http://www.douban.com/", timeout=10)
#     print(response.read().decode('utf-8'))
# except urllib.error.HTTPError as e:
#     print(e)  # HTTP Error 418: 这个错表示你已经被发现是个爬虫了 那么怎么办？

# 如何伪装自己 不让对方发现？ User-Agent
try:
    url = "http://www.douban.com/"
    # header = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Connection": "keep-alive",
    #     "Cookie": "ll='108296'; bid=im-fqNgm-m4; _pk_ses.100001.8cb4=*; _pk_id.100001.8cb4=5a67896ad26495a9.1616563112.1.1616563256.1616563112.",
    #     "Host": "www.douban.com",
    #     "Sec-Fetch-Dest": "document",
    #     "Sec-Fetch-Mode": "navigate",
    #     "Sec-Fetch-Site": "none",
    #     "Upgrade-Insecure-Requests": "1"
    #     "Cookie": "bid=f7CkS1mANhE; dbcl2="195346423:xqjLGkOA9sc"; ck=Ta54; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1616658085%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; __yadk_uid=Q5MT4k0DQ9sLet0cCMfRQPsENsHUQ8gG; __gads=ID=13801efc694179d2-221d07c7d7c6005a:T=1616658639:RT=1616658639:S=ALNI_MaWdweOI1tJoLVSowWX_HLltbUULA; _pk_id.100001.4cf6=fd3cc9cbaf11d8a0.1616658085.1.1616658644.1616658085."
    # }
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    }
    # data = bytes(urllib.parse.urlencode({"key1": "val1"}), encoding="utf-8")
    req = urllib.request.Request(url=url, headers=header, )
    response = urllib.request.urlopen(req)
    # print(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print(e)


# ---------------------测试结束---------------------
