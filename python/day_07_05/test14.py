# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
print(type(x))
print(type(y))
ax1.plot(x, y, 'r')


# 设置x轴y轴描述信息
plt.xlabel("x")
plt.ylabel("y")
plt.title("big figure")


# 绘制图中图，小图1
# 设置图像对应的位置，这里使用的是百分比
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(y, x, "b")
ax2.set_title("small figure1")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")


# 小图2
left, bottom, width, height = 0.6, 0.2, 0.25, 0.25
plt.axes([left, bottom, width, height])
plt.plot( x, y[::-1], "g")
plt.title("small figure2")
plt.ylabel("Y")
plt.xlabel("X")

plt.show()