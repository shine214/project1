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
