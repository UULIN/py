"""
针对本题的题目设定，我们只能向上下左右移动一个单位。为了简便书写，我们不会使用四个判断语句来完成四个方向的移动，而是定义两个列表，分别存储 x 方向和
 y 方向的移动。例如，x 方向的列表为 [0,1,0,-1]，y 方向的列表为 [1,0,-1,0]，如此只需要一个 for 循环，其中 x[i],y[i] 分别代表不同方向的移
 动情况，就能完成上下左右四个方向的遍历（x=0,y=1 为向上，x=1,y=0 为向右，x=0, y=-1 为向下，x=-1,y=0 为向左）。
"""
from queue import Queue

Q = Queue   # 建立队列


class grid:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def bfs(self, val, startrow, startcol):
        row = len(val)  # val是存储地图的二维列表，row存储其行数，也就是y轴的值
        col = len(val[0])   # col存储其列数
        arrived = [[False for i in range(int(col))]for j in range(int(row))]
        # arrived存储二维列表每个方格是否已经到达过，或是否已经进入队列
        moverow = [0, 1, 0, -1]
        # moverow存储向相邻方格移动时行的变化情况，分别是1右移，0不动，-1左移
        movecol = [1, 0, -1, 0]
        # movecol存储向相邻方格移动时行的变化情况，分别是1右移，0不动，-1左移
        ans = 1
        Q.put(grid(int(startrow), int(startcol)))   # 将起点加入队列
        arrived[int(startrow) - 1][int(startcol) - 1] = True    # 设定起点已经到达过
        while not Q.empty():    # 进行队列判断，判断队列是否为空
            cur = Q.get()   # 取出队列首位的元素
            for i in range(4):
                # 遍历moverow和movecol，其实就是向现所位于的方格的四个方向移动
                newrow = cur.row + moverow[i]

                newcol = cur.row + movecol[i]
                if newrow > row or newrow <=0 or newcol > col and newcol <= 0:
                    # 判断移动后是否超界
                    continue
                if not arrived[newrow - 1][newcol - 1] and val[newrow - 1][newcol - 1] != val[cur.row -1][cur.col - 1]:
                    # 判断是否已经到达过时，是否与起始点数值不同
                    Q.put(grid(newrow, newcol)) # 将发现可以到达的新节点放入队列中
                    arrived[newrow - 1][newcol - 1] = True  # 将可到达的新方格设置为已到达过
                    ans += 1    # 求得答案
        return ans
