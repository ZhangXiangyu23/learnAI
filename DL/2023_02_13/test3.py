# coding:utf-8

import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
from random import random

"""
    用pytorch框架手写神经网络，解决回归问题，进行拟合
"""

# 造数据
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = pow(x, 2) + 0.2 * torch.rand(x.size())
# plt.scatter(x.numpy(), y.numpy())
# plt.show()

# 搭建神经网络
class Net(torch.nn.Module):
    # 神经网络相关层的数据
    def __init__(self, n_features, n_hidden, n_output):
        super(Net, self).__init__()
        # 隐藏层
        self.hidden = torch.nn.Linear(in_features=n_features, out_features=n_hidden)
        # 输出层
        self.output = torch.nn.Linear(in_features=n_hidden, out_features=n_output)

    # 进行前向传播
    def forward(self, x):
        # 输入数据x先经过隐藏层，然后对隐藏层输出数据使用激活函数
        x = torch.relu(self.hidden(x))
        # 将经过隐藏层的数据，经过输出层
        x = self.output(x)

        return x


# 使用神经网络类
n = Net(1, 10, 1)
# 输出神经网络的结构
print(n)

# 打开matplotlib的交互模式
plt.ion()


# 优化神经网络的参数
optimizer = torch.optim.SGD(n.parameters(), lr=0.2)
loss_fuc = torch.nn.MSELoss()


# 进行训练
for t in range(100):
    # 使用搭建好的神经网络进行预测
    prediction = n.forward(x)
    # 计算均方误差
    loss = loss_fuc(prediction, y)
    # 梯度清零
    optimizer.zero_grad()
    # 误差反向传播
    loss.backward()
    # 逐步优化
    optimizer.step()

    # 每5步展示一下
    if t % 5 == 0:
        # 清楚当前的Axes对象
        plt.cla()
        # 展示散点
        plt.scatter(x, y)
        # 展示拟合曲线
        plt.plot(x, prediction.detach().numpy(), "r-", lw=5)
        plt.text(0.5, 0, "loss = %.4f" % loss.data.numpy(), fontdict={"color": "red", "size": 20})
        # 暂停0.2秒
        plt.pause(0.2)


# 关闭交互模式
plt.ioff()
# 进行展示
plt.show()







