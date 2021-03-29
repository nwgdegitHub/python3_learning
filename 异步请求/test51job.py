# 有的网页，并不是下一页获取分页数据，而是又一个链接获取json

# 比如B站评论区，百度地图，网易邮箱的注册，花瓣网 都是异步请求的结果

# 处理步骤：
# 0。判断是否为异步加载
# 1。找到异步请求的链接并分析规律
# 2。获取返回的json数据并解析

import json
import urllib.request, urllib.error
import re

def main():
    # 这个url是怎么得到的，点击第一页之后的页数，找到network中的地址，右键点copy
    url = "https://search.51job.com/list/020000,000000,0000,00,9,99,Python,2,3.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    # askUrl(url)

    # 直接把爬到的数据存result.html 避免多次请求
    result = open('result.html', 'r', encoding='gbk')
    data = re.findall(r"\"engine_search_result\":(.+?),\"jobid_count\"", str(result.readlines()))
    jsonObj = json.loads(data[0])
    # print(jsonObj)
    for item in jsonObj:
        print(item['job_name'] + ':' + item['company_name'])

def askUrl(url):
    html_ret = ""
    head = {
        # User-Agent必要 其他看情况
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        # "Cookie": "guid=bcf0eb12832008fd871a0f50ed19a303; _ujz=MTAwMTM2MjQwMA%3D%3D; ps=needv%3D0; 51job=cuid%3D100136240%26%7C%26cusername%3Dphone_18856425363%26%7C%26cpassword%3D%26%7C%26cname%3D%25C1%25F5%25CE%25B0%26%7C%26cemail%3Dliuw_flexi%2540163.com%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3D%26%7C%26ccry%3D.0ehKQ733GRTY%26%7C%26cconfirmkey%3DlirQ%252FTc.G7rEI%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3DlibdxQRJfBgfg%26%7C%26to%3D3feca52f1665a7e09c0d4ace31e25f44606130cc%26%7C%26; slife=lowbrowser%3Dnot%26%7C%26lastlogindate%3D20210329%26%7C%26securetime%3DAj4ANVA3WTteNVNlWmMAaVVkBzA%253D"
    }
    try:
        req = urllib.request.Request(url=url, headers=head)
        response = urllib.request.urlopen(req)
        htmlRet = response.read().decode("gbk")
        print(htmlRet)
        html_ret = htmlRet

        # 因为多次请求会被403 所以模拟加载本地html文本
        # f = open("51job.json", 'r')
        # html_ret = f.read()
        # print(html_ret)


    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html_ret


if __name__ == '__main__':
    main()