
# __str__
#
# __repr__
#
# __unicode__
#
# __dir__

class Person(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')


if __name__ == '__main__':
    person = Person('LW',30)
    print(person)
    print(dir(person))
