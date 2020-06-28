"""
归并排序
分而治之的思想
时间复杂度：O(nlogn)

"""
from math import floor

test_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]


def merge(left, right):
    # 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
    sorted_list = []
    # 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
    i = j = 0
    while i < len(left) and j < len(right):
        # 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
        if left[i] <= right[j]:
            # 将i指向的数字添加到排序列表里面
            sorted_list.append(left[i])
            # 指针增加一位
            i += 1
        else:
            # 重复步骤 3 直到某一指针达到序列尾；
            sorted_list.append(right[j])
            j += 1
    # 将另一序列剩下的所有元素直接复制到合并序列尾。
    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list


def merge_sort(arr):
    mid = floor(len(arr) / 2)
    while mid <= 1:
        return arr
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


if __name__ == '__main__':
    print(merge_sort(test_list))