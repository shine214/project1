set1 = {1, 2, 3}
set4 = {2, 3, 4}
set5 = {3, 4, 5}
set2 = {}  # 空集合会被认为是空字典
set3 = set()  # 定义空集合
# 集合不支持随机访问
print(1 in set1)  # 判断元素是否在集合中

# 集合的交集
result = set1.intersection(set4, set5)
print(result)
print(set1.isdisjoint(set4))
