# coding:utf-8
import numpy as np
"""
    numpy中的合并
"""

# 竖直方向上的合并
A = np.array([1, 2, 3])
B = np.array([1, 1, 1])
print(np.vstack((A, B)))
# 输出矩阵形状
print(np.vstack((A, B)).shape)



# 水平方向上的合并
print(np.hstack((A, B)))
print(np.hstack((A, B)).shape)

print("原来的A矩阵", A)
# 输出矩阵A的形状
print(A.shape)
# 给列加上维度
print(A[:, np.newaxis])
# 给行加上维度
print(A[np.newaxis, :])


A = np.array([1, 2, 3])[:, np.newaxis]
B = np.array([1, 1, 1])[:, np.newaxis]
C = np.hstack((A, B))
print("水平合并之后")
print(C)
D = np.vstack((A, B))
print("竖直合并之后")
print(D)


# 多个矩阵进行合并,竖直方向合并, 0代表竖直方向， 1代表水平方向
E = np.concatenate((A, B, A, A), axis=0)
F = np.concatenate((A, B, A, B), axis=1)
print("-" * 20)
print(E)
print("&" * 20)
print(F)