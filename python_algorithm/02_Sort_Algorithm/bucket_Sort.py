"""
桶排序，有两种实现：固定元素范围版，非固定元素范围版
"""

# 固定元素范围版
countn = [0] * 51

arr, result = [1, 1, 3, 19, 35, 49, 50, 5, 10, 16], []
for i in arr:
    countn[i] += 1
print(countn)
for i in range(len(countn)):
    if countn[i]:
        result += [i] * countn[i]
print(result)

# 非固定元素范围版

arr, result = [19, 35, 49, 49, 50, 5, 10, 16], []
max1 = max(arr)
min1 = min(arr)
countn1 = [0] * (max1 - min1 + 1)
for i in arr:
    countn1[i - min1] += 1
for i in range(len(countn1)):
    if countn1[i]:
        result += countn1[i] * [i + min1]
print(result)

