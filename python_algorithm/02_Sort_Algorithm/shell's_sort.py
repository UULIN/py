list_sort1 = [11, 2321, 4656, 6743, 12, 54, 876, 232, 1]

# first insert_sort
"""
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序
"""
gap = len(list_sort1)//2
while gap > 0:
    for i in range(gap, len(list_sort1)):
        temp = list_sort1[i]
        j = i - gap
        while j >= 0 and list_sort1[j] > temp:
            list_sort1[j + gap] = list_sort1[j]
            j -= gap
        list_sort1[j + gap] = temp
    gap = gap // 2
print(list_sort1)
