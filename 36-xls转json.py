
import xlrd
from collections import OrderedDict
import simplejson as json
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('./douban_origin/豆瓣电影Top250.xls')
sh = wb.sheet_by_index(0)
# List to hold dictionaries
data_list = []
# print(sh.nrows)
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(rownum)
    print(row_values)
    data['link'] = row_values[0]
    data['imgSrc'] = row_values[1]
    data['titles_z'] = row_values[2]
    data['titles_e'] = row_values[3]
    data['rating'] = row_values[4]
    data['judgeNum'] = row_values[5]
    data['inq'] = row_values[6]
    data['bd'] = row_values[7]
    data['collect'] = row_values[8]
    data_list.append(data)
# data_list = {'intents': data_list} # Added line
# Serialize the list of dicts to JSON
j = json.dumps(data_list)
# Write to file
with open('top250.json', 'w') as f:
    f.write(j)