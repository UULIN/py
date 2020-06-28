"""
堆排序
"""


# 向下调整的函数，传入的数据为堆，堆顶节点的编号和堆末尾的界限值
def Heapify(heap, start, end):
    father = start
    son = father * 2 # son存储较大的子节点的编号，初始化为左子节点
    while end >= son: # 当目前数据所处的节点还有子节点时，继续循环调整
        # 存在子节点且左右节点进行比较
        if end >= son + 1 and heap[son + 1] > heap[son]:
            # 如果存在右节点且其值大于左子节点的值，son存储右子节点的编号
            son += 1
        if heap[son] > heap[father]: # 如果子节点值大于父节点值
            # 进行值的交换
            heap[father], heap[son] = heap[son], heap[father]
            # 继续进行下一层调整
            father = son
            son = father * 2
        else:
            # 如果所有父节点大于等于子节点，则交换完成
            return


def HeapSort(heap):
    # 初始化最大顶函数
    heap.insert(0, 0)
    # 堆顶编号从0开始，在位置0处插入一个数使得堆中元素的编号与在数组中的下标一样
    for i in range(len(heap) - 1 // 2, 0, -1): # 从最底层最右侧的非叶子节点开始调整
        Heapify(heap, i, len(heap) - 1)
    # 从堆末尾开始进行元素交换
    for i in range(len(heap) - 1, 0, -1):
        heap[1], heap[i] = heap[i], heap[1]
        Heapify(heap, 1, i-1)
    return heap


if __name__ == '__main__':
    test_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]
    print(HeapSort(test_list))
