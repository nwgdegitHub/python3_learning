print("元组拆包------")
def return_num():
    return 1, 2

num1,num2 = return_num()
print(num1)
print(num2)

print("字典拆包------")
dict1 = {'name': 'Tom', 'age': 18}
a, b = dict1

print(a)
print(b)

print(dict1[a])
print(dict1[b])

