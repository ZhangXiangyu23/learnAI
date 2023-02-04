# coding:utf-8
import torch

x_one = [1, 2, 3, 4, 5]
print("x_one的数据为", x_one)
print("x_one的数据类型为", type(x_one))

# list转torch.Tensor
x_two = torch.Tensor(x_one)
print("x_two的数据为", x_two)
print("x_two的数据类型为", type(x_two))

# torch.Tensor转list
x_three = x_two.tolist()
print("x_three的数据为", x_three)
print("x_three的数据类型为", type(x_three))