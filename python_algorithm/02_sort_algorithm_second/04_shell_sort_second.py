# 希尔排序，时间复杂度O(n2) 算法不稳定
"""
思想的话是将列表元素进行规定步长排序，最后步长为1时已接近排好序的列表，这时使用快排，效率最高
"""


def shell_sort(list):
    length = len(list)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            # 设定无序列表的第一个值为temp
            temp = list[i]
            # 设定有序列表的最后一个值的下标为j
            j = i - gap
            while j >= 0 and list[j] > temp:
                list[j + gap] = list[j]
                list[j] = temp
                j -= gap
        gap = gap // 2

    return list


if __name__ == '__main__':
    list = [21,41,2,123,5,2]
    print(shell_sort(list))
