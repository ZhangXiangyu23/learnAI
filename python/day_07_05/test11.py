# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
"""
    3D图像
"""

fig = plt.figure()
# 添加3D坐标轴
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2, Y**2)

Z = np.sin(R)

plt.show()




# 展示
plt.show()
