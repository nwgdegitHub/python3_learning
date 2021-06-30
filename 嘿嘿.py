import re,os
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from urllib import request

# 477 550 697
NUM = 447

def askURL(url):
    html_ret = ""
    head = {
        # User-Agent必要 其他看情况
        # "authority": "www.yalayi.com",
        "referer": "https://www.yalayi.com/user/mygallery/",
        # "if-modified-since": "Tue, 29 Jun 2021 06:36:01 GMT",
        # "sec-ch-ua-mobile": "?0",
        # "sec-fetch-dest": "document",
        # "sec-fetch-mode": "navigate",
        # "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "keep-alive",
        # "Cache-Control": "max-age=0",
        "Host": "www.yalayi.com",
        # "Sec-Fetch-Dest": "document",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-Site": "none",
        # "Upgrade-Insecure-Requests": "1",
        "Cookie": "UM_distinctid=17a1896e5f5a55-087a424c171bb1-37607201-240000-17a1896e5f637b; ogmjxmlusername=18856425363; ogmjxmluserid=167138; ogmjxmlgroupid=3; ogmjxmlrnd=LmG8sQZ5fsGUlHL3co1H; ogmjxmlauth=d884a3835c9e405e5fbf3866e4f88a94; CNZZDATA1279092031=2145931356-1623905385-%7C1625031868"
    }
    try:
        req = urllib.request.Request(url=url, headers=head)
        response = urllib.request.urlopen(req)
        htmlRet = response.read().decode("utf-8")
        print(htmlRet)
        html_ret = htmlRet

        # 创建空文件
        desktop_path = os.getcwd() + "/美女/"  # 新创建的txt文件的存放路径

        full_path = desktop_path + "{}".format(NUM) + '.html'  # 也可以创建一个.doc的word文档
        print(full_path)
        file = open(full_path, 'w')  # w 的含义为可进行读写
        file.write(html_ret)  # file.write()为写入指令
        file.close()





        # 因为多次请求会被403 所以模拟加载本地html文本
        # f = open("/Users/udc/Desktop/日常学习/Python3/美女/550.html", 'r')
        # html_ret = f.read()
        # print(html_ret)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html_ret

def creat_dir(path):
    """
    创建文件夹
    :param path:文件夹路径
    :return:文件夹
    """
    if not os.path.exists(path):
        os.mkdir(path) #默认在当前项目下创建

if __name__ == '__main__':
    askURL("https://www.yalayi.com/gallery/664.html")
#     # 打开文件
#     fo = open("849.html", "rw+")
#     print("文件名: ", fo.name)

    # creat_dir("{}".format(NUM))
    #
    # f = open("/Users/udc/Desktop/日常学习/Python3/美女/{}.html".format(NUM), 'r') #没有就新建
    # html_ret = f.read()
    # # print(html_ret)
    # soup = BeautifulSoup(html_ret, "html.parser")  # 使用html.parser解析器来解析html
    # data = []
    #
    # findImgSrc = re.compile(r'<img.*data-original="(.*?)"', re.S)
    #
    # for item in soup.find_all('img', class_="lazy"):
    #     link = re.findall(findImgSrc, str(item))[0]
    #     data.append(link)
    # print(data)
    #
    # for i, value in enumerate(data):
    #     print(i, value)
    #     save_path = "./{}/{}.jpg".format(NUM, i)
    #     # print(save_path)
    #     request.urlretrieve(value, save_path)
