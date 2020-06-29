"""
斐波那契数列-递归方法
1、1、2、3、5、8、13、21、34、
"""
def feb(n):

    if n <= 1:
        return n
    else:
        return feb(n -1) + feb(n -2)

if __name__ == '__main__':
    for i in range(1, 20):
        print(feb(i))