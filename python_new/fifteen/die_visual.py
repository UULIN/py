from python_new.fifteen import Die
import pygal
"""投骰子"""
# 创建2个骰子
die1 = Die()
die2 = Die()

# 投几次骰子，放入一个列表
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):

    frequency = results.count(value)
    frequencies.append(frequency)

# 进行结果可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = []

for label_num in range(2, 13):
    hist.x_labels.append(label_num)

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('./data/die_visual.svg')

