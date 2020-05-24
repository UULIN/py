import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

plt.show()