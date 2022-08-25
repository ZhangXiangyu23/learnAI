# coding:utf-8
import numpy as np
"""
    numpy中的合并
"""

# 竖直方向上的合并
A = np.array([1, 2, 3])
B = np.array([1, 1, 1])
# print(np.vstack((A, B)))
# # 输出矩阵形状
# print(np.vstack((A, B)).shape)



# # 水平方向上的合并
# print(np.hstack((A, B)))
# print(np.hstack((A, B)).shape) # (6,)表示一行六列的矩阵
#
# print("原来的A矩阵", A)
# # 输出矩阵A的形状
# print(A.shape)  # (3,)表示一行三列的矩阵
# print("原来的矩阵", A)
# # 给列加上维度
# print(A[:, np.newaxis])
# # 给行加上维度
# print(A[np.newaxis, :])

# # 当矩阵为1行是就默认为列表形式了，转置之后也是列表形式
# # 比如说一行三列，转置之后仍然是一行三列
# # 要想将一行三列变成三行一列，应该使用：加维度
# print(A)
# print(A.T)
# A = np.array([1, 2, 3])[:, np.newaxis]
#
# print(A)
# print(type(A))
# print(A.shape)
# B = np.array([1, 1, 1])[:, np.newaxis]
#
# C = np.hstack((A, B))
# print("水平合并之后")
# print(C)
# D = np.vstack((A, B))
# print("竖直合并之后")
# print(D)


# 多个矩阵进行合并,竖直方向合并, 0代表竖直方向， 1代表水平方向
A = np.array([1, 2, 3])[:, np.newaxis]
B = np.array([1, 1, 1])[:, np.newaxis]
E = np.concatenate((A, B, A, A), axis=0)
F = np.concatenate((A, B, A, B), axis=1)
print("-" * 20)
print(E)
print("&" * 20)
print(F)