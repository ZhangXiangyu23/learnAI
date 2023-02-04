# coding:utf-8

import numpy as np
import torch

# list和numpy.ndarray之间的转化
x_one = [[1, 2, 3], [4, 5, 6]]
print("x_one的数据为\n", x_one)
print("x_one的数据类型为", type(x_one))

# 将list数据转化为numpy.ndarray形式
x_two = np.array(x_one)
print("x_two的数据为\n", x_two)
print("x_two的数据类型为", type(x_two))

# 将numpy.ndarray转化为lisy形式
x_three = x_two.tolist()
print("x_three的数据为\n", x_three)
print("x_three的数据类型为", type(x_three))

