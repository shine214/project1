lst = [5, 2, 3, 1, 4]
print('sorted基本使用')
print(f'排序后的lst{sorted(lst)},不改变原来的lst{lst}')
print('-'*50)
print('sort使用')
lst.sort()
print(lst)

print(sorted("This is a test string from Andrew".split(), key=str.lower))

student_tuples = [
 ('john', 'A', 15),
 ('jane', 'B', 12),
 ('dave', 'B', 10),
 ]
print('-'*50)
print(sorted(student_tuples,key = lambda x:(x[1],x[2])))

mydict = { 'Li' : ['M',7],
 'Zhang': ['E',2],
 'Wang' : ['P',3],
 'Du' : ['C',2],
 'Ma' : ['C',9],
 'Zhe' : ['H',7] }
print('-'*50)
print(sorted(mydict.items(),key = lambda x:x[1][1]))
#两个排序列
tuples = [(3,5),(1,2),(2,4),(3,1),(1,3)]
#以第一个生序，第二个降序
print(sorted(tuples,key = lambda x:(x[0],-x[1])))