# 选择排序 时间复杂度O(n2) 不稳定

def selection_sort(list):
    length = len(list)
    for i in range(length):
        min_num = i
        for j in range(i + 1, length):
            if list[j] < list[min_num]:
                min_num = j
        list[i], list[min_num] = list[min_num], list[i]
    return list

if __name__ == '__main__':
    list = [1,3,2,65,23,55]
    print(selection_sort(list))
