# coding:utf-8
import numpy as np

"""
    输出矩阵的各种形式！！！！
"""

#   矩阵输出出来，中间没有逗号；
#     而列表打印出来会有逗号
# a_list = [1, 2, 3]
# print(a_list)
# a_np_array = np.array([1, 2, 3])
# print(a_np_array)
# dtype是用来设定矩阵中数值的数据类型
# a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
# print(a.dtype)
# print(a)

# 生成3行4列的零矩阵
# b = np.zeros((3, 4))
# print(b)

# 生成数值全部是1的矩阵
# c = np.ones((2,4), dtype=np.int32)
# print(c)

# # 输出empty的矩阵
# d = np.empty((3,4))
# print(d)

# 输出顺序的矩阵,生成数据类比range; 从10到20，左闭右开，步长为2
# e = np.arange(10, 20, 2)
# print(e)

# 输出顺序的矩阵,按顺序以三行四列的格式进行输出
# f = np.arange(12).reshape(3, 4)
# print(f)

# 输出线段,1是起始值，10是终止值，6是生成数值个数，从1到10生成6个数，并且他们之间是等距的
# 自动匹配步长
g = np.linspace(1, 10, 6).reshape(2, 3)
print(g)