"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
"""
arry_list = [55, 30, 60, 20, 1, 50, 51]
# 第一层for表示循环选择的遍数
for i in range(len(arry_list)-1):
    # 将起始元素设为最小元素
    min_index = i
    # 第二层for表示最小元素和后面的元素逐个比较
    for j in range(i+1, len(arry_list)):
        if arry_list[min_index] > arry_list[j]:
            # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
            min_index = j
    # 查找一遍后将最小元素与起始元素互换
    arry_list[i], arry_list[min_index] = arry_list[min_index], arry_list[i]

print(arry_list)