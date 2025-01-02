# 单例设计模式，通过重写__new__实例方法在没实例的时候调用父类object的__new__方法来把实例个数严格限制为1

class Animal(object):
    # 这个instance 就是类属性
    instance = None

    def __new__(cls, *args, **kwargs):
        """
        固定写法， 需记忆
        """
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # 由于只有一个实例对象，所以后面来的实例会覆盖先前的实例
    tiger = Animal('tiger')
    elphant = Animal('elphant')
    print(id(tiger))
    print(id(elphant))
    print(tiger.name)
    print(elphant.name)
