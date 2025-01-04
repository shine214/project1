import copy

#1
class Person:
    def __init__(self, name,pack):
        self.name = name
        self.pack = pack
# person = Person('xiaoming',[10,20,30,40])
# new_person = copy.copy(person)
#
# #浅拷贝
# print('-'*50+'浅拷贝'+'-'*50)
#
# a = [1,2,[3,4]]
# b = copy.copy(a)
#
# #浅拷贝在类中也是如此，如若类实例作为浅拷贝的对象，那么更改实例中的可变数据类型，二者就会同时更改，更改实例中的不可变数据类型，则会相互独立
# new_person.pack[3] = 50
# print(person.pack)
# print(new_person.pack)
#
# print('-'*50+'深拷贝'+'-'*50)
#
# #深拷贝
# c = copy.deepcopy(a)
# b[2][0] = 99
# print(a)
# print(c)


#2、3 正则表达式
import re

""" 
正则表达式 单字符： 
    .   匹配任意一个字符（除了\n）
    []  匹配[]中列举的字符 [a-zA-Z0-9]即字母或数字
    \d  匹配数字，即 0-9 decimal
    \D  匹配非数字，即不是数字
    \s  匹配空白，即 空格，tab 键 space
    \S  匹配非空白
    \w  匹配单词字符，即 a-z、A-Z、0-9、_ (汉字) word
    \W  匹配非单词字符

匹配多个字符：
    *       匹配前一个字符出现 0 次或者无限次，即可有可无
    +       匹配前一个字符出现 1 次或者无限次，即至少有 1 次
    ?       匹配前一个字符出现 1 次或者 0 次，即要么有 1 次，要么没有
    {m}     匹配前一个字符出现 m 次
    {m,n}   匹配前一个字符出现从 m 到 n 次

组合起来就是：  '\d*'   '[a-z]+'  '\w{4,20}'

匹配开头结尾：
    ^   匹配字符串开头
    ¥%  匹配字符串结尾

匹配分组：
    |           匹配左右任意一个表达式
    (ab)        将括号中字符作为一个分组
    \num        引用分组 num 匹配到的字符串 : 也就是这个正则表达式中第num个分组的字符串
    (?P<name>)  分组起别名
    (?P=name)   引用别名为 name 分组匹配到的字符串


([^-]*) 代表没有遇到小横杠-就一直进行匹配，一直匹配下去：

    伴随*就是可以是0个元素
    若是换成+就是至少得是1个元素



"""


def use_match(pattern, string):
    """
    match的用法就是在给定txt的开头找出符合pattern的字串
    返回的是group对象，想要进一步处理需要 .group
    """
    result = re.match(pattern, string)
    print(result)


def use_findall(pattern, string):
    """
    findall的用法是找到字符串中所有满足pattern的子串
    返回的是list
    """
    result = re.findall(pattern, string)
    print(result)


def use_search(pattern, string):
    """
    search的用法是找到字符串中第一个满足pattern的子串
    返回的是group
    """
    result = re.search(pattern, string)
    print(result.group())


def use_finditer(pattern, string):
    """
    finderiter的用法就是迭代器，可以通过next(result)来逐个去遍历在字符串中符合pattern的子串
    """
    result = re.finditer(pattern, string)
    print(next(result).group())
    print(next(result).group())
    print(next(result).group())
    print(next(result).group())


def add(temp):
    """
    处理sub的函数，temp为找到的子串，通过一系列的操作最后将结果返回用于替换原来的子串
    """
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def use_sub(pattern, string):
    """
    sub用于替换字符串中的满足pattern的子串，参数1是pattern 参数2是用来替换的子串（也可以是方法），参数3是文本
    """

    # 直接替换
    result = re.sub(pattern, 'xyz', string)
    print(result)

    # 用自定义函数去替换
    # 这个自定义函数需要定义一个传参将找到的子串传入到函数中操作，并且最后用返回的新子串替换掉原来的子串
    pattern2 = '\d+'
    result2 = re.sub('\d+', add, string)
    print(result2)


def use_split(pattern, string):
    """
    split方法就是用pattern来分割字符串，并返回列表
    """
    print(string)
    result = re.split(' |:|/', string)
    print(result)


if __name__ == '__main__':
    # txt = 'abcd ss abcd8129abcd'
    # pattern = 'abcd'
    # # use_match(pattern,txt)
    # # use_findall(pattern,txt)
    # # use_search(pattern,txt)
    # # use_finditer(pattern,txt)
    # # use_sub(pattern,txt)
    # pattern = ' |:|/'
    # txt = '2022 2023:2024/2025'
    # use_split(pattern, txt)
    pass
