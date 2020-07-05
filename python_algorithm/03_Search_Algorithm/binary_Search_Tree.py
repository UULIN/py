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

    # 插入
    def insert(self, data):
        """
        如果二叉搜索树中节点的键值没有与要插入的元素重合，那么一定会有这样一个唯一的空位供新节点插入；
        反之，如果有重合的节点，那么一定会被查找到。这时候，不需要插入，直接 return 退出函数即可。
        :param data:插入的值
        :return:
        """
        exist, n, p = self.search(self._root, self._root, data) # 接受查抄操作的数据
        if exist:# 如果有重合的节点，那么一定会被查找到。这时候，不需要插入，直接 return 退出函数即可
            return
        else:
            new_code = TreeNode(data) # 数据为data的节点不存在，新建一个节点
            if data > p.data: #如果data大于父亲节点，在右孩子的位置插入
                p.right = new_code
            else: # 如果data小于父亲节点，在左孩子的位置插入
                p.left = new_code


    # 查找前驱
    def getlast(self, node, data, maxn):
        """
        :param node:最后的节点node
        :param data: 输入的值
        :param maxn:最大的符合前驱要求的数
        :return:
        """
        if node is None: # 如果当前位置为空，但仍没有查找到与data相等的元素
            return 0, maxn # 返回目前经过路径上最大的符合前驱要求的数
        elif data == node.data: # 找到了与data相等的元素
            if node.left == None:# 且值为data的节点没有左子树
                return 1, maxn # 返回目前经过路径上最大的符合前驱要求的数
            else: # 值为data的节点有左子树
                tmp = node.left # 进入左子树后找到左子树中最大的数
                while tmp.right is not None:
                    tmp = tmp.right
                return 1, tmp # 返回左子树中最大的数（最右边的数）
        elif data < node.data: # 如果data元素小于当前节点的数据，进入左子树
            return self.getlast(node.left, data, maxn)
        else: # data大于当前节点的数据，进入右子树
            if maxn.data < node.data:# 如果当前数据比已经存储在maxn中的前驱要大，更新maxn
                maxn = node
            return self.getlast(node.right, data, maxn)
    # 查找后继
    def getnext(self, node, data, minn):
        if node is None: # 如果当前位置为空，但仍没有查找到与data相等的元素
            return 0, minn
        elif data == node.data: # 如果当前值与data相等
            if node.right == None: # 且值为data的节点没有右子树
                return 1, minn # 返回目前经过路径上最小的符合后继要求的数
            else:# 如果当前节点有右子树
                tmp = node.right # 进入右子树找出右子树中最小的值
                while tmp.right is not None:
                    tmp = tmp.right
                    return 1, tmp #返回右子树中最小的数据(最左边的数据)
        elif data < node.data:# 如果data小于当前节点的数据，进入左子树
            if minn.data > node.data:
                # 如果当前额数据已经比存储在min中的数据要小，更新minn
                minn = node
                return self.getlast(node.left, data, minn)
        else: #如果data大于当前节点的数据，进入右子树
            return self.getlast(node.right, data, minn)


    # 二叉搜索树删除节点
    def delete(self, root, data):
        exist, n, p = self.search(root, root, data)
        if not exist:
            # 要删除的数据不存在
            return '数据不存在'
        else:
            if n.left is None: # 要删除的节点左子树为空
                if n == p.left: # 如果N是左孩子，则把N的左孩子赋值为P的左孩子
                    p.left = n.left
                if n == p.right:
                    p.right = n.left # 如果N是右孩子，则把P的右孩子赋值为N的左孩子
                del n # 删除N
            else:# 左右子树均不为空
                tmp = n.right
                if tmp.left is None:# 如果N的右孩子没有左子树，则N的右孩子就是N的后继
                    n.data = tmp.data
                    n.right = tmp.right
                    del tmp
                else:
                    next = tmp.left
                    while next.left is not None:# 在右子树中查找N的后继
                        tmp = next
                        next = next.left
                    n.data = next.data
                    tmp.left = next.right
                    del next # 删除next
