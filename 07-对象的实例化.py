class Person(object):

    # 构造方法 用的也比较少
    def __new__(cls,*args,**kwargs):
        print('call __new__ method')
        print(args)
        return super(Person,cls).__new__(cls,*args,**kwargs)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 较少用
    def __del__(self):
        print('对象销毁')

if __name__ == '__main__':
    person = Person('LW',30)
    print(person.__dict__)
