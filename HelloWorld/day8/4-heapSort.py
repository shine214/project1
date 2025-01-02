import random

def adjust_heap(q,pos,lenth):
    """
    调整这个堆成大根堆
    """
    dad = pos
    #先把son定位左孩子
    son = pos*2+1
    while son < lenth:
        if son+1<lenth and q[son]<q[son+1]:
            #看哪个孩子大
            son += 1
        if q[son]>q[dad]:
            q[son],q[dad] = q[dad],q[son]
            #相当于再递归，这里是用数值来实现
            dad = son
            son = dad*2+1
        else:
            #这里意思是父亲比两个孩子都大，那么做大根堆调整的话自然就要结束循环
            break
if __name__ == '__main__':
    q =[]
    for i in range(10):
        q.append(random.randint(1,100))
    print(q)
    length = len(q)
    #如果根节点的下标是0 那么最后一个父亲的下标就是len（q） //2 - 1
    for i in range(len(q)//2-1,-1,-1):
        adjust_heap(q,i,len(q))

    #每次先换然后调整，由于下面都有序，使用只用adjust根节点即可
    for i in range(len(q)-1,0,-1):
        q[0], q[i] = q[i], q[0]
        adjust_heap(q,0,i)

    print(q)
