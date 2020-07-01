"""
二分查找
时间复杂度为O(logn)，空间复杂度为O(1)
二分查找也叫做折半查找，是一种在有序数组中查找某一特定元素的查找算法。
查找过程从中间元素开始。如果中间元素正好是要查找的元素，则查找过程结束。
"""


def binary_search1(arr, value):
    """
    binary_search1 寻找与value相等的值返回下标，没有则返回-1
    :param arr:
    :param value:
    :return:
    """
    # 初始化左右游标
    left, right = 0, len(arr) - 1

    while right >= left:
        mid = (left + right) // 2

        if arr[mid] > value:
            right = mid - 1
        elif arr[mid] < value:
            left = mid + 1
        else:
            return mid
    return -1


def binary_search2(arr, value):
    """
    对同一个列表做二分查找，找出在列表中不大于关键字的最大值。
    :param arr:
    :param value:
    :return:
    """
    left, right = 0, len(arr) - 1
    # 不使用等于原因是如果 左右指针相等时，代表查找已经完成了，此时不进行结束的化无法结束循环
    while right > left:
        # 如果不进行加1操作，若left和right相邻时，mid的平均值则永远 = left，此时循环则永远无法结束
        mid = (left + right + 1) // 2
        if arr[mid] <= value:
            left = mid
        else:
            right = mid - 1
    return arr[mid]

if __name__ == '__main__':
    test_list = [2, 5, 6, 8, 12, 15, 17, 23, 27, 31, 39, 40, 45, 56, 79, 90]
    value = int(input("please input your goal_value: "))
    print(binary_search2(test_list, value))