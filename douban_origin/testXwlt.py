
import xlwt

'''
workbook = xlwt.Workbook(encoding="utf-8") # 创建Workbook对象
worksheet = workbook.add_sheet('sheet1') # 创建名为sheet1的工作表
worksheet.write(0,0,'hello') # 给（0，0）这个单元格写入 'hello'
workbook.save('student.xls') #保存数据

'''


# 做一个99乘法表的练习
workbook = xlwt.Workbook(encoding="utf-8") # 创建Workbook对象
worksheet = workbook.add_sheet('sheet1') # 创建名为sheet1的工作表
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i, j, "%d * %d = %d"%(i+1, j+1, (i+1)*(j+1)))  # 给（0，0）这个单元格写入 'hello'

workbook.save('student.xls') #保存数据