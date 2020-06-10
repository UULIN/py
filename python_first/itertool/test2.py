from itertools import accumulate
test_list = [x for x in range(1, 10)]
print(test_list)
for i in accumulate(test_list):
    print(i,end=' ')
    print()
for i in accumulate(test_list, lambda x,y : x * y):
    print(i, end=',')