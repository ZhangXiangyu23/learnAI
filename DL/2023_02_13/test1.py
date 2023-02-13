# coding:utf-8

import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

x = torch.linspace(-5, 5, 200)
y_relu = torch.relu(x)
y_tanh = torch.tanh(x)
y_sigmoid = torch.sigmoid(x)
y_softplus = F.softplus(x)

# 绘制图片
plt.figure()

# 绘制子图
plt.subplot(221)
plt.plot(x, y_relu, c="red", label="relu")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend(loc="best")

plt.subplot(222)
plt.plot(x, y_tanh, c="red", label="tanh")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend(loc="best")

plt.subplot(223)
plt.plot(x, y_sigmoid, c="red", label="sigmoid")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend(loc="best")

plt.subplot(224)
plt.plot(x, y_softplus, c="red", label="softplus")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend(loc="best")

# 展示
plt.show()