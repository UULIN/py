# 快速排序 时间复杂度O(nlogn) 空间复杂度O(logn) 不稳定
"""
 采用递归与分治的思想，选取一个哨兵作为基准值，比哨兵小的放在左边，比哨兵大的放在右边，最后将基准值与
"""


def quick_sort(list, left, right):
    # 设定哨兵为left
    temp = list[left]
    # 设定起始值左游标为start,右为right
    start, end = left, right
    length = len(list)
    if left >= right:
        return
    while start < end:
        # 从右往左开始遍历
        while start < end and list[end] > temp:
            end -= 1
        list[start] = list[end]
        while start < end and list[start] < temp:
            start += 1
        list[end] = list[start]
    list[start] = temp

    quick_sort(list, left, right - 1)
    quick_sort(list, left + 1, right)
    return list


if __name__ == '__main__':
    list = [12,2,4512,21,45,245]
    print(quick_sort(list,0, len(list) - 1))