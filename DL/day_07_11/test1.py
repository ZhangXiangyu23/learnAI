# coding:utf-8

import numpy as np
import torch

"""
    numpy和torch的对比
"""
# 生成[0, 6)的6个整数,然后转化成2行3列的矩阵
np_data = np.arange(6).reshape(2, 3)
# 将numpy类型的数据转化成torch类型
torch_data = torch.from_numpy(np_data)

print(np_data)
print(torch_data)

print(type(np_data))
# 将tensor类型的数据转化成numpy类型
# 使用.numpy()方法
tensor_to_numpy_data = torch_data.numpy()
print(tensor_to_numpy_data)

print("-" * 50)
# abs
data = [-1, -2, 1, 2]
# 将list类型转化成tensor类型
tensor = torch.FloatTensor(data)

print(data)
print(tensor)
print(np.abs(data))
print(torch.abs(tensor))

# 想要说明的一点是,torch和numpy很多函数功能是一致的,比如abs ,sin ,cos
# sin
print("#" * 50)
print(np.sin(data))
print(torch.sin(tensor))
# cos
print(np.cos(data))
print(torch.cos(tensor))

# mean求平均值
print(np.mean(data))
print(torch.mean(tensor))

# numpy和torch两种方式进行矩阵乘法
new_data = [[1, 2], [3, 4]]
print(type(new_data))
# 将list类型转化成tensor类型
tensor_data = torch.FloatTensor(new_data)

print(np.matmul(new_data, new_data))
print(torch.mm(tensor_data, tensor_data))

# .dot
numpy_data = np.array(new_data)
# 依然是矩阵乘法
print(numpy_data.dot(new_data))
# 而torch中的.dot则是将张量展开了,逐个对应相乘,现在版本会报错的
# print(tensor_data.dot(tensor_data))