"""
<<<<<<< Updated upstream
1.先确定一个基准数，然后按照比较规则，如本例是升序排列，则将比基数大的放到右边，比基数小的放到左边。
2.接下来各边重复步骤1，直到全部排序完毕。
"""
quick_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]


def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end: # 递归的退出条件
        return
    mid = alist[start] # 设定起始的基准元素
    low = start # low为序列左边在开始位置的由左向右移动的游标
    high = end # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low和high未重合，high指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high] # 走到此位置时high指向一个比基准元素小的元素，将high指向的元素放到low的位置上，此时high指向的元素为空，接下来移动low将符合条件的值放到此处
        # 如果low和high未重合，low指向的元素小于基准元素，则low向右移动
        while low < high and alist[low] < mid:
            low += 1

        alist[high] = alist[low] #此时low指向的一个比mid大的元素，将low指向的元素放到high空着的位置上，此时low指向的位置空着，之后再进行下一次循环，将high符合元素的位置放到此处
    # 退出循环后low与high重合，此时所指位置为基准元素的正确位置，左边的元素都比基准小，右边的元素都比基准大
    alist[low] = mid
    # 对基准左边的子序列进行快速排序
    quick_sort(alist,start,end - 1)
    # 对基准右边的子序列进行快速排序
    quick_sort(alist,start +1, end)
    return alist


if __name__ == '__main__':
    print(quick_sort(quick_list, 0, len(quick_list)-1))

