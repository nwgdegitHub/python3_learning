# 能被4整除且不能被100整除的为闰年。
# 能被4整除且能被100整除，且能被400整除的为闰年。

# //1、非整百年：能被4整除的为闰年。（如2004年就是闰年,2100年不是闰年）
# //2、整百年：能被400整除的是闰年。(如2000年是闰年，1900年不是闰年)
# //3、对于数值很大的年份：这年如果能被3200整除,并且能被172800整除则是闰年。如172800年是闰年，86400年不是闰年(因为虽然能被3200整除，但不能被172800整除)
year = int(input("输入一个年份: "))

if (year % 4 ) == 0:
    if (year % 100 ) == 0:
        if (year % 400) == 0:
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    else:
        print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))


