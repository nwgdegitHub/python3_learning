# 把函数作为参数传入 这样的函数叫高阶函数, 也就是函数的参数包含函数
import functools

print(abs(-10))

print(round(1.2))
print(round(1.9))

print("map------ 作用于每个元素")
list1 = [1, 2, 3, 4, 5]


def func1(x):
    return x ** 2


ret1 = map(func1, list1)

print(ret1)  # <map object at 0x100ba2f70>

print(list(ret1))  # [1, 4, 9, 16, 25]


print("reduce------- 累加")
list2 = [1, 2, 3, 4, 5]


def func2(a, b):
    return  a + b

ret2 = functools.reduce(func2, list2)

print(ret2)  # 15

print("filter------ 过滤掉不满足条件的元素")

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func3(x):
    return x % 2 == 0

ret3 = filter(func3, list3)

print(ret3)

print(list(ret3))

