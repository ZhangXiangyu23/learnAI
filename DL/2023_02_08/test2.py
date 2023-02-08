# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F

# 生成数据
data = torch.linspace(-5, 5, 200)
y_relu = torch.relu(data)
y_sigmoid = torch.sigmoid(data)
y_tanh = torch.tanh(data)
y_softplus = F.softplus(data)

# 绘图
plt.figure()

# 绘制子图
plt.subplot(221)
plt.plot(data, y_relu, c="red", label="relu")
plt.ylim(-1, 5)
plt.legend(loc="best")

plt.subplot(222)
plt.plot(data, y_sigmoid, c="red", label="sigmoid")
plt.ylim(-1, 5)
plt.legend(loc="best")

plt.subplot(223)
plt.plot(data, y_tanh, c="red", label="tanh")
plt.ylim(-1, 5)
plt.legend(loc="best")

plt.subplot(224)
plt.plot(data, y_softplus, c="red", label="softplus")
plt.ylim(-1, 5)
plt.legend(loc="best")

# 展示
plt.show()