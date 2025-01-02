class Zombia2:
    def __init__(self, name, color='black'):
        self.name = name
        self.__color = color

    def __str__(self):
        return f'name:{self.name} color:{self.__color}'


if __name__ == '__main__':
    nomal = Zombia2('nomal')
    special = Zombia2('special', 'red')
    print(nomal)
    print(special)
    # print(nomal.name,nomal.color)
