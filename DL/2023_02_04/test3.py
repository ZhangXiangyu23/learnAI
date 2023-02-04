# coding:utf-8

import torch
import numpy as np

# numpy.ndarray
# 造数据
data_one = np.arange(6).reshape(2, 3)
print("data_one的数据为\n", data_one)
print("data_one的数据类型为", type(data_one))

print("-" * 100)
# numpy.ndarray转化为tensor
data_two = torch.from_numpy(data_one)
print("data_two的数据为\n", data_two)
print("data_two的数据类型为", type(data_two))

print("#" * 100)
# tensor转化为numpy.ndarray
data_three = data_two.numpy()
print("data_three的数据为\n", data_three)
print("data_three的数据类型为", type(data_three))