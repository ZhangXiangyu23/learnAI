import torch
from torch.autograd import Variable

tensor_data = torch.FloatTensor([[1, 2], [3, 4]])
# 将tensor数据转化为variable数据
variable = Variable(tensor_data, requires_grad=True)

print("tensor_data为\n", tensor_data)
print("variable为\n", variable)

print("-----------" * 5)
print("tensor相乘之后的结果")
t_out = torch.mean(tensor_data * tensor_data)
print(t_out)
print("variable相乘之后的结果")
v_out = torch.mean(variable * variable)
print(v_out)

# 对v_out进行反向传播
v_out.backward()
print('v_out进行反向传播之后，variable的梯度')
# 因为v_out由variable而来的，所以v_out反向传播之后，variable也会受影响
print(variable.grad)

print("-----------------" * 5)
# variable和tensor类型一样
print("variable的类型为", type(variable))
print(type(variable.data))
# 直接将variable使用numpy()转化为numpy类型，会报错
# variable和tensor还是有一点区别的！
# 修改这里
print(variable.data.numpy())
