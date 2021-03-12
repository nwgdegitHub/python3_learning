print("判断是否存在------------")

name_list = ["TOM","James","Linda"]
print("James" not in name_list)
print("James" in name_list)

print("追加数据------------")
print(name_list.append("Li"))
print(name_list)

name_list.extend("LW")
print(name_list)

name_list.extend(["LW","LW2"])
print(name_list)

print("插入------------")
name_list.insert(0,"Zhang")
print(name_list)

print("删除------------")
# del name_list
# del name_list[0]
# name_list.pop()
# name_list.remove("LW")
# name_list.clear()

print(name_list)

print("修改------------方法无返回值")
num_list = [11,2,3,4,5,6,8]

#修改指定下标
num_list[0] = 33
print(num_list)

#逆置
num_list.reverse()
print(num_list)

#升序
num_list.sort(key=None,reverse=False)
print(num_list)
#降序
num_list.sort(key=None,reverse=True)
print(num_list)

#复制
num_list2 = num_list.copy()
print(num_list2)

#while遍历
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

#for遍历
for i in name_list:
    print(i)

#列表嵌套----类似二维数组处理







