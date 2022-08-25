# coding:utf-8
import numpy as np
"""
    numpy中的索引
"""
A = np.arange(3, 15).reshape((3, 4))
print(A)
# # 矩阵中，指定索引的值
# print(A[2])  # [11, 12, 13, 14]
#
# # 输出指定索引对应的数值
# print(A[1][1]) # 8
# # 也可以是这种形式进行具体索引的输出
# print(A[1, 1]) # 8

# # 打印第二行的所有数
# print(A[2, :])
# # 打印第一列的所有数
# print(A[:, 1])
#
# # 在python中满足左闭右开的原则
# print(A[1, 1:3])

# # 循环起来，打印行
# print("#" * 20)
# for row in A:
#     print(row)

# # 打印列
# for column in A.T:
#     print(column)


# 迭代矩阵的项,这样输出的是矩阵的每一行
for item in A:
    print(item)

print("%" * 50)
print(type(A))
# # 将矩阵拉直为一维矩阵
# print(A.flatten())
# # 矩阵
# print(type(A.flatten()))
# # 想要迭代每一个元素，需要这样
# print("迭代每一个数值")
# for item in A.flat:
#     print(item)