import day3_module


def use_find():
    a = [1, 1, 2, 2, 3, 3, 4, 4, 5]
    b = [x for x in a if a.count(x) == 1]
    print(b)


def use_generate():
    a = [x for x in range(21)]
    print(a)


def say_hello(times):
    '''
     用于打印times次Hello
     '''
    print("Hello" * times)


def use_module():
    day3_module.first_print()
    day3_module.second_print()
    day3_module.third_print()


def use_list():
    # 生成一个奇数位为奇数，偶数位为-1的列表
    a = [x if x % 2 == 1 else -1 for x in range(10)]
    print(a)
    a.append(6)
    a.insert(3, 8)
    a.sort()
    a.sort(reverse=True)
    print(a)
    for i in a:
        print(i)


def use_find_plus():
    a = [1, 1, 4, 4, 6, 6, 7, 8]
    b = [x for x in a if a.count(x) == 1]
    print(b)

# use_find()
# use_generate()
# say_hello(3)
# use_module()
# use_list()
# use_find_plus()
