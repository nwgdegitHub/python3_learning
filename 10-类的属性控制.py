# __setattr__(self,name,value)

# __getattr__(self,name)

# __getattribute__(self,name)

# __delattr__(self,name,value)

class Programer(object):
    """docstring for ."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattribute__(self,name):
        return super(Programer,self).__getattribute__(name)

    def __setattr__(self,name,value):
        self.__dict__[name] = value

if __name__ == '__main__':
    p = Programer('LW',30)
    print(p.name)