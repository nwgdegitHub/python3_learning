# 回文数就是指整数倒过来和原整数相等
str = str(input("请输入一个数字: "))
print(str)
print(str[::-1])
if str == str[::-1]:
    print("是")
else:
    print("不是")