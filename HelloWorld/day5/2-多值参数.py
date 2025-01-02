# 先position 再*arg 再**kwarg

def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)

    # args 和kwargs都是作为一个元素（元组或字典）
    # 用 * 或 ** 可以把args或kwargs的元组或字典拆成多个元素
    # 然后再传入demo2 就会变成多值参数传参
    print("不带星星")
    demo2(args, kwargs)
    print("带星星")
    demo2(*args, **kwargs)


def demo2(*args, **kwargs):
    print(args)
    print(kwargs)


demo(1, 2, [2, 3, 4], 5, name="小明", age="19")
