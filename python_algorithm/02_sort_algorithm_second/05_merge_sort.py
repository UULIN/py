# 归并排序
"""
采用递归思想和二分思想，首先将列表拆分为不可再分的单元，然后将单元进行merge操作，将较小的值放入临时列表，剩余的值进行追加
"""


# 首先我们来写一个分的操作,采用提柜发
def merge_sort(list):

    # 二分法，定义序列的长度
    length = len(list)
    # 设定退出的条件，如果length <= 1,则表示列表为不可分割的最小单元，返回list即可
    if length <= 1:
        return list
    # 确定中位数，进行左右分割
    mid = length // 2

    # 采用递归的方式进行数据分割并排序
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))


# merge的操作，将已分割的数组进行排序并合并
def merge(left, right):
    # 定义一个临时的列表，用来存放已排序好的数据
    temp_list = []
    # 设定两个待排序序列的下标为i, j
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp_list.append(left[i])
            i += 1
        else:
            temp_list.append(right[j])
            j += 1
    temp_list += left[i:]
    temp_list += right[j:]

    return temp_list


if __name__ == '__main__':
    list = [22,21,6,225,61]
    print(merge_sort(list))