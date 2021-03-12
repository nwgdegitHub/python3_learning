dict1 = {i: i*2 for i in range(1,5)}
print(dict1)

list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict2 = {list1[i]: list[i] for i in range(len(list1))}
print(dict2)

print("提取目标数据")
counts = {"A": 258, "B": 125, "C": 201, "D": 199}
count1 = {key: value for key, value in counts.items() if value > 200}
print(count1)