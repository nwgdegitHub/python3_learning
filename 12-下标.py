str = 'abcdefg'
print(str[0])
print(str[1])

# 序列[开始位置下标:结束位置下标:步长]
# 步长正负数都行 默认是1 为负数表示倒着选 结尾不包含
# 不写开始 默认从0开始
# 不写结尾 默认选到最后
# 下标-1表示最后一位 -2表示倒数第二位

str1 = "0123456789"
print(str1[2:5:1])
print(str1[2:5:2])
print(str1[2:5]) #默认步长1
print(str1[:5]) #默认结束下标5
print(str1[2:])
print(str1[:])
print(str1[:-1])  # 在头部开始 -1处结束 默认步长1

print("负数测试-------------")
print(str1[::-1])
print(str1[-4:-1]) #倒数第4位开始 倒数第一位结束(不包含)

print("步长负数测试-------------")
print(str1[-4:-1:1])
print(str1[-4:-1:-1]) #步长为-1 就是说方向向左 这样的切片数据不存在

# 字符串可以认为是字符的的集合
