"""
Python删除单链表倒数第n个节点
"""
class ListNode:
    def __init__(self, v):
        """

        :param v: 存储数据
        """
        self._val = v
        self._next = None
    def removeLastNth(self, head, n):
        # 防止出现倒数第N个节点正好是第一个节点的情况，需要先创建一个临时节点作为头节点并把两个指针都赋值为链表的头节点
        temp = ListNode(0)
        temp._next = head
        # 设定两个指针，让fast先走n步，然后两个指针同时移动，当fast指向最后一个元素时，slow指向的元素即为倒数第n-1个节点
        fast = slow = temp
        c = 0
        while c < n:
            fast = fast._next
            c += 1
        while fast._next:
            fast = fast._next
            slow = slow._next
        slow._next = slow._next._next
        return temp._next