list_sort1 = [11, 2321, 4656, 6743, 12, 54, 876, 232, 1]

# first insert_sort

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
