a = 2;
b = 2;
print(a is b)
a = 'hello'
print(id(a))
print(id(b))
del a
print(id(b))
b = 'hello'
print(id(b))
