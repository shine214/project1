#1
#1
# pack __init__:
# from . import rcvd_message
# from . import send_message

import pack1

pack1.send_message.send()
txt = pack1.rcvd_message.rcvd()
print(txt)


#2、5
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

#3
import os
# 删除非空目录需要用shutil
import shutil


#  列出指定目录下的所有文件和子目录
def list_dir():
    l_dir = os.listdir()
    print(l_dir)


def get_cwd():
    print(os.getcwd())


def abs_path():
    """获取文件或目录的绝对路径"""
    absolute_path = os.path.abspath('file1.txt')
    print(absolute_path)


def get_size():
    file_size = os.path.getsize('file1.txt')
    print(file_size)


def make_dir():
    """
    创建新目录
    """
    os.mkdir('./new_dir')


def if_exist():
    """
    判断文件目录是否存在
    """
    path = './new_dir'
    # 判断文件路径是否存在
    if os.path.exists(path):
        print('文件路径存在')
    else:
        print('文件路径不存在')

    if os.path.isdir(path):
        print('该文件是目录文件')
    else:
        print('不是目录文件')


def remove_dir():
    """
    删除目录
    """
    # 删除非空目录
    os.rmdir('./new_dir')

    # 删除多级空目录
    os.removedirs('./new_dir')

    # 删除非空目录
    shutil.rmtree('./new_dir')


def change_dir():
    os.chdir('./new_dir')
    print(os.getcwd())


def rename_dir():
    os.rename('./new_dir', './old_dir')


if __name__ == '__main__':
    # make_dir()
    # change_dir()
    get_cwd()
    abs_path()
    get_size()



#4
# import sys

f = open('wjn.txt')


def print_txt(txt):
    print(txt)


# while True:
#     line = f.readline()
#     file_wjn = open(line + 'txt', 'w+', encoding='utf8')
#     file_wjn.write("wjnsb")
#     print(line, end='')
#     if not line:
#         break
a = ''
print(print_txt(a))


#6


def dfs(path):
    for i in os.listdir(path):
        full_path = os.path.join(path, i)
        if(os.path.isdir(full_path)):
            dfs(full_path)
        else:
            print(full_path)
dfs(os.getcwd())
