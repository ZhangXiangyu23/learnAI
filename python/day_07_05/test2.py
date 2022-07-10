# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

"""
    figure的使用
"""

# 造数据, 在-1~1之间均匀生成50个数
x = np.linspace(-1, 1, 50)

# 编号为2的图像,通过figsize参数设置图像的大小
plt.figure(num=2, figsize=(8, 5))
y1 = x - 1
# 绘制编号为2的图像
plt.plot(x, y1)


# 编号为3的图像 ,figsize=(宽， 高)
plt.figure(num=3, figsize=(5, 8))
y2 = x**2
# 绘制编号为3的图像，  绘制的有两条
plt.plot(x, y2)
# color参数用来设置线条颜色,linewidth参数用来设定线条宽度,linestyle参数用来设定线条样式
plt.plot(x, y1, color="red", linewidth=10.0, linestyle="--")

# 进行展示
plt.show()