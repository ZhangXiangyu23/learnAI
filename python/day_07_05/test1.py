# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
    绘制一条直线
"""

# 通过numpy创造50个数据，范围为从-1到1
x = np.linspace(-1, 1, 50)
# y值
y = x - 1
# 通过自变量和因变量进行绘制
plt.plot(x, y)
# 进行展示
plt.show()