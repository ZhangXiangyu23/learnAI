# coding:utf-8
import numpy as np
"""
    分割矩阵
"""

# 生成一个三行四列的矩阵
A = np.arange(12).reshape((3, 4))
print(A)

# 对矩阵进行分割
# 参数1代表被分割的矩阵，参数2代表分割的块数，参数3代表分割的方向
# 0代表横向分割，1代表纵向分割
print(np.split(A, 2, axis=1))

# 横向分割成三块
print(np.split(A, 3, axis=0))

# split只能分割成相等的，不能不等分

# 使用array_split进行不等分割
print(np.array_split(A, 3, axis=1))


# 横向纵向指的是最后如何排列的
# 或者这样理解，垂直切是在垂直方向上切的；水平切是在水平方向上切的
# 直接使用函数进行纵向分割
print("纵向分割---------------------------")
print(np.vsplit(A, 3))
# 直接使用函数进行横向分割
print("横向分割---------------------------")
print(np.hsplit(A, 2))
