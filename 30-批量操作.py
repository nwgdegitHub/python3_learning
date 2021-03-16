import os

# 批量修改文件名，既可以添加指定字符串，又能删除指定字符串

file_list = os.listdir('testdir')
print(file_list)
for i in file_list:
    new_name = 'python_' + i
    os.rename('testdir/'+i, 'testdir/'+ new_name)
