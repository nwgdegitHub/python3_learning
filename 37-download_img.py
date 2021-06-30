# 引入模块
import os
from urllib import request
import urllib.request, urllib.error



def startdown():
    for j in range(600, 699):

        creat_dir("{}".format(j))
        for i in range(1, 50):
            try:

                url = "https://img.yalayi.net/img/gallery/{}/{}.jpg!pcimg".format(j, i)
                # print(url)
                save_path = "./{}/{}.jpg".format(j, i)
                # print(save_path)
                request.urlretrieve(url, save_path)  # s是图片的网络地址，./图片1.jpg，是图片的保存地址，如果不写./表示在本目录下
                while i == 50:
                    print("{}目录下载完毕!".format(j))
            except:
                if i == 1:
                    print("{}目录下无内容!".format(j))
                    # remove_dir("{}".format(j))
                    break

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

def remove_dir(path):
    if os.path.exists(path):
        os.remove(path)


if __name__ == '__main__':


    startdown()