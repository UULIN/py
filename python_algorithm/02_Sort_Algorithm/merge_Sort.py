"""
归并排序
"""
from math import floor

merge_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]


# 先治再分
def merge(left, right):
    temp_list = []
    while left and right:
        if left[0] > right[0]:
            temp_list.append(right.pop(0))
        else:
            temp_list.append(left.pop(0))
            print([1], left,right,temp_list)
    while left:
        temp_list.append(left.pop(0))
        print([2], left, right,temp_list)
    while right:
        temp_list.append(right.pop(0))
        print([3],left, right,temp_list)
    return temp_list


# 分
def merge_Sort(arr):
    gap = floor(len(arr) / 2)
    if gap < 2:
        return arr
    left, right = arr[0:gap], arr[gap:]
    print([1231231],merge_Sort(left), merge_Sort(right))
    return merge(merge_Sort(left), merge_Sort(right))


if __name__ == '__main__':
    print(merge_Sort(merge_list))