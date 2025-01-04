import copy
class Person:
    def __init__(self, name,pack):
        self.name = name
        self.pack = pack
person = Person('xiaoming',[10,20,30,40])
new_person = copy.copy(person)

#浅拷贝
print('-'*50+'浅拷贝'+'-'*50)

a = [1,2,[3,4]]
b = copy.copy(a)

#浅拷贝在类中也是如此，如若类实例作为浅拷贝的对象，那么更改实例中的可变数据类型，二者就会同时更改，更改实例中的不可变数据类型，则会相互独立
new_person.pack[3] = 50
print(person.pack)
print(new_person.pack)

print('-'*50+'深拷贝'+'-'*50)

#深拷贝
c = copy.deepcopy(a)
b[2][0] = 99
print(a)
print(c)
