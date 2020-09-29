# 快速排序
"""
同样使用分治法，
"""


def quick_sort(list, left, right):
    mid = list[left]
    start = left # 起点，终点
    end = right
    if left >= right:
        return
    while end > start:
        while end > start and list[end] > mid:
            end -= 1
        list[start] = list[end]
        while end > start and list[start] < mid:
            start += 1
        list[end] = list[start]

    list[start] = mid

    quick_sort(list, left + 1, right)
    quick_sort(list, left, right - 1)

    return list


if __name__ == '__main__':
    list = [22,21,6,225,61]
    print(quick_sort(list, 0, len(list) - 1 ))