import copy

#浅拷贝
a = [1,2,[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)
b[2][0] = 99
print(a)
print(b)
print(c)

print(f'a的地址{id(a)},b的地址{id(b)},c的地址{id(c)}')