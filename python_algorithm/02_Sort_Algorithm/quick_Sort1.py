"""
快速排序
"""


def quick_sort(list, start, end):
    # 设定退出条件
    if start >= end:
        return
    # 选定一个起始位置为参考值
    mid = list[start]
    low = start # 设定一个从左往右的游标
    high = end  # 设定一个从右往左的游标
    # 开始进行筛选
    while high > low:
        # 先从右往左
        while high > low and list[high] >= mid:
            high -= 1
        # 直到找到一个值去替换low的位置，此时high 的值为空
        list[low] = list[high]
        # 再从左往右
        while high > low and list[low] < mid:
            low += 1
        # 找到一个大于mid值，放在上面的high的位置上面
        list[high] = list[low]

    list[low] = mid
    # 左边的序列继续进行快速排序
    quick_sort(list, start, end - 1)
    # 右边
    quick_sort(list, start + 1, end)
    return list


if __name__ == '__main__':
    quick_list = [11,333,45453,1231,12312,566,1,2335,78,2]
    print(quick_sort(quick_list,0 , len(quick_list) -1))

