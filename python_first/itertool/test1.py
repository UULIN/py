from itertools import cycle
a = cycle('abcd')
print(next(a))
b = next(a)
for _ in range(0,10):
    b = next(a)
    print(b, end=',')