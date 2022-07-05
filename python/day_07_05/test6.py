# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    绘制2*X+1的图像
"""

# 造数据
x = np.linspace(-5, 5, 20)
y = 2*x + 1
plt.plot(x, y)

# 设定x轴范围
plt.xlim(-4, 4, 9)
# 设定y轴范围
plt.ylim(-8, 8, 9)

# 设定x轴描述
plt.xlabel("I AM X")
# 设定y轴描述
plt.ylabel("I AM Y")

# 获取图像的边框
ax = plt.gca()
ax.spines["right"].set_color("None")
ax.spines["top"].set_color("None")

# 移动剩下的边框
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

# 展示一个点
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0)
plt.show()

