t1 = (10, 20, 30)
print(t1)
print(type(t1))

t2 = (1, )
print(t2)
print(type(t2))

t3 = (3) # 等价于t3 = 3
print(type(t3))

t4 = ('hello')
print(type(t4))

print("元组查找--------------")
tuple1 = ('aa', 'bb', 'cc', 'cc', 'cc')
print(tuple1[0])

print(tuple1.index("bb"))
print(tuple1.count("cc"))  # cc出现的次数

print(len(tuple1))

print("元组修改--------------")
tuple2 = ('aa', 'bb', 'cc')
# tuple2[0] = 'aaa'  # 元组禁止修改 报错
# print(tuple2)

# 元组里面有列表 可以修改列表里面的数据
tuple3 = (1, 2, 3, ['aa', 'bb', 'cc'], 4, 5)
print(tuple3[3])

tuple3[3][0] = '110aaa'
print(tuple3)








