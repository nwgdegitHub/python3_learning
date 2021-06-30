import re
import urllib.request, urllib.error

def askURL(url):
    html_ret = ""
    head = {
        # User-Agent必要 其他看情况
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "keep-alive",
        # "Cache-Control": "max-age=0",
        # "Host": "movie.douban.com",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "none",
        # "Upgrade-Insecure-Requests": "1",
        # "Cookie": "UM_distinctid=17a574442e2639-06e0f9d03d4e1c-34647600-232800-17a574442e3b98; ogmjxmlusername=18856425363; ogmjxmluserid=167138; ogmjxmlgroupid=3; ogmjxmlrnd=xJUg658dJQGobFzDJGto; ogmjxmlauth=ce7b6c2389aaa97aa19b66078b5ad85f; CNZZDATA1279092031=309614284-1624956686-|1624962238"
    }
    try:
        req = urllib.request.Request(url=url, headers=head)
        response = urllib.request.urlopen(req)
        htmlRet = response.read().decode("utf-8")
        # print(htmlRet)
        html_ret = htmlRet

        # 因为多次请求会被403 所以模拟加载本地html文本
        # f = open("豆瓣.html", 'r')
        # html_ret = f.read()
        # print(html_ret)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html_ret