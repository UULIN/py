"""
堆排序
"""
# 向下调整,依次传入上层节点的编号，堆末尾界限值编号
def Heapify(heap, start, end):
    # 设定初始父节点为father
    father = start
    # 初始化左侧子节点为son
    son = father * 2
    # 如果堆末尾界限值大于子节点编号，则继续下一步
    while end >= son:
        # 首先进行左右两个子节点值的比较，如果右子节点大于左子节点值，则将son赋值为右子节点
        if end >= son + 1 and heap[son + 1] > heap[son]:
            son += 1
        # 进行子节点与父节点的比较，如果子节点大于父节点，则将位置进行替换
        if end >= son and heap[son] > heap[father]:
            heap[father], heap[son] = heap[son], heap[father]

            # 继续进行下一个二叉树的比较
            father = son
            son = father * 2
        else:
            return

def heapSort(heap):
    # 先进行堆的初始化
    # 要使堆编码和序列索引对应，则先在序列前插入一个值
    heap.insert(0, 0)
    # len(heap) - 1 // 2 代表最右侧非叶子节点的编码，进行由下往上的遍历
    for i in range(len(heap) - 1 // 2, 0, -1):
        Heapify(heap, i, len(heap) - 1)

    # 排序
    for i in range(len(heap) - 1, 0 , -1):
        # 对堆末尾元素进行交换
        heap[1], heap[i] = heap[i], heap[1]
        # 对序列进行重新排序
        Heapify(heap, 1, i - 1)
    # 删除之前插入的0
    heap.remove(0)
    return heap

if __name__ == '__main__':
    test_list = [11, 6743, 4656, 2321, 12, 54, 876, 232]
    print(heapSort(test_list))

