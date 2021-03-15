# int,float,string,tupple 不可变，数据不可以直接修改
a = 1
b = a
print(b)

print(id(a))
print(id(b))

a = 2

print(b)

print(id(a))
print(id(b))

print("-----------------------")

# list, dict, 集合 可变,数据可以直接修改
aa = [10, 20]
bb = aa

print(bb)

print(id(aa))
print(id(bb))

aa.append(30)
print(bb)

print(id(aa))
print(id(bb))
