# coding:utf-8
import numpy as np
import torch
from torch.autograd import Variable

"""
    变量variable
"""

tensor = torch.FloatTensor([[1, 2], [3, 4]])
variable = Variable(tensor, requires_grad=True)

print(tensor)
print(variable)
print(type(tensor))
print(type(variable))

# 两个tensor相乘之后进行求平均数
t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)
print(t_out)
print(v_out)

# v_out进行反向传播
v_out.backward()
# 输出variable的梯度

# 函数为v_out = 1/4 * (variable ^ 2)
# 函数值为v_out ,自变量为variable
# 求v_out关于variable的梯度(导数值)
# d(v_out)/d(variable) = 1/2 * variable
# 也就是v_out 关于 variable的梯度为原来variable的一半
print("原来值为")
print(variable)
print("梯度为")
print(variable.grad)

# variable里面除了grad属性,还有data属性
print(variable.data)
print(type(variable.data))
print(type(variable))
# 转成numpy的形式
print(variable.data.numpy())
