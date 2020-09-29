# 归并排序 时间复杂度O(nlogn),算法为稳定的算法

def merge_sort(list):
    mid = len(list) // 2
    if len(list) <= 1:
        return list
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))


def merge(left, right):
    # 设定游标i,j
    i = j = 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp += left[i:]
    temp += right[j:]
    return temp


if __name__ == '__main__':
    list = [44,2,12,5,222,54]
    print(merge_sort(list))