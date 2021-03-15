#lamda其实定义了一个匿名函数

# lambda 参数列表 ：表达式

print((lambda a, b: a + b)(1, 2))  # 3
print(lambda: 100)  # <function <lambda> at 0x10f2290d0>
print((lambda: 100)())  # 100
print((lambda a: a)('hello'))  # hello
print((lambda *args: args)(10, 20, 30))  # (10, 20, 30)
print((lambda **kwargs: kwargs)(name='python', age=20))  # {'name': 'python', 'age': 20}
