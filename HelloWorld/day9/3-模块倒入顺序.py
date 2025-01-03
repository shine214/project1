import sys
print(sys.path)
sys.path.append('test_module')
print(sys.path)
import my_module #这个红波浪线是pycharm的小bug 不必理会
#这个模块的包与当前文件的位置平级，所以直接找是找不到该模块的
#需要预先将这个包导入进path，然后才能找到
my_module.test1()
