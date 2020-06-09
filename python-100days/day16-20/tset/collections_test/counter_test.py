from collections import Counter

str="abcbcaccbbad"
li=[2,3,43,3,45,54,33,33,1]
d={'d':3,'f':4,'g':3,'h':5}

a = Counter(str)
b = Counter(li)
print(a.most_common(3))
print(sorted(b, reverse=True))
print(' '.join(sorted(a.elements())))
print(sum(a.values()))
del a['a']
print(a)