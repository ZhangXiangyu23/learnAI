import torch
import numpy as np

numpy_data = np.arange(6).reshape(2, 3)
print("numpy_data为:\n", numpy_data)
print("numpy_data的数据类型为", type(numpy_data))

# 将numpy的数据转化成torch的形式, 从ndarray到Tensor
torch_data = torch.from_numpy(numpy_data)
print("torch_data为:\n", torch_data)
print("torch_data的数据类型为:", type(torch_data))

# 将torch的数据转化成numpy到达形式，从Tensor到ndarray
numpy_data_2 = torch_data.numpy()
print("numpy_data_2为:\n", numpy_data_2)
print("numpy_data_2的数据类型为:", type(numpy_data_2))

print("-------------------" * 5)
data = [-1, 2, -3, 5]
# 1.先将list形式转化为ndarray形式
# 2.再讲ndarray形式转化为tensor的形式
data_tensor = torch.from_numpy(np.array(data))

# abs运算
print("numpy求绝对值", np.abs(data))
print("pytorch求绝对值", torch.abs(data_tensor))
# 矩阵相乘
numpy_data = np.arange(4).reshape(2, 2)
torch_data = torch.from_numpy(numpy_data)
print("numpy中的矩阵相乘结果为\n", np.matmul(numpy_data, numpy_data))
print("torch中的矩阵相乘结果为\n", torch.mm(torch_data, torch_data))