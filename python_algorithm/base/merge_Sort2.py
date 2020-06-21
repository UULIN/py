"""
归并排序
"""
from math import floor

merge_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]


# 合并两个数据，产生一个已经排序好的新的数组
def merge(left, right):
    # 设定临时数组
    result = []
    # 设定指向两个数组的指针，起始为0
    i = j = 0
    while i < len(left) and j < len(right):
        # 如果left的下标i > right的下标j
        if left[i] >= right[j]:
            # 将right中的第j个元素放到result中
            result.append(right[j])
            # j的下标右移一位
            j += 1
        else:
            result.append(left[i])
            i += 1

    result += left[i:]
    result += right[j:]
    return result


# 将数组分开
def merge_Sort(arr):
    mid = floor(len(arr) / 2)
    # 如果列表已经是最小单元，返回这个列表
    if mid <= 1:
        return arr
    # 对arr进行“分”的处理
    return merge(merge_Sort(arr[0:mid]), merge_Sort(arr[mid:]))


if __name__ == '__main__':
    print(merge_Sort(merge_list))

