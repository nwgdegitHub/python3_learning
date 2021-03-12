# 创建集合用{} 或者 set()
# 但如果要创建空集合只能用set() 因为{} 是用来创建空字典的

print("创建集合------")
s1 = {1, 2, 3, 4, 5, 6}
print(s1)

s2 = {1, 2, 1, 2, 3, 1, 2}
print(s2)  # 去重了{1, 2, 3}

s3 = set("abcdefg")
print(s3)

s4 = set()
print(s4)

s5 = {}
print(s5)

s6 = set({1, 2, 1, 2, 3, 1, 2})
print(s6)

print("增加------")
s1.add(100)
print(s1)  # {1, 2, 3, 4, 5, 6, 100}

s1.update("100")  # 注意增加的数据是序列 此处相当于 ['1', '0', '0']
print(s1)  # {1, 2, 3, 4, 5, 6, '0', 100, '1'}

print("删除------")
s1.remove(1)
print(s1)  # {2, 3, 4, 5, 6, '0', 100, '1'}

s1.discard(1)  # 删除指定数据 如果数据不存在也不会报错
print(s1)

s1.pop()
print(s1)  # {3, 4, 5, 6, '0', 100, '1'}


print("查询------")
print(3 in s1)  # True
print(3 not in s1)  # False


