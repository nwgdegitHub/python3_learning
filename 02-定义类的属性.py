class Person(object):
    mobile = '18856425363'

    def __init__(self, name, age, weight):
        self._Person__weight = None
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    @property
    def Person__weight(self):
        return self._Person__weight


if __name__ == '__main__':
    # 注意 定义了3个参数，必须传3个
    # person = Person('LW',30)
    person = Person('LW', 30, 70)

    print(dir(person))
    # 获取对象的全部属性
    print(person.__dict__)
    print(person.get_weight())
    print(person.Person__weight)

# <__main__.Person object at 0x10a86aee0>
# <class '__main__.Person'>
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']
