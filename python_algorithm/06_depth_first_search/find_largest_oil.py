"""
寻找最大油田
政府现勘探到一片油田，在这一片油田中有很多散落的石油资源。因为经费原因，政府只能开采一处油田，所以需找到最大的油田进行施工。油田的地理情况被简化成了一个矩阵，其中每一个方格代表一块土地，0 代表陆地，1 代表石油资源。如果一处石油资源和另一
处石油相连接，则其算一块油田。现要找到最大的相互连接的石油资源，并输出它的面积。
"""


def max_area_of_island(grid):
    row = len(grid) # 数组的行数，也就是y轴的长度
    col = len(grid[0])  # 数组的列数，也就是x轴的长度
    # 定义油田是否被访问过
    arrived = [[False for i in range(row)] for j in range(col)]

    # 记录油田的最大面积
    ans = 0

    # 写一个深度优先遍历方法去遍历油田
    def DFS(x, y):
        # 判断现在搜索的土地是否出界，是否已经访问过，是否存在油田
        if 0 <= x < col and 0 <= y < row and not arrived[x][y] and grid[x][y] == 1:
            arrived[x][y] = True # 标记该土地已经被搜索过
            # 搜索相邻的土地并将答案加1
            return 1 + DFS(x - 1, y) + DFS(x + 1, y) + DFS(x, y - 1) + DFS(x, y + 1)

        else:
            return 0
# 调用深度遍历函数
    for i in range(row):
        for j in range(col):
            area = DFS(i, j)
            if area > ans:
                ans = area
    return ans

if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1]]
    print(max_area_of_island(grid))