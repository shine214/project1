# 1
class Zombia:
    def __init__(self, name, blood, position):
        self.name = name
        self.blood = blood
        self.position = position

    def beAttacked(self):
        self.blood -= 1

    def walk(self):
        self.position -= 1

    def __str__(self):
        return f'僵尸名字：{self.name} 僵尸血量：{self.blood} 僵尸位置：{self.position}'


class Zombia2:
    def __init__(self, name, color='black'):
        self.name = name
        self.__color = color

    def __str__(self):
        return f'name:{self.name} color:{self.__color}'


# 多重继承顺序以及args参数传递
class secondZombia:
    def __init__(self, para4):
        self.para4 = para4


class motherZombia(secondZombia):
    def __init__(self, para2, *args):
        self.para2 = para2
        super().__init__(*args)


class fatherZombia(secondZombia):
    def __init__(self, para3, *args):
        self.para3 = para3
        super().__init__(*args)


# 想调用motherZombia的init就在zombia里调用super，想要调用father就在mother里调用super
class Zombia4(motherZombia, fatherZombia):
    def __init__(self, para1, *args):
        self.para1 = para1
        super().__init__(*args)


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


def question5():
    try:
        num = input("请输入一个整数")
        # 单写一个int（num）可以引出非整数类型的异常
        int(num)
    except ValueError:
        # 发生了类型错误就向上抛出类型异常
        raise ValueError('输入的不是整数类型')
    if (issymmetric(num) == False):
        raise Exception(f'{num}不是对称数')
    return num


def issymmetric(num):
    return num == num[::-1]


if __name__ == '__main__':
    try:
        print(question5())
    except Exception as e:
        print(f"错误: {e}")
    # 1
    # nomal = Zombia('nomal', 5, 10)
    # print(f'僵尸初始 {nomal}')
    # nomal.beAttacked()
    # print(f'僵尸被攻击后 {nomal}')
    # nomal.walk()
    # print(f'僵尸行进后 {nomal}')
    # # 2
    # nomal2 = Zombia2('nomal')
    # special = Zombia2('special', 'red')
    # print(nomal2)
    # print(special)
    # print(nomal2.name, nomal2.color)
    # # 3
    # zombia = Zombia4(1, 2, 3, 4)
    # print(zombia.para1)
    # print(zombia.para2)
    # print(zombia.para3)
    # print(zombia.para4)
    # # 4
    # # 由于只有一个实例对象，所以后面来的实例会覆盖先前的实例
    # tiger = Animal('tiger')
    # elphant = Animal('elphant')
    # print(id(tiger))
    # print(id(elphant))
    # print(tiger.name)
    # print(elphant.name)
    # 5
