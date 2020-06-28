"""
顺序查找
是最基础的一种，按照查找表中原有的顺序对线性表进行遍历查找
由于需要遍历整个表，所以顺序查找的时间复杂度为O(n)

"""
"""
eg1
【例 1】在一个已知的列表 [1,3,5,4,2,4,6,5,1] 中查找给定的元素出现的第一个位置。
如果给定的元素存在于列表中，输出它的下标；如果不存在，输出 -1。输入的给定元素是 int 类型。
"""



def sequential_search1(arr, value):
    for i in range(len(arr)):
        if int(value) == test_list[i]:
            return i
    return -1


"""
eg2
在一个已知的列表 [1,3,5,4,2,4,6,5,1] 中查找给定的元素。输出给定元素出现的所有下标。
若给定元素不存在于数组中，不输出。输入的给定元素是 int 类型。
"""


def sequential_search2(arr, value):
    temp = []
    for i in range(len(arr)):
        if arr[i] == value:
            temp.append(i)
    return  temp





if __name__ == '__main__':
    test_list = [1, 3, 5, 4, 2, 4, 6, 5, 1]
    globle_value = int(input("please input your value: "))
    print(sequential_search2(test_list, globle_value))
