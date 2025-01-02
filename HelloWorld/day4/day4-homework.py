# 2
def func2():
    a = [1, 2, 3]
    b = [2, 3, 4]
    c = list(set(a) & set(b))
    print(c)


# 3
def func3():
    a = [1, 2, 2, 2, 2, 2, 2, 3]
    b = set([x for x in a if a.count(x) > len(a) / 2])
    print(b)


def func4():
    pass
    # a = (1, 2, 3)
    # print(a[0])
    # a[0] = 4
    # print(a[0])
    # 相同点：可遍历
    # 不同点： 列表和元组可随机访问 列表和字典可修改


def func5():
    a = (1, 2, 3)
    b = {4, 5, 6}
    c = list(a) + list(b)
    print(c)


def func6():
    a = [1, 2, 3, 4, 5, 6]
    a.insert(0, 0)
    # a.insert(9,8) # insert超出长度范围，就会自动插入到最后
    a.append(7)
    print(a)


def func7():
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    a.reverse()
    print(a)


def func8():
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    a.reverse()
    print(a.index(5))


def func9():
    a = [True, False, 0, 1]
    # True 和1 等价 0和false等价，相同元素,甚至再set里会被去重
    for i in a:
        print(a.count(i))
    b = set(a)
    print(b)


def func10():
    a = [True, 1, 0, 'x', None, 'x', False, 2, True]
    for i in range(a.count('x')):
        a.remove('x')  # remove 只删一个，哪怕有重复的
    print(a)


def func11():
    a = [True, 1, 0, 'x', None, 'x', False, 2, True]
    a.pop(4)  # pop用于知道索引号的删除
    print(a)


def func12():
    # pop完了以后下标会变化，所以最好是从下标大的开始
    a = [True, 1, 0, 'x', None, 'x', False, 2, True]
    for i in range(len(a) - 1, -1, -1):
        if i % 2 == 0:
            a.pop(i)
    print(a)


def func13():
    a = [True, 1, 0, 'x', None, 'x', False, 2, True]
    a.clear()
    print(a)


def func14():
    a = [3, 0, 8, 5, 7]
    a.sort()
    print(f'升序{a}')
    a.sort(reverse=True)
    print(f'降序{a}')


def func15():
    a = [3, 0, 8, 5, 7]
    for i in range(len(a)):
        if (a[i] > 5):
            a[i] = 1;
        else:
            a[i] = 0;
    print(a)


def func16():
    # 两种遍历方法
    a = ['x', 'y', 'z']
    for i in range(len(a)):
        print(i, a[i])
    for i in a:
        print(a.index(i), i)


def func17():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = a[::2];
    c = a[1::2]
    print(a, '\n', b, '\n', c)


def func18():
    a = [[6, 5], [3, 7], [2, 8]]
    a.sort()
    print(a)


def func19():
    # 列表中间插入列表
    a = [1, 4, 7, 2, 5, 8]
    b = ['x', 'y', 'z']
    a = a[:3] + b + a[3:]
    print(a)


def func20():
    a = [x for x in range(5, 50)]
    print(a)


def func21():
    pass


def func22():
    # zip方法
    a = ['x', 'y', 'z']
    b = [1, 2, 3]
    print(list(zip(b, a)))


def func23():
    a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print([x for x in a.keys()])


def func24():
    a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print([x for x in a.values()])


def func25():
    a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print([x for x in a.items()])


def func26():
    a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    a['David'] = 19
    a['Cecil'] = 17
    print(a)


def func27():
    a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    del a['Beth']
    print(a)
    a.clear()
    print(a)


def func28():
    a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print('David' in a, 'Alice' in a, 'Beth' in a, 'Cecil' in a)


def func29():
    a = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    for i in a.items():
        print(i)


def func30():
    pass


def func31():
    # 快速生成value相同的字典，可以是字符串分割，也可以是可迭代对象遍历
    a = {}.fromkeys('A B C D E F G H I J K'.split(), 0)
    b = {}.fromkeys([1, 2, 3, 4, 5], 0)
    print(a)
    print(b)


def func32():
    # 字典更新需要用以元组为元素的列表
    a = [['a', 1], ['b', 2]]
    b = (('x', 3), ('y', 4))
    c = [('abc', 1)]
    d = dict(a)
    e = dict(b)
    print(e)
    e.update(c)
    print(e)


def func33():
    a = (1, 2)
    b = (3, 4)
    print(a + b)


def func34():
    x, y, z = (1, 2, 3)
    print(x, y, z)


def func35():
    a = ('A', 'B', 'C')
    print(a.index('C'))


def func36():
    a = (2, 5, 2, 3, 4)
    print(a.count(2))


def func37():
    a = ('A', 'B', 'C')
    print('C' in a)


def func38():
    # 元组不能修改，想要插入必须这样写，如果只插入一个元素不要忘记逗号
    a = (2, 5, 3, 7)
    b = a[:1] + (9,) + a[1:]
    print(b)


def func39():
    a = set()
    b = set().union(['a', 'b', 'c'])
    a.update(('x', 'y', 'z'))
    print(b)
    print(a)


def func40():
    # 空 set是表现为 set()的形式 而非{}
    a = {'z', 'y', 'x'}
    a.remove('z')
    a.update('w')
    a.clear()
    print(a)
    print(type(a))
    b = {}
    print(b)
    print(type(b))


def func41():
    a = {'a', 'b', 'c'}
    b = {'b', 'e', 'c'}
    print(a - b)


def func42():
    a = {'a', 'b', 'c'}
    b = {'d', 'e', 'f'}
    print(a & b)


def func43():
    a = {'a', 'b', 'c'}
    b = {'d', 'e', 'c'}
    print(a | b)
    # & == intersection 都是取并集
    print(a & b == a.intersection(b))


def func44():
    # 雨或非优先级小于加减
    a = {'a', 'b', 'c'}
    b = {'d', 'e', 'c'}
    c = (a | b) - (a & b)
    print(c)
    # different 理解为 a区别于b 指明 a中独立的部分
    print(a.difference(b))


def func45():
    a = {'a', 'b', 'c'}
    b = {'d', 'e', 'c'}
    if a.intersection(b):
        print(a.intersection(b))
    else:
        print('no')


def func46():
    a = {'a', 'c'}
    b = {'d', 'c', 'e', 'a'}
    print(a.issubset(b))


def func47():
    a = [1, 2, 5, 2, 3, 4, 5, 'x', 4, 'x']
    print(list(set(a)))


def func48():
    a = 'abCdEfg'
    print(a.lower())
    print(a.upper())
    # 大小写互换 swapcase
    print(a.swapcase())


def func49():
    a = 'abCdEfg'
    print(a.islower())
    print(a.isupper())
    print(a.capitalize()[0] == a[0])


def func50():
    a = "this，is1pytho，you"
    print(a.capitalize())
    # title 把每一个单词都首字母大写（单词可以以各种形式分割，甚至是数字）
    print(a.title())


def func51():
    a = "this is python"
    print(a.startswith('this'))
    print(a.endswith('python'))


def func52():
    a = "this is python"
    print(a.count('is'))


def func53():
    a = 'this is python'
    print(a.index('is'), a.rindex('is'))


def func54():
    a = 'this is python'
    print(a.split())


def func55():
    a = 'blog.csdn.net/xufive/article/details/102946961'
    print(a.split())
    print(a.split('/'))


def func56():
    a = '2.72, 5, 7, 3.14'.split(',')
    b = list()
    for i in a:
        if '.' in i:
            b.append(float(i))
        else:
            b.append(int(i))
    print(b)
    conv = lambda x: float(x) if '.' in x else int(x)
    print(list(map(conv, a)))


def func57():
    a = 'adS12K56'
    print(a.isalnum(), a.isalpha(), a.isdecimal())


def func58():
    a = "this is python"
    b = a.replace('is', 'are')
    c = b.replace('this', 'these')
    print(c)


def func59():
    a = '\t python \n'
    print(a)
    a.lstrip()
    a.rstrip()
    a.strip()
    print(a)


def func60():
    # 对其操作
    a = ['ok', 'hello', 'thank you']
    l = len(a[2])
    for i in a:
        print(i.ljust(l))
    for i in a:
        print(i.rjust(l))
    for i in a:
        print(i.center(l))


def func61():
    a = ['15', '127', '65535']
    l = max(len(x) for x in a)
    for i in a:
        print(i.rjust(l, '0'))
    for i in a:
        print(i.ljust(l, '0'))
    for i in a:
        print(i.center(l, '0'))


def func62():
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    print('|'.join(a))  # 这个join好像只能用给字符串


def func63():
    a = "12345"
    print(','.join(a))


def func64():
    number = input()
    print(f'mobile:{number}')


def func65():
    time = input().split()
    print('-'.join(time[:3]) + ' ' + ':'.join(time[3:]))


def func66():
    a = 3.1415926
    b = 2.7182818
    print('{:.4f} {:.4f}'.format(a, b))


def func67():
    a = 0.00774592
    b = 356800000
    print("{:e} {:e}".format(a, b))


def func68():
    a = [0, 1, 2, 3.14, 'x', None, '', list(), {5}]
    b = [bool(x) for x in a]
    print(b)


def func69():
    print(ord('a'), ord('A'))


def func70():
    print(chr(57), chr(122))


def func71():
    a = [3, 'a', 5.2, 4, {}, 9, []]
    b = [x for x in a if (type(x) == int or type(x) == float) and x > 3]
    print(b)


def func72():
    a = [[1], ['a', 'b'], [2.3, 4.5, 6.7]]
    b = [y for x in a for y in x]
    print(b)


def func73():
    values = [1, 2, 3, 4, 5]
    keys = ['a', 'b', 'c', 'd', 'e']
    dict1 = dict(zip(keys, values))
    print(dict1)


def func74():
    s = list(range(10))
    b = [x for x in range(10)]
    print(sum(s))
    print(sum(b))


func74()
# func73()
# func72()
# func71()
# func69()
# func70()
# func68()
# func67()
# func66()
# func65()
# func64()
# func63()
# func62()
# func61()
# func60()
# func58()
# func57()
# func56()
# func55()
# func54()
# func53()
# func52()
# func51()
# func50()
# func49()
# func48()
# func59()
# func47()
# func46()
# func45()
# func44()
# func43()
# func42()
# func41()
# func40()
# func39()
# func38()
# func37()
# func36()
# func35()
# func34()
# func33()
# func32()
# func31()
# func30()
# func29()
# func28()
# func27()
# func26()
# func25()
# func24()
# func23()
# func22()
# func21()
# func20()
# func19()
# func18()
# func17()
# func16()
# func15()
# func14()
# func2()
# func3()
# func4()
# func5()
# func6()
# func7()
# func8()
# func9()
# func10()
# func11()
# func12()
# func13()
