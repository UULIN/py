# https://pinyin.sogou.com/skins/detail/view/info/526286
def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break
