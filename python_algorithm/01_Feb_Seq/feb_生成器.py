"""
生成器法：
1、带有yield关键字的函数对象 他是返回一个列表list，list中的每个元素 都是 yield返回的每一个值 （每次执行yield输出值构成的列表）

2、带有yield的函数都被看成生成器，生成器是可迭代对象，且具备__iter__ 和 __next__方法， 可以遍历获取元素
python要求迭代器本身也是可迭代的，所以我们还要为迭代器实现__iter__方法，而__iter__方法要返回一个迭代器，迭代器自身正是一个迭代器，所以迭代器的__iter__方法返回自身即可
————————————————
版权声明：本文为CSDN博主「lamusique」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lamusique/article/details/89161831
"""
def feb(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

if __name__ == '__main__':
    for i in feb(20):
        print(i, end=' ')