# 直接插入排序 时间复杂度是O(n2)，稳定性，稳定
def insert_sort(list):
    length = len(list)
    for i in range(1,length):
        # 设置为无序列表的第一个值
        temp = list[i]
        # 设置为有序列表的最后一个值
        j = i - 1
        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            list[j] = temp
            j -= 1
    return list


if __name__ == '__main__':
    list = [22,41,6,123,5]
    print(insert_sort(list))