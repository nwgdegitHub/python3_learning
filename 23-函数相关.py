print("元组拆包------")


def return_num():
    return 1, 2


num1, num2 = return_num()
print(num1)
print(num2)

print("字典拆包------")
dict1 = {'name': 'Tom', 'age': 18}
a, b = dict1

print(a)
print(b)

print(dict1[a])
print(dict1[b])

print("修改全局变量------")
a = 100


def testA():
    global a
    a = 200
    print(a)


testA()

print("函数的多个返回值------")


def testB():
    return 1, 2, 3


print(testB())

print("函数的传参------")


def testC(name, age, gender):
    print(f'名字={name},年龄={age},性别={gender}')


testC("LW", age=30, gender='男')  # age=30 这种叫关键字参数

print("不定长参数------")


def testD(*args):
    print(args)  # ('LW', 30)


testD('LW', 30)


def testD(**kwargs):
    print(kwargs)  # {'name': 'LW', 'age': 30}


testD(name='LW', age=30)
