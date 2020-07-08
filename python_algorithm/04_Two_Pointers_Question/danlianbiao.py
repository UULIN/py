
"""
在两个列表中，相同下标的元素属于链表中的同一个元素。也就是说，链表的第一个元素的值是 1，它在列表 ListValue 中的下标是 0，
则 ListPointer[0] == 3 就是链表的这个元素存储的指针。

这个指针指向下一个元素，也就是 ListValue 中下标为 3 的数值 2。和 2 属于链表中同一个元素的指针是 ListPointer[3]，它指向下一个数值。
以此类推，直到有一个指针的值为 -1，代表它的后面没有其他元素了。ListValue 和 ListPointer 这两个列表合起来就建立了一个模拟链表。

需要注意的是，链表的第一个元素并不一定处于列表下标为 0 的位置。所以，往往还需要一个单独的指针变量来存储第一个元素的位置。这个指针被称为头指针。
1 _0 listpoint[0]=3
2 _3 listpoint[3]=5
3 _5 listpoint[5]=4
4 _4 listpoint[4]=1
5 _1 listpoint[1]=2
6 _2 listpoint[2]=-1
"""

# 遍历单链表
def show_list():
    ListValue = [1, 5, 6, 2, 4, 3]
    ListPointer = [3, 2, -1, 5, 1, 4]
    head = 0  # head是指向链表的第一个元素的指针，需要自己定义
    next = head  # 给next赋初始值

    while next != -1:  # next是指向下一个元素的指针，不等于-1说明后面还有元素
        print(ListValue[next])  # 输出下一个元素中存储的值
        next = ListPointer[next]    # 把指针变为下一个元素中存储的指针


# 单链表插入值

listvalue = [1, 4, 5, 2]
listpoint = [3, 2, -1, 1]
head = 0    # 初始化头指针
num = 3 # num为要插入的元素
next, last = head,head  # 初始化表示插入元素的下一个元素和上一个元素的指针
def output():   # 定义一个函数用于输出链表
    next = head
    while next != -1:
        print(listvalue[next])
        next = listpoint[next]

    while listvalue[next] <= num and next != -1:    # 找到合适的位置插入元素

        last = next
        next = listpoint[next]


listvalue.append(num) # 向数组末尾加入新的元素的值
listpoint.append(listpoint[last])  # 加上新元素指针指向的位置
listpoint[last] = len(listvalue) - 1    # 上一个元素的位置指向新的元素
output()

# 删除列表
ListValue = [1, 5, 6, 2, 7, 3]  #建立单链表
ListRight = [3, 2, 4, 5, -1, 1]
head = 0    # 确定头指针
prepos = 5# 确定要删除的元素的前一个数的位置
ListRight[prepos] = ListRight[ListRight[prepos]] #删除元素




