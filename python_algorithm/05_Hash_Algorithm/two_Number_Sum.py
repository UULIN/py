"""
在给定的一些数字中找出两个数，使得它们的和为 N，前提是这些数据中保证有答案，并且只有一个答案。
给定 5 个数字：3、4、5、7、10，从中选择两个数使它们的和为 11，可以选择 4 和 7，这个问题用哈希算法该如何解决呢？
"""
#两个数的和
#两个数的和
def twoSums(mynum, target):
    mydict = {}
    for i in range(len(mynum)):
        m= mynum[i] #定义m为当前待查询的数字
        if target-m in mydict: #判定target-m是否已经在字典中
            return mydict[target - m], i  #如果已经存在，则返回这两个数的下标
        else:
            mydict[m] = i
