# 冒泡排序
def bubble_sort(list):
    len_list = len(list)

    for i in range(len_list - 1):
        flag = True
        for j in range(len_list - i - 1):
            if list[j + 1] < list[j]:
                flag = False
                list[j + 1], list[j] = list[j], list[j + 1]
        if flag:
            return list


if __name__ == "__main__":
    list = [22,21,6,225,61,124,98,987,76,2]
    print(bubble_sort(list))