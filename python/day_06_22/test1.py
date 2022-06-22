# coding:utf-8
import numpy as np
"""
    numpy的属性
"""

# 将列表转化成一个numpy的矩阵
array = np.array([[1, 2, 3], [4, 5, 6]])
# 输出矩阵
print(array)
# 输出矩阵的维数
print("dim", array.ndim)
# 输出矩阵形状
print("shape", array.shape)
# 输出矩阵尺寸
print("size", array.size)