# coding:utf-8

import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F


# 造数据
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = pow(x, 2) + 0.2 * torch.rand(x.size())

# 画个散点图来展示数据点
# plt.scatter(x.numpy(), y.numpy())
# plt.show()

# 搭建神经网络类
class Net(torch.nn.Module):
    # 神经网络中，层的相关信息
    # 形参分别代表：输入特征数、隐藏层神经元个数、输出值个数
    def __init__(self, n_features, n_hidden, n_output):
        # 继承自Net
        super(Net, self).__init__()
        # 隐藏层
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        # 输出层
        self.predict = torch.nn.Linear(n_hidden, n_output)

    # 神经网络进行前向传播
    # x是输入信息
    def forward(self, x):
        # 用激励函数进行激活x
        x = torch.relu(self.hidden(x))
        # 其他激活函数的测试
        # x = F.softplus(self.hidden(x))
        # x = torch.sigmoid(self.hidden(x))
        # x = torch.tanh(self.hidden(x))
        # 将经过隐藏层的数据输入到predict层
        x = self.predict(x)
        return x


# 使用搭建好的神经网络
net = Net(1, 10, 1)
# 输出神经网络的层结构
print(net)

# 将matplotlib设定为实时打印
plt.ion()
plt.show()


# 优化神经网络参数
optimizer = torch.optim.SGD(net.parameters(), lr=0.5)
# 损失函数
loss_func = torch.nn.MSELoss()



# 开始训练,训练100步
for t in range(100):
    # 用搭建好的神经网络进行预测
    prediction = net(x)
    # 计算误差
    loss = loss_func(prediction, y)
    # 计算完之后，将梯度清为0
    optimizer.zero_grad()
    # 进行误差的反向传播
    loss.backward()
    # 然后逐步优化
    optimizer.step()

    # 进行可视化
    # 每五步进行打印一次
    if t % 5 == 0:
        plt.cla()
        plt.scatter(x, y)
        # 进行绘制线条
        plt.plot(x.numpy(), prediction.detach().numpy(), "r-", lw=5)
        plt.text(0.5, 0, "Loss=%.4f" % loss.data.numpy(), fontdict={"size": 20, "color": "red"})
        plt.pause(0.2)

print(f"最终的loss为{loss.data.numpy()}")
plt.ioff()
plt.show()





