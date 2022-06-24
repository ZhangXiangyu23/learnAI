# coding:utf-8
import numpy as np

"""
    numpy矩阵中的深拷贝和浅拷贝
"""

# 赋值，其实就还是公用一片内存
A = np.arange(5)
print("A矩阵", A)
B = A
C = A
print("B矩阵", B)
print("C矩阵", C)

# 赋值是浅拷贝，地址其实一致
print(id(A))
print(id(B))
print(id(C))

# 深度拷贝是，地址不一致， 新开辟了空间
D = A.copy()
print("A的地址是", id(A))
print("D的地址是", id(D))

