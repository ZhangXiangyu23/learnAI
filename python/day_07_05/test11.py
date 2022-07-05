# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
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
R = np.sqrt(X**2+Y**2)

Z = np.sin(R)

# 参数rstride表示行跨，cstride表示列跨
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))

# zdir参数表示将压到哪个轴    offset参数表示等高线图的平面将压到哪个位置
ax.contourf(X, Y, Z, zdir='z', offset=-1.5, cmap='rainbow')
ax.set_zlim(-2, 2)
plt.show()




# 展示
plt.show()
