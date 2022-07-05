# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    绘制柱状图
"""

n = 12
X = np.arange(n)
# uniform表示均匀分布
Y1 = (1-X/float(n))*np.random.uniform(0.5, 1.0, n)
Y2 = (1-X/float(n))*np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    # ha:水平方向居中对齐 va:竖直方向向下对齐
    # x，y为文字放置的位置
    plt.text(x, y+0.05, '%.2f' % y, ha="center", va="bottom")

for x, y in zip(X, Y2):
    plt.text(x, -y-0.1, '-%.2f' % y, ha="center", va="bottom")

plt.xlim(-.5, n)
# 消除x轴的数值
# plt.xticks(())
plt.ylim(-1.25, 1.25)
# 消除y轴数值
# plt.yticks(())

plt.show()
