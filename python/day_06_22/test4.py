# coding:utf-8
import numpy as np
"""
    numpy中的运算
"""

# 生成顺序数值，并设定为三行四列
A = np.arange(2, 14).reshape(3, 4)
print(A)
# 输出矩阵中数值最小的那个值所在的索引
print(np.argmin(A))
# 最大值对应的索引
print(np.argmax(A))


# 输出矩阵中的平均数
print(np.mean(A))
# 输出矩阵中的中位数
print(np.median(A))


# 矩阵中前几项的累计
print(np.cumsum(A))

# 矩阵数值之间，每两个数值之间的差值
print(np.diff(A))

# 以行数组和列数组，输出矩阵中非0数值
print(np.nonzero(A))

B = np.array([[5, 9, 2],
              [1, 0, 7]])
print(B)
# 使用sort对矩阵数值进行 逐行排序
print(np.sort(B))

# 对矩阵进行转置
print(np.transpose(A))
# print(A.T)


# 矩阵中小于5的值全部变成5；大于9的值全部变成9，位于5到9之间的数值，保持不变
print(np.clip(A, 5, 9))

# 对行算平均值，对列算平均值
# 参数为0是对行算平均值，参数为1是对列算平均值
print(np.mean(A, axis=0)) # 对列
print(np.mean(A, axis=1)) # 对行