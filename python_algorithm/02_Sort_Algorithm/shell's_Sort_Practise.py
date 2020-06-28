"""
希尔排序，每次以一半步长进行，是插入排序的进阶版，插入排序以1为单位，希尔排序以指定步长为单位
"""
from math import floor
test_list = [12, 123, 43, 4554, 1, 432, 656, 65, 12312, 2]


def shell_sort(arr):
    step = floor(len(arr) / 2)
    while step > 0:
        for i in range(step, len(arr)):
            temp = arr[i]
            j = i - step
            while j >= 0 and arr[j] > temp:
                arr[j + step] = arr[j]
                j -= step
            arr[j + step] = temp
        step  = floor(step / 2)
    return arr


if __name__ == '__main__':
    print(shell_sort(test_list))