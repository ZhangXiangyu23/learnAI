# coding:utf-8

import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

n_data = torch.ones(100, 2)
# 被打上0类标签的数据
x0 = torch.normal(2*n_data, 1)
y0 = torch.zeros(100)
# 被打上1类标签的数据
x1 = torch.normal(-2*n_data, 1)
y1 = torch.ones(100)
# 将两类数据进行拼接
x = torch.cat((x0, x1), 0).type(torch.FloatTensor)
y = torch.cat((y0, y1), ).type(torch.LongTensor)

# 可视化当前数据
# plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=y.data.numpy(), s=100, lw=0, cmap='RdYlGn')
# plt.show()


# 搭建神经网络
class Net(torch.nn.Module):
    # 神经网络各层的相关信息
    def __init__(self, n_features, hidden_features, out_features):
        super(Net, self).__init__()
        # 隐层层
        self.hidden = torch.nn.Linear(in_features=n_features, out_features=hidden_features)
        # 输出层
        self.predict = torch.nn.Linear(in_features=hidden_features, out_features=out_features)

    # 前向传播
    def forward(self, x):
        # 输入数据，经过隐藏层
        x = torch.relu(self.hidden(x))
        # 从隐藏层出来的数据，进入输出层
        x = self.predict(x)
        # 返回输出值
        return x


# 实例化神经网络
net = Net(2, 2, 2)
# 神经网络各层的情况
print(net)

# 优化器
optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
# 损失函数
loss_fuc = torch.nn.CrossEntropyLoss()

# 打开交互模式
plt.ion()

# 训练过程,100个时间步
for t in range(100):
    # 神经网络预测
    out = net.predict(x)
    # 和真实比较
    loss = loss_fuc(out, y)
    # 梯度清零
    net.zero_grad()
    # 误差反向传播
    loss.backward()
    # 优化器逐步优化
    optimizer.step()

    if t % 2 == 0:
        # 清空绘图区域
        plt.cla()
        # 输出分类之后，最大概率值所在的位置(其实就是被分成的那一类)
        prediction = torch.max(out, 1)[1]
        # 预测之后，所有数据的标签（属于0类还是1类）
        pred_y = prediction.data.numpy()
        # 原来被打上的标签的数据（最开始设定的0类和1类）
        target_y = y.data.numpy()
        # 绘制散点图
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0, cmap='RdYlGn')
        # 准确率=预测正确的数据总数/数据总数
        accuracy = float((pred_y == target_y).astype(int).sum()) / float(target_y.size)
        # 显示文本——准确率
        plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color':  'red'})
        plt.pause(0.2)

# 关闭交互模式
plt.ioff()
plt.show()
