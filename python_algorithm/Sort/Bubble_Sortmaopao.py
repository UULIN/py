"""
比较相邻的元素。如果第一个比第二个大，就交换他们两个。

对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

针对所有的元素重复以上的步骤，除了最后一个。

持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
arry_list = [55, 30, 60, 20, 1, 50, 51]

for i in range(len(arry_list) -1 ):
    for j in range(len(arry_list)-i-1):
        print(j)
        if arry_list[j + 1] > arry_list[j]:
            arry_list[j], arry_list[j + 1] = arry_list[j + 1], arry_list[j]

print(arry_list)
