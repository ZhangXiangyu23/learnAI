# coding:utf-8
import numpy as np
import torch

"""
    list和ndarray之间的相互转化
"""

# 生成数据
data_np = np.linspace(-10, 10, 20)
print("data_np的数据为\n", data_np)
print("数据格式为", type(data_np))
# 从nd.array转化成list
data_list = data_np.tolist()
print("data_list的数据为\n", data_list)
print("数据格式为", type(data_list))

print("-" * 100)
# 生成数据
a_list = [1, 2, 3, 4]
print("a_list", a_list)
print("数据格式为", type(a_list))
# list转nd.array
a_ndarray = np.array(a_list)
print("a_ndarray的数据是", a_ndarray)
print("数据格式为", type(a_ndarray))

print("#" * 100)

"""
    ndarray和tensor之间的转化
"""

a_ndarray = np.linspace(-5, 5, 10)
print("a_ndarray的数据为", a_ndarray)
print("数据类型为", type(a_ndarray))
# a_ndarray转tensor
a_tensor = torch.from_numpy(a_ndarray)
print("a_tensor的数据为", a_tensor)
print("数据类型为", type(a_tensor))
print("-" * 100)


# 从tensor转ndarray
b_data = a_tensor.numpy()
print("b_data的数据为", b_data)
print("数据类型为", type(b_data))

print("#" * 100)
"""
    list和tensor之间的转化
"""

zxy_tensor = torch.linspace(-5, 5, 10)
print("zxy_tensor的数据为", zxy_tensor)
print("数据类型为", type(zxy_tensor))
# tensor转list
zxy_list = zxy_tensor.tolist()
print("zxy_list的数据为", zxy_list)
print("数据类型为", type(zxy_list))
print("-" * 100)

# list转tensor
c_data = torch.Tensor(zxy_list)
print("c_data的数据为", c_data)
print("c_data的数据类型为", type(c_data))