class Person(object):

    __solt__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 访问器 getter方法
    @property
    def name(self):
        return self._name

    # 访问器 getter方法
    @property
    def age(self):
        return self._age

    # 修改器 setter方法
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age < 16:
            print('%s正在玩飞行棋' % self._name)
        else:
            print('%s正在玩斗地主' % self._name)


def main():
    person = Person('王大锤', 18)
    person.play()
    person.age = 14
    person.play()
    person._gender = '男'
    person._is_gay = True

 
main()