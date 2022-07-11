# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
import torch.nn.functional as F

"""
    激活函数的展示
"""

# 造数据, 数值范围是-5~5, 生成200个值, 每个值之间均匀间隔
x = np.linspace(-5, 5, 200)
# 将numpy格式转成tensor格式
x_tensor = torch.from_numpy(x)
# 将tensor格式转成variable形式
variable = Variable(x_tensor)

y_relu = torch.relu(x_tensor).data.numpy()
y_sigmoid = torch.sigmoid(x_tensor).data.numpy()
y_tanh = torch.tanh(x_tensor).data.numpy()
y_softmax = torch.softmax(dim=0, input=x_tensor).data.numpy()

# 都是numpy形式才能用matplotlib进行绘图
fig = plt.Figure()
# y_relu
plt.subplot(221)
plt.plot(x, y_relu, c="red", label="relu")
plt.ylim(-1, 5)
plt.legend(loc="best")

# y_sigmoid
plt.subplot(222)
plt.plot(x, y_sigmoid, c="green", label="sigmoid")
plt.ylim(-1, 5)
plt.legend(loc="best")

# y_tanh
plt.subplot(223)
plt.plot(x, y_tanh, c="blue", label="tanh")
plt.ylim(-1, 5)
plt.legend(loc="best")

# y_softmax
plt.subplot(224)
plt.plot(x, y_softmax, c="yellow", label="softmax")
plt.ylim(-1, 5)
plt.legend(loc="best")

# 展示
plt.show()




