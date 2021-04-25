import datetime
import calendar
import time
def sum(n):
    sum = 0
    while n >= 1:
        sum = sum + n
        n = n - 1
    return sum




def fn(n):
    return n


print(sum(365))

# 第一天存1块，第二天存2块，第三天存3块，...第365天存365块
# 今天的日期是 第XXX天 我应该存XXX 目前位置存了XXX
print(datetime.date.today())

monthRange = calendar.monthrange(2021, 4)
print(monthRange)

# 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
# 以上实例输出的意思为 2021 年 4 月份的第一天是星期四，该月总共有 30 天。

months = (0,31,59,90,120,151,181,212,243,273,304,334)

print(datetime.date.month)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)

days = months[int(localtime.tm_mon)-1] + int(localtime.tm_mday)

print(f'今天的日期是%s, 第%d天, 我应该存%d, 目前总共存了%d'%(datetime.date.today(),days,days,sum(days)))





