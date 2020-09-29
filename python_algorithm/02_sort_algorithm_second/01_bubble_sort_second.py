# 冒泡排序 时间复杂度O(n2)，稳定的算法

def bubble_sort(list):
    length = len(list)
    for i in range(length):
        flag = True
        for j in range(1, length - i):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1 ]
                flag = False
    if flag:
        return list

#    return list

if __name__ == '__main__':
    list = [9,10,2,3,4,1,56]
    print(bubble_sort(list))