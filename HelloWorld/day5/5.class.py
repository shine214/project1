class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def reflect(self, person):
        if (person == '生人'):
            print('汪汪叫')
        elif (person == '熟人'):
            print('摇尾巴')


xiaohuang = Dog('xiaohuang', 'red')
xiaohuang.reflect('熟人')
