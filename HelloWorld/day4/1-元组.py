tuple_a = ("xiaoming", 18, 12345)

# 可迭代 遍历元组
# for i in tuple_a:
#     print(i)

# 格式化字符串：分组展示元组内的元素（要求个数匹配）
print("姓名%s 年龄%d 学号%d" % tuple_a)

# 单元素的元组表示需要加逗号(否则就会变成元组内元素的数据类型)
tuple_b = (1,)
