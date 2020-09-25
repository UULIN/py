# 希尔排序
"""
希尔排序是插入排序的优化版，插入排序在几乎已排好序的情况下排序效率是非常高的，但是步长为1时一般都是低效率的，我们要做的是尽量的
在步长为1的情况下使列表尽量排好序
"""

def shell_sort(list):
    length = len(list)
    # 确定步长
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            # 已排序列表的最后一个值的下标
            j = i - gap
            # 未排序列表的第一个值temp
            temp = list[i]

            while j >= 0 and list[j] > temp:
                list[j + gap] = list[j]
                list[j] = temp
                j -= gap

        gap = gap // 2

    return list


if __name__ == '__main__':
    list = [22,21,6,225,61]
    print(shell_sort(list))
