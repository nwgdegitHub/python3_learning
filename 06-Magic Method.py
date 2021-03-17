# 前后两个下划线的方法
class A(object):
    a = 0

    def __init__(self):
        self.b = 1


aa = A()
print(A.__dict__)  #返回类 的所有属性和方法对应的字典
print(aa.__dict__)  #返回实例属性和值组成的字典