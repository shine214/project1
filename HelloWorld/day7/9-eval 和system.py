import os

# eval 用于执行python语句
# os.system() 用于执行系统linux语句

# eval("__import__('os').system('ls')")

# eval还可以读配置，把读如json文件生成的字符串转为字典

f = open('json.txt', 'r', encoding='utf-8')
txt = f.read()
print(txt, type(txt))
# 用eval执行字符串类型的“字典”，就会把它自动转为字典类型
my_dict = eval(txt)
print(type(my_dict))
