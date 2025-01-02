use_dict = {"name": "xiaoming", "age": 18, "gender": True, "height": 175}
# print(use_dict)

# #遍历字典的键值对
# for i in use_dict.items():  # 以元组方式（每组kv一个元组）
#     print(i)
# for k, v in use_dict.items(): #以字符串方式
#     print(f'key {k} value {v}')

# #字典不能随机访问
# print(use_dict[0])

# # 遍历字典的键
# for i in use_dict:
#     print(i)

# #copy相当于复制出一份（类似软链接） 赋值是直接把新的指针挂到原字典上（类似硬链接）
# new1_use_dict = use_dict.copy();
# new2_use_dict = use_dict
# print(new1_use_dict)
# print(new2_use_dict)
# print(id(use_dict), id(new1_use_dict), id(new2_use_dict))

# # 字典增加、修改（直接给键赋值、没有的话会自动新增）
# use_dict['weight'] = 200
# print(use_dict)
# use_dict['weight'] = 230
# print(use_dict)

# # 字典删除
# print(use_dict.pop('height'))  # pop的返回值是删除的key对应的value,必须有参数传入
# del use_dict["age"] # 无返回值
# print(use_dict)

# 合并字典
# temp_dict = {"height": 170, "age": 20, "weight": 290}
# use_dict.update(temp_dict)  # update方法 有就更新 没有就添加
# print(use_dict)

# 字典列表（列表中的元素是字典）
# class1 = [{"name": "xiaoming", "age": 18, "gender": True, "height": 175},
#           {"name": "xiaohong", "age": 20, "gender": False, "height": 160},
#           {"name": "xiaogang", "age": 25, "gender": True, "height": 188}]
# for student_info in class1:
#     for value in student_info.values():
#         print(value)
