class Zombia:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'name:{self.name},color:{self.color}'

    def eat(self):
        print('吃掉植物一滴血')

    def walk(self):
        print('向前前进一格')


class PEZombia(Zombia):

    # 不写init和eat
    def walk(self):
        super().walk()
        print('体育生走得快，额外再走一格')

    def run(self):
        print('体育生特殊技能，可以向前移动三格')


if __name__ == '__main__':
    peStudent = PEZombia('peStudent', 'black')
    print(peStudent)
    peStudent.eat()
    peStudent.walk()
    peStudent.run()
