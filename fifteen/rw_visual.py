import matplotlib.pyplot as plt
from fifteen.random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步

# 创建一个random实例，并将其包含的点都绘制出来
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    point_number = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
