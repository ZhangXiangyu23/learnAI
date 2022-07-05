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
# 标一个点
plt.scatter(x0, y0, color="b", s=100)
plt.plot([x0, x0], [y0, 0], "k--", lw=2.5)

# 进行注释,方式一
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords="data", xytext=(+30, -30),
             textcoords="offset points", fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))

plt.text(-4.7, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={"size":16, "color": 'r'})

plt.show()

