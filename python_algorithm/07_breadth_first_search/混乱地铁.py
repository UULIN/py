"""
在某一个城市中地铁网极度混乱。一条地铁线路上有 n 个地铁站，分别编号为 1 到 n。地铁线路上的每一个站都会停靠地铁，每一个地铁站上都有一个数字 m，代表从此站出发乘客必须乘坐的站数。

每个地铁站都有通往两个方向的地铁。因此既可以向编号大的方向前进 m 站，也可以向编号小的方向前进 m 站。但如果前进后超出了地铁站的范围，则该地铁不可被乘坐。例如编号为 1 的地铁上的数字为 3，那么在该地铁站上车，可以向正方向坐车到
4 号地铁站。但不能反方向坐车到 -2 号地铁站，因为 -2 号地铁站不存在。现在乘客从 A 号地铁站出发，想要到达 B 号地铁站，求他能否到达，最少要搭乘多少次地铁？
"""
from queue import Queue
move = []   # 列表里存储每一个地铁站的数字
Q = Queue() # 建立队列
start, end, num = input().split()   # 读入出发点，目的地，总共的地铁站数量
move = input().split()  # 读入每个地铁站的数字
station = [-1 for i in range(0, int(num) + 1)]  # station 列表存储出发点到对应地铁站需要乘坐地铁的趟数，-1代表无法到达
Q.put(int(start))   # 将出发点放入队列中
station[int(start)] = 0 # 出发点到自身地铁站时不用乘坐任何地铁，赋值为0
while not Q.empty():    # 广度优先搜索循环
    cur = Q.get() # 取出队列第一项，并将其移除队列
    left = cur - int(move[cur - 1])    # 计算出反方向乘坐会到达哪个地铁站
    right = cur + int(move[cur - 1])    # 计算出正方向乘坐会到达哪个地铁站
    if left >= 1 and station[left] == -1:
        # 如果反方向乘坐没有出界且没有到过，则将新到达的地铁站加入队列
        Q.put(left)
        station[left] = station[cur] + 1
        # 更新到达对应地铁站需乘坐的趟数
    if right <= int(num) and station[right] == -1:
        Q.put(right)
        station[right] = station[cur] + 1
print(station[int(end)])    # 输出答案
