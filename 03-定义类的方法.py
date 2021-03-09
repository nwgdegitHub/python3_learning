class Student(object):
    mobile = '18856425363'
    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_mobile(cls):
        return cls.mobile

    @property
    def get_weight(self):
        return self.__weight

    # 正常的实例方法
    def self_introduction(self):
        print('我叫%s,我的年龄是%d' % (self.name, self._age))

if __name__ == '__main__':
    # 注意 定义了3个参数，必须传3个
    # stu = Student('LW',30)
    stu = Student('LW',30,70)

    print(dir(stu))

    print(Student.get_mobile())

    print(stu.get_weight)

    stu.self_introduction()
