# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    给图片加上图例legend
"""

# 造数据
x = np.linspace(-1, 1 ,50)
y1 = x**2

# 设定x的范围
plt.xlim(-2, 2)
# 设定y的范围
plt.ylim(-2, 2)

# 设置x轴描述
plt.xlabel("I am x")
# 设置y轴描述
plt.ylabel("I am y")

# 设置每一格的宽度,参数2是起始，参数1是终止，参数5是刻度总数
new_ticks = np.linspace(-2, 1, 5)
# print(new_ticks)
# 设定新的横轴刻度
plt.xticks(new_ticks)

# 设定新的纵轴刻度
# 前后加上美元符号，使字体变的好看起来
# 如何打印出数学中的alpha，使用\进行转义
plt.yticks([-2, -1, 0, 1, 2],
           [r"$really\ bad$", r"$bad\ \alpha$", r"$normal$", r"$good$", r"$really\ good$"])

y2 = -x + 1
# plt.plot(x, y2, label="one")
# # 添加图例
# plt.legend()

l1, = plt.plot(x, y1, color="red", linewidth=2.0, linestyle="--", label="two")
l2, = plt.plot(x, y2, label="one")
plt.legend(handles=[l1, l2,], labels=["aaa", "bbb"], loc="best")
# 进行绘制
plt.show()