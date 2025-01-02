import random


def partition(q, l, r):
    # 选择基准元素，这里选择最右端的元素作为基准
    pivot = q[r]
    i = l - 1  # i是小于基准元素的部分的末尾索引
    for j in range(l, r):
        if q[j] <= pivot:
            i += 1
            q[i], q[j] = q[j], q[i]  # 交换q[i]和q[j]，确保小于基准的元素在左边
    q[i+1], q[r] = q[r], q[i+1]  # 将基准元素放到正确的位置
    return i + 1  # 返回基准元素的位置


def quick_sort(q, l, r):
    if l < r:
        # 获取基准元素的位置
        pivot_index = partition(q, l, r)
        # 对基准左边和右边的部分进行递归排序
        quick_sort(q, l, pivot_index - 1)
        quick_sort(q, pivot_index + 1, r)


if __name__ == '__main__':
    q = [random.randint(0, 100) for _ in range(10)]  # 生成10个随机数
    print("Original list:", q)
    quick_sort(q, 0, len(q) - 1)
    print("Sorted list:", q)