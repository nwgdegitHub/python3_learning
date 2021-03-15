import os  # 文件夹操作都需要借助os模块
# 用法:
# os.函数名()
# os.rename(目标文件名, 新文件名)
# os.remove(目标文件名)
# os.mkdir(文件夹名字)
# os.rmdir(文件夹名字)
# os.getcwd()
#



# 1.用户输入目标文件
# 2.备份文件的名字
# 3.写入数据

old_name = input('请输入文件名:')  # test.txt

index = old_name.rfind('.')

print(index)
if index > 0:
    print("文件名合格")
    postfix = old_name[index:]

print(old_name[:index])

new_name = old_name[:index] + '[备份]' + postfix

print(new_name)

old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)

old_f.close()
new_f.close()

