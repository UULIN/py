"""
归并排序
"""
from math import floor

merge_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]


# 合并两个数据，产生一个已经排序好的新的数组
def merge(left, right):
    # 设定临时列表，用来存放比较后的列表的值
    result = []
    # 设定指向两个数组的指针，起始为0
    i = j = 0
    while i < len(left) and j < len(right):# 设定指针的边界条件，如果不满足，则直接将另一个数组的值追加进临时数组即可
        # 如果left的下标i > right的下标j
        if left[i] >= right[j]:
            # 将right中的第j个元素放到result中
            result.append(right[j])
            # j的下标右移一位
            j += 1
        else:
            result.append(left[i])
            i += 1
    # 将其中一个数组剩余的值添加进result列表即可
    result += left[i:]
    result += right[j:]
    return result


# 将数组分开
def merge_Sort(arr):
    mid = floor(len(arr) / 2) # 取中间值
    # 如果列表已经是最小单元，返回这个列表
    if len(arr) <= 1:
        return arr # 切分为不可再分的单元
    # 对arr进行“分”的处理
    return merge(merge_Sort(arr[0:mid]), merge_Sort(arr[mid:]))


if __name__ == '__main__':
    print(merge_Sort(merge_list))

