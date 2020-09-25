# 插入排序
def insert_sort(list):
    length = len(list)
    for i in range(1, length):

        # 无序列表的第一个值
        temp = list[i]
        # j为已排序列表的最后一个值
        j = i - 1

        while j >= 0:
            # 如果有序列表的最后一个值大于无序列表的第一个值的话
            if list[j] > temp:
                list[j + 1] = list[j]
                list[j] = temp
                j -= 1
            else:
                break
    return list
def insert_sort2(list):
    length = len(list)
    for i in range(1, length):

        # 无序列表的第一个值
        temp = list[i]
        # j为已排序列表的最后一个值
        j = i - 1

        while j >= 0 and list[j] > temp:
            # 如果有序列表的最后一个值大于无序列表的第一个值的话
            list[j + 1] = list[j]
            list[j] = temp
            j -= 1
    return list


if __name__ == '__main__':
    list = [22,21,6,225,61]
    print(insert_sort2(list))



