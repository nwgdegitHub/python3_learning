print("方法一:定义中间变量")

numA = 10
numB = 20


def swap1(a, b):
    c = 0
    c = a
    a = b
    b = c
    return a, b


print(swap1(numA, numB))

print("方法二：")

numA, numB = numB, numA

print(numA, numB)
