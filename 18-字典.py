dict1 = {'name': 'Tom', 'age': 30, 'gender': '男'}
dict2 = {}
dict3 = dict()

print("增------")
dict1['id'] = 110
print(dict1)

print("删------")
# dict1.clear()
# print(dict1)

del(dict2)
# print(dict2) #报错

del(dict1['name']) #删除name键值对
print(dict1)

print("改------")
dict1['age'] = 31
print(dict1)

print("查-------")
print(dict1["age"])

print(dict1.get('age'))
print(dict1.get('sex'))
print(dict1.get('sex', '男'))

print(dict1.keys())
print(dict1.values())

print(dict1.items()) # [('age', 31), ('gender', '男'), ('id', 110)]

print("遍历-------")
for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for item in dict1.items():
    print(item)

for key,value in dict1.items():
    print(f'{key} = {value}')