from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3

# 注意变量的命名最好不要和关键字冲突


def main():
    print("main")
    # 1.爬取网页
    baseurl = "http://movie.douban.com/top250?start="
    datalist = getData(baseurl)

    # 2.解析数据

    # 3.保存数据
    savepath = "豆瓣电影Top250.xls"
    saveData(datalist,savepath)


# ---------------------全局正则---------------------
# 影片连接
findLink = re.compile(r'<a href="(.*?)">')
# 影片展示图片
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 相关内容
findBd = re.compile(r'<p class="">(.*)<div class="star">', re.S)  # re.S 模式表示忽视换行符


# 1.爬取网页
def getData(baseurl):

    datalist = []

    for i in range(0, 10):
        url = baseurl + str(i * 25)
        htmlRet = askURL(url)
        # 逐一解析 弄到一个网页就解析一下
        soup = BeautifulSoup(htmlRet,"html.parser") #使用html.parser解析器来解析html
        for item in soup.find_all('div',class_="item"):
            # print(item)
            data = []  #保存一部电影的所有信息
            # 1
            link = re.findall(findLink, str(item))[0]
            data.append(link)
            # 2
            imgSrc = re.findall(findImgSrc, str(item))[0]
            data.append(imgSrc)
            # 3 # 4
            # print(re.findall(findTitle, str(item)))
            titles = re.findall(findTitle, str(item))
            #片名如果有中英文 都存一下
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            elif(len(titles) == 1):

                ctitle = titles[0]
                data.append(ctitle)
                data.append(' ') #外文名可能为空
            else:
                print("titles 为 []")

            # 5
            rating = re.findall(findRating,str(item))[0]
            data.append(rating)
            # 6
            judgeNum = re.findall(findJudge,str(item))[0]
            data.append(judgeNum)
            # 7
            inq = re.findall(findInq,str(item))
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            # 8
            print(re.findall(findBd, str(item)))
            bd = re.findall(findBd, str(item))[0]
            # bd = str(bd)
            bd = re.sub('<br(\s+)?/>(\s+)'," ", bd)  # 去掉br
            bd = re.sub('/'," ",bd)  # 去掉/

            data.append(bd.strip())  # 去掉前后空格
            # print(bd.strip().find("<div class=\"star\">"))
            # 我这里有一个问题 就是findBd这个正则找到的内容里有html标签 需要继续处理一下

            datalist.append(data)

    return datalist


def askURL(url):
    html_ret = ""
    head = {
        # User-Agent必要 其他看情况
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
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
        # "Cookie": "bid=f7CkS1mANhE; dbcl2='195346423:xqjLGkOA9sc'; ck=Ta54; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1616658085%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; __yadk_uid=Q5MT4k0DQ9sLet0cCMfRQPsENsHUQ8gG; __gads=ID=13801efc694179d2-221d07c7d7c6005a:T=1616658639:RT=1616658639:S=ALNI_MaWdweOI1tJoLVSowWX_HLltbUULA; _pk_id.100001.4cf6=fd3cc9cbaf11d8a0.1616658085.1.1616658644.1616658085."
    }
    try:
        # req = urllib.request.Request(url=url, headers=head)
        # response = urllib.request.urlopen(req)
        # htmlRet = response.read().decode("utf-8")
        # # print(htmlRet)
        # html_ret = htmlRet

        # 因为多次请求会被403 所以模拟加载本地html文本
        f = open("豆瓣.html", 'r')
        html_ret = f.read()
        # print(html_ret)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html_ret


def saveData(datalist, savepath):
    workbook = xlwt.Workbook(encoding="utf-8")  # 创建Workbook对象
    worksheet = workbook.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)  # 创建名为xxx的工作表 单元格可以被覆盖
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价书", "概况", "相关信息")  # 列
    for i in range(0, 8):
        worksheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0, 8):
            worksheet.write(i+1, j, data[j])

    workbook.save(savepath)  # 保存数据


if __name__ == '__main__':
    main()





















