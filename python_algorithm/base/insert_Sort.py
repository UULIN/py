"""
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""
sort_list = [30, 44, 23, 656, 23, 78, 96, 212, 777]
for i in range(1, len(sort_list)):
    j = i - 1
    temp = sort_list[i]

    while j >= 0 and sort_list[j] > temp:
        sort_list[j + 1] = sort_list[j]
        j -= 1
    sort_list[j + 1] = temp
print(sort_list)

