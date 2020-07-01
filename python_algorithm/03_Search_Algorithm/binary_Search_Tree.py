class TreeNode:
    """
    二叉搜索树的建立
    二叉搜索树和每一个二叉树一样都有一个存储节点本身数据的变量还有两个存储左右孩子的变量
    """
    def __init__(self, val):
        """

        :param val:根节点本身
        :param _left:左孩子节点
        :param _right:右孩子节点
        """
        self._val = val
        self._left = None
        self._right = None


class BST:
    """
    定义二叉搜索树，假设所有元素都已列表的形式输入，我们可以在类内的init()函数中初始化
    """
    def __init__(self, tlist):
        """
        :param tlist:以列表的形式展现
        """
        self._root = TreeNode(tlist[0]) # 把第一个元素建立为根节点
        for i in tlist[1:]: # 按顺序把剩下的元素用insert插入到列表中
            self.insert(i)

    # 搜索
    def search(self, node, parent, data):
        """
        :param node:最后的节点node
        :param parent:父节点
        :param data:输入的值
        :return:二叉搜索树中查找是否有键值为 val 的节点。如果有，返回节点的位置；如果没有，返回 0
        """
        if node is None: # 如果当前节点为空，且仍没有查找到与data相等的元素
            return 0, node, parent
        elif data == node.data: # 找到了与data相等的元素
            return 1, node, parent
        elif data < node.data: # 如果data小于当前节点的元素值，则进入左子节点继续查找
            return self.search(node.left, node, data)
        elif data > node.data: # 如果data大于当前节点的元素值，则进入右子节点继续查找
            return self.search(node.right, node, data)

    # 查找前驱
    def getlast(self, node, data, maxn):
        if node is None: # 如果当前位置为空，但仍没有查找到与data相等的元素
            return 0, maxn # 返回目前经过路径上最大的符合前驱要求的数
        elif data == node.data: # 找到了与data相等的元素


