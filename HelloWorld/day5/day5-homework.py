def default_para_func(name, age, height=175, weight=200):
    print(name, age, height, weight)


def multi_para_func(name, *args, **kwargs):
    print(name, args, kwargs)


class Dog:
    def __init__(self, name, color, meet):
        self.name = name
        self.color = color
        self.meet = meet
        print(name, color, "because meet", meet, "so:")
        if (self.meet == "熟人"):
            self.swing()
        elif (self.meet == "生人"):
            self.bark()

    def swing(self):
        print("摇尾巴")

    def bark(self):
        print("狗叫")


if __name__ == '__main__':
    default_para_func('缺省参数', 16, 200)
    # 多值参数直接传递
    multi_para_func('多值参数直接传递', 1, 2, 3, 4, 5, a=3, b=2)
    # 多值参数拆包传递
    a = (1, 2, 3, 4, [2, 3], ',')
    c = [1, 2, 3, 4, 5]
    d = {1, 23, 4}
    b = {'a': 1, 'b': 2}
    multi_para_func('多值参数拆包传递', *d, **b)  # 位置参数拆包的话不仅限于元组，列表集合都可以,但是kw参数应该只能是字典
    mike = Dog("mike", "yellow", "熟人")
    david = Dog('david', 'black', "生人")
