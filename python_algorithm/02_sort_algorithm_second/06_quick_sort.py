# 快速排序
"""
同样使用分治法，
"""

def quick_sort(list,left,right):
    # 设定退出条件
    if left >= right:
        return
    # 设定一个哨兵起始位置为left
    mid = list[left]
    # 设定high，low
    low = left
    high = right
    # 右游标一直大于左游标
    while low < high:
        # 如果右游标对应的值大于哨兵值，则继续往左移动
        while high > low and list[high] > mid:
            high -= 1
        # 如果比哨兵值小，则将high对应的值放在left处，接下来移动low的值，找到符合条件的放在此处
        list[low] = list[high]
        while high > low and list[low] < mid:
            # 游标向右移动
            low += 1
        list[high] = list[low]
    # 直到交换完成后，两值重合，将哨兵节点对应的值与左游标对应的值进行交换
    list[low] = mid
    # 使用递归的方式继续进行值的遍历与交换
    quick_sort(list,left, right - 1)
    quick_sort(list,left + 1, right)
    return list


if __name__ == '__main__':
    list = [22,21,6,225,61]
    print(quick_sort(list,0, len(list) - 1 ))