def file_r():
    """
    只读文件，R或RW都不能新建文件
    """
    file = open("file1.txt", 'r', encoding='utf-8')
    txt = file.read()
    print(txt, type(txt))
    file.close()


def file_rw():
    """
    读写文件
    """
    file = open("file1.txt", 'r+', encoding='utf-8')
    # 这个执行一边read就会把该文件的指针移到最后，然后再执行写操作就会在末尾写入
    # 如果不执行read就会直接在开始的地方写，然后覆盖原内容

    file.read()
    file.write('新编内容')
    txt = file.read()
    file.close()


def file_w():
    """
    以只写的方式打开文件，如果文件存在会被写完之后的文件覆盖，
    如果文件不存在就会新建文件
    """
    f = open("file2.txt", 'w', encoding='utf-8')
    f.write('这是通过W方式创建的文件')
    f.close()


def file_wr():
    f = open("file3.txt", 'w+', encoding='utf-8')
    f.write('这是通过WR方式创建的文件')
    # seek 修改文件指针的位置
    # utf-8的中文字符占3B，所以这个offset如果不是3的整数倍就会报错
    # seek(offset，whence) whence 0表示文件起始， 1表示当前位置， 2表示文件末尾（这时的offset就会是往前走）
    f.seek(3, 0)
    txt = f.read()
    print(txt)
    f.close()


def file_r_by_lines():
    """
    按行读取 readline(limit) limit 参数代表要读取的文件内容大小
    """
    f = open("file3.txt", 'r', encoding='utf-8')
    while True:
        txt = f.readline()
        # 如果读完了，那么txt为空，空字符串=False
        if not txt:
            break
        # 这里写end = ‘“ 是因为按行读取本身末尾就自带一个换行，如果不加end就会变成换两行
        print(txt, end="")

    f.close()


def file_seek_b():
    """
    只有在二进制打开文件的模式下才可以用seek中的负偏移量
    """
    file = open("file3.txt", 'rb+')
    file.seek(5, 0)
    file.seek(-1, 1)
    txt = file.read()
    print(txt)


if __name__ == '__main__':
    # file_wr()
    # file_r_by_lines()
    file_seek_b()
