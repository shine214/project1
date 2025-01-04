import random
class Sort:
    def __init__(self, n):
        self.n = n
        self.arr = [0]*n
        self.random_data()
        print(self.arr)
    def random_data(self):
        for i in range(self.n):
            self.arr[i] = random.randint(1, 100)
    def partition(self,arr,l,r):
        # 选择基准元素，这里选择最右端的元素作为基准
        pivot = arr[r]
        i = l - 1  # i是小于基准元素的部分的末尾索引
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # 交换q[i]和q[j]，确保小于基准的元素在左边
        arr[i + 1], arr[r] = arr[r], arr[i + 1]  # 将基准元素放到正确的位置
        return i + 1  # 返回基准元素的位置

    def quick_sort(self,arr,l,r):
        if l < r:
            # 获取基准元素的位置
            pivot_index = self.partition(arr, l, r)
            # 对基准左边和右边的部分进行递归排序
            self.quick_sort(arr, l, pivot_index - 1)
            self.quick_sort(arr, pivot_index + 1, r)

sort1 = Sort(10)
lst = [1,6,5,2,7,9,11]
sort1.quick_sort(lst,0,len(lst)-1)
print(lst)

