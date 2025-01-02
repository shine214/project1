class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        # 让狗玩耍
        dog.game()
        # 1. 创建一个狗对象


wangcai1 = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# 2. 创建一个大象对象
xiaoming = Person("大象")
# 3. 让大象调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(wangcai1)
