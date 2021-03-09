
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

class CollegeStudent(Student):
    def __init__(self,name,age,weight,language):
        super(CollegeStudent,self).__init__(name,age,weight)
        self.language = language

    def self_introduction(self):
        print('我叫%s,我的年龄是%d,我学的语言是%s' % (self.name, self._age,self.language))

def introduce(stu):
    if isinstance(stu,Student):
        stu.self_introduction()


if __name__ == '__main__':

    stu = Student('LW',30,70)

    cstu = CollegeStudent('LW',30,70,'中文')

    introduce(stu)

    introduce(cstu)
