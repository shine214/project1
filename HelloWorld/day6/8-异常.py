# 异常捕获
def exception1():
    try:
        # 试图通过输入一个无法解析的对象，例如函数、文件对象等
        num = open('file.txt', 'r')  # 这里尝试打开一个文件并赋值给 num
        print(8 / num)  # 这里会抛出 TypeError，因为 num 是文件对象
    except ZeroDivisionError:
        print('除数为零')
    except ValueError:
        print('请输入整形数据类型')
    except Exception as e:
        print(e)  # 捕获其他所有未被专门捕获的异常


# 异常传递
def exception2():
    print("begin exception2")
    exception3()
    print("end exception2")


def exception3():
    print("begin exception3")
    x = 1 / 0
    print("end exception3")


# 异常抛出
def exception4():
    pwd = input("请输入至少八位密码")
    if (len(pwd) >= 8):
        return pwd
    print('主动抛出异常')
    ex = Exception("密码长度不够")
    raise ex


def exception5():
    try:
        print(exception4())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # exception1()

    # try:
    #     exception2()
    # except Exception as e:
    #     print(e)

    # exception5()

    ex = Exception('你的脑子有毛病')
    print(ex)
    print(type(ex))
