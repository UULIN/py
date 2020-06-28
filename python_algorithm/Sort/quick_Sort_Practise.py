"""
快速排序
核心思想还是分而治之的思想
是插入排序的优化版，也是最快的排序方法之一，但是对数据量小的时候不是很友好
时间复杂度是O(nlogn)
首先找一个参照值，先从右往左开始遍历，比参照值大的放右边，比参照值小的放左边
对分成的两个队列递归的进行下一次排序，直到所有值有序为止
因为会对子序列进行值的交换，所以该算法为不稳定算法
"""


# 以第一个点为参考值
def quick_sort(arr, start, end):
    # 不要忘记设定退出条件，这样会导致递归太深
    if start > end:
        return
    mid = arr[start]
    # 设定两个游标，low，high
    low = start
    high = end
    while high > low:
        # 两个游标不重合
        # 开始从右往左遍历
        while high > low and arr[high] >= mid:  # 如果arr[high] 大于游标值，则左移
            high -= 1
        # 直到找到小于游标值的点，将游标与arr[high]进行替换
        arr[low] = arr[high]
        # 开始从左往右遍历
        while high > low and arr[low] < mid: # 如果arr[low]小于游标值，右移一位
            low += 1
        # 直到找到大于游标值的值，将改点填入arr[high],此时arr[low]为空
        arr[high] = arr[low]

    # 最后将 mid值放入arr[low]
    arr[low] = mid
    # 递归进行后续排序
    quick_sort(arr, start, low - 1)
    quick_sort(arr, low + 1, end)
    return arr


if __name__ == '__main__':
    test_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]
    print(quick_sort(test_list, 0, len(test_list) - 1))
