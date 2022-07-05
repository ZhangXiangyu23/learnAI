# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    对坐标轴进行设置2
"""

# 造数据
x = np.linspace(-1, 1, 50)
y = x + 1
plt.plot(x, y, color="red", linewidth=2.0, linestyle="--")
# 设置X轴范围
plt.xlim(-2, 2)
# 设置Y轴范围
plt.ylim(-2, 2)
# 设置x轴描述
plt.xlabel("I AM X")
plt.ylabel("I AM Y")

# 重新设置刻度
plt.yticks([-2, -1, 0, 1, 2],
         [r"$really\ bad$", r"$bad$", r"$normal$", r"$good$", r"$really\ \alpha good$"])

# 获取到图像的四个边框
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# 将边框设置为x轴和y轴
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
# 将下边框移动到数值为0的位置
ax.spines["bottom"].set_position(('data', 0))
# 将左边框移动到数值为0的位置
ax.spines["left"].set_position(("data", 0))

plt.show()

