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


if __name__ == '__main__':
    zombia = Zombia4(1, 2, 3, 4)
    print(zombia.para1)
    print(zombia.para2)
    print(zombia.para3)
    print(zombia.para4)
