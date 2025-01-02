class Person:
    # 类属性（可以理解为该类的全局变量）
    number = 0

    def __init__(self, name):
        self.name = name
        Person.number += 1
        self.initialize()

    @classmethod
    def show_count(cls):
        """
        类方法头@classmathod
        """
        print(cls.number)

    @staticmethod
    def initialize():
        """
        静态方法头@staticmethod 一般用于初始化，不需要设置任何传参
        """
        print("初始化加载中")
        print('正在设置各项参数')


if __name__ == "__main__":
    mike = Person("Mike")
    david = Person("David")
    Person.show_count()
