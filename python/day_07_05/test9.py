# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
    等高线的绘制
"""

# 计算高度的函数
def f(x,y):
    return (1- x/2 + x**5 + y**3) * np.exp(-x**2-y**2)


n = 256
# 生成范围为-3~3，生成点的个数为256,间隔均匀
x = np.linspace(-3, 3, n)
# 生成范围为-3~3，生成点的个数为256,间隔均匀
y = np.linspace(-3, 3, n)
# print(x)
# print(y)
# 生成网格点坐标矩阵，通俗的讲就是，将x坐标一个一个对应上y坐标，相当于形成了网格坐标！！！
X, Y = np.meshgrid(x, y)
# print(X)
# print(Y)
# 参数8表示将颜色等级分为10部分。因为为0时，将颜色等级分为了两部分！！！
# cmap表示热力图的形式,
plt.contourf(X, Y, f(X,Y), 8, alpha=0.75, cmap=plt.cm.hot)


# 画等高线的线
C = plt.contour(X,Y, f(X,Y), 8, colors="black", linewidth=.5)

# 给等高线加上数值, inline为True表示数值显示在线里面！！！
plt.clabel(C, inline=True, fontsize=10)
# 去掉x坐标轴
plt.xticks(())
# 去掉y坐标轴
plt.yticks(())
# 展示
plt.show()