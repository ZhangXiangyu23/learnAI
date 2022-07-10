# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    在一张图中放置几张子图
"""

plt.figure()

# 2表示总共两行,1表示当前行只有一列,最后一个类表示图形的计数
plt.subplot(2, 1, 1)
# 第一个列表表示x轴数据,第二个列表表示y轴数据,
plt.plot([0, 1], [0, 1])

# 第一行本该放三个,结果一个图把一行都占了,仍然计数,所以第二行第一列为第四个
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 1])


plt.show()