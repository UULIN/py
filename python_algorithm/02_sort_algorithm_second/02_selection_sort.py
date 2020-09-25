# 选择排序

def selection_sort(list):
    len_list = len(list)
    for i in range(len_list):
        # 设置为第一个元素
        min_num = i
        for j in range(i+1,len_list):
            if list[j] < list[min_num]:
                min_num = j
                list[min_num], list[i] = list[i], list[min_num]

    return list


if __name__ == '__main__':
    list = [22,21,6,225,61]
    print(selection_sort(list))
