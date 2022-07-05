# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
    figure的使用
"""

# 通过numpy造数据
x = np.linspace(-1, 1, 50)

# 编号为2的图像
plt.figure(num=2, figsize=(8, 5))
y1 = x - 1
# 绘制编号为2的图像
plt.plot(x, y1)


# 编号为3的图像 ,figsize=(宽， 高)
plt.figure(num=3, figsize=(5, 8))
y2 = x**2
# 绘制编号为3的图像，  绘制的有两条
plt.plot(x, y2)
plt.plot(x, y1, color="red", linewidth=10.0, linestyle="--")

# 进行展示
plt.show()