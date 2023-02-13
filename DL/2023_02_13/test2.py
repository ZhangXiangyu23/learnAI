# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import torch

"""
    ndarray和list之间相互转化
"""

# ndarray转list
x_ndarray = np.arange(12).reshape(3, 4)
print("x_ndarray的数据为\n", x_ndarray)
print("x_ndarray的数据类型为", type(x_ndarray))
x_list = x_ndarray.tolist()
print("x_list的数据为\n", x_list)
print("x_list的数据类型为", type(x_list))

# list转ndarray
y_ndarray = np.array(x_list)
print("y_ndarray的数据为\n", y_ndarray)
print("y_ndarray的数据类型为", type(y_ndarray))

print("-" * 100)

"""
    ndarray和tensor之间的转化 
"""

# tensor转ndarray
x_tensor = torch.FloatTensor(x_list)
print("x_tensor的数据为\n", x_tensor)
print("x_tensor的数据类型为", type(x_tensor))
u_ndarray = x_tensor.numpy()
print("u_ndarray的数据为\n", u_ndarray)
print("u_ndarray的数据类型为", type(u_ndarray))

# ndarray转tensor
y_tensor = torch.from_numpy(u_ndarray)
print("y_tensor的数据为\n", y_tensor)
print("y_tensor的数据类型为", type(y_tensor))

print("-" * 100)

"""
    list和tensor之间的转化
"""
# list转tensor
z_tensor = torch.Tensor(x_list)
print("z_tensor的数据为\n", z_tensor)
print("z_tensor的数据类型为", type(z_tensor))

# tensor转list
z_list = z_tensor.tolist()
print("z_list的数据为", z_list)
print("z_list的数据类型为", type(z_list))