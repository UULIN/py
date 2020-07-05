"""
数组合并
"""
def compare(arr1, arr2):
    index1, index2 = 0, 0
    tmp =[]
    while index1 <= len(arr1) - 1 and index2 <=  len(arr2) - 1:
        if arr1[index1] >= arr2[index2]:
            tmp.append(arr2[index2])
            index2 += 1
        else:
            tmp.append(arr1[index1])
            index1 += 1
    if index1 == len(arr1):
        tmp += arr2[index2:]
    else:
        tmp += arr1[index1:]
    return  tmp


if __name__ == '__main__':
    arr1 = [3, 6, 9, 12, 15]  # 初始化两个数组
    arr2 = [2, 4, 7, 13, 14]
    print(compare(arr1, arr2))