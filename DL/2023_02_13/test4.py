# coding:utf-8

import torch
import matplotlib.pyplot as plt

# 造数据
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x ** 2 + 0.2 * torch.rand(x.size())
# plt.scatter(x, y)
# plt.show()

# 构建神经网络
class Net(torch.nn.Module):
    def __init__(self, input_features, hidden_features, output_features):
        super(Net, self).__init__()
        # 隐藏层
        self.hidden = torch.nn.Linear(in_features=input_features, out_features=hidden_features)
        # 输出层
        self.output = torch.nn.Linear(in_features=hidden_features, out_features=output_features)

    def forward(self, x):
        x = torch.relu(self.hidden(x))
        x = self.output(x)
        return x



# 实例化神经网络
net = Net(1, 10, 1)
print(net)

# 开启交互模式
plt.ion()

# 优化器
optimizer = torch.optim.SGD(net.parameters(), lr=0.5)
loss_fuc = torch.nn.MSELoss()

# 训练
for t in range(100):
    net.forward(x)
    prediction = net.forward(x)
    loss = loss_fuc(prediction, y)
    # 梯度清0
    net.zero_grad()
    # 误差反向传播
    loss.backward()
    # 逐步优化
    optimizer.step()

    # 动态展示
    if t % 5 == 0:
        # 清空绘图区域
        plt.cla()
        # 先绘制原有数据
        plt.scatter(x, y)
        plt.plot(x, prediction.detach().numpy(), "r-", lw=5)
        plt.text(0.5, 0, "loss = %.4f" % loss.data.numpy(), fontdict={"color": "red", "size": 20})
        plt.pause(0.2)


plt.ioff()
plt.show()





