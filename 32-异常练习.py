# 尝试打开一个文件 如果文件存在就读取内容 文件不存在就提示用户
# 读取内容时检测到意外终止，就捕获异常并提示

import time

try:
    f = open('test1.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(3)  # 延时一下
            print(content)
    except:
        print("程序被意外终止----如:ctrl+c")

except:
    print('文件不存在')
