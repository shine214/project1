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


if __name__ == '__main__':
    nomal = Zombia('nomal', 5, 10)
    print(f'僵尸初始 {nomal}')
    nomal.beAttacked()
    print(f'僵尸被攻击后 {nomal}')
    nomal.walk()
    print(f'僵尸行进后 {nomal}')
