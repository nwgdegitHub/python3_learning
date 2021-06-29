# 引入模块
import os
from urllib import request
import urllib.request, urllib.error



def startdown():

    for i in range(0, 100):
        try:

            url = "https://img.yalayi.net/img/gallery/{}/{}.jpg!pcimg".format('849',i)
            # print(url)
            save_path = "./{}/{}.jpg".format('849',i)
            # print(save_path)
            request.urlretrieve(url, save_path) # s是图片的网络地址，./图片1.jpg，是图片的保存地址，如果不写./表示在本目录下

        except:
            continue

    # try:
    #     url = 'https://img.yalayi.net/img/gallery/841/0.jpg!pcimg'
    #     ret = request.urlretrieve(url, './841/0.jpg')
    #     print(ret)
    #     # ('./841/30.jpg', < http.client.HTTPMessage object at 0x10cbe85e0 >)
    # except:
    #     # 如果真的出现了异常执行的代码
    #     print("continue")

def creat_dir(path):
    """
    创建文件夹
    :param path:文件夹路径
    :return:文件夹
    """
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':

    creat_dir("849")
    startdown()