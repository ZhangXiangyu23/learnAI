# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    绘制散点图
"""

n = 1024
# 按照正态分布(也叫做高斯分布)生成n个均值为0，标准差为1的随机数
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# 为了生成颜色
T = np.arctan2(X, Y)

# alpha代表透明度
plt.scatter(X, Y, s=75, c=T, alpha=0.7)
# 设定x轴范围
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))

# 将x轴y轴的数值进行隐藏
plt.xticks(())
plt.yticks(())
# 进行展示
plt.show()