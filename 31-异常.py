# open('tet.txt','r') #打开一个不存在的文件 FileNotFoundError: [Errno 2] No such file or directory: 'tet.txt'

try:
    # 可能发生错误的代码
    f = open('test.txt', 'r')
except:
    # 如果真的出现了异常执行的代码
    f = open('test.txt', 'w')


print("捕获多个异常的类型------")
try:
    print(1/0)
except (NameError, ZeroDivisionError):
    print("错误")

print("捕获异常描述信息------")
try:
    print(1/0)
except (NameError, ZeroDivisionError) as ret:
    print(ret)

print("捕获所有异常,Exception是所有异常的父类------")
try:
    print(1/0)
except Exception as ret:
    print(ret)

print("异常的else--------")
try:
    print(1)
except Exception as ret:
    print(ret)
else:
    print("异常的else表示如果没有异常要执行的代码")


print("异常的finally表示无论有无异常都会执行--------")
try:
    f = open('test1.txt','r')
except Exception as ret:
    f = open('test1.txt','2')
else:
    print("没有异常 真开心")
finally:
    f.close()

