# coding:utf-8
import random

import numpy as np
"""
    numpy的基础运算
"""

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print("a矩阵", a)
print("b矩阵", b)
# 矩阵减法
c = a - b
print("c矩阵", c)
# 矩阵加法
d = a + b
print("d矩阵", d)

# 进行平方
e = b**2
print("e矩阵", e)

# 调用numpy中的三角函数, sin ,cos ,tan
f = np.sin(a)
print(f)

# 判断矩阵中哪些值是小于3的
print(b)
print(b<3)

"""
    相乘
"""
g = np.array([[1, 1],
              [0, 1]])
h = np.arange(4).reshape((2,2))

print(g)
print(h)

# 每个元素挨个相乘
i = g * h
print(i)
# 矩阵相乘
j = np.dot(g, h)
print(j)

# 矩阵相乘的另一种形式
k = g.dot(h)
print(k)

# 生成随机数组
l = np.random.random((2,4))
print(l)

# 对矩阵中的数值进行求和、求最大值、求最小值
print(np.sum(l))
print(np.max(l))
print(np.min(l))

# 对指定行和列进行求和、求最大值、求最小值
# 其中axis参数值为0时，代表列；参数值为1时，代表行
print(np.sum(l, axis=1))
print(np.max(l, axis=0))
print(np.min(l, axis=1))