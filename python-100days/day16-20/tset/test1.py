import itertools

# 产生ABCD的全排列
print(list(itertools.permutations('ABCD')))
print(list(itertools.combinations('ABCD', 2)))
print(list(itertools.product('ABDC', '123', 'YDU')))