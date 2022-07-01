# coding:utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# 对数据进行累加
data = data.cumsum()
data.plot()
plt.show()

# 使用dataframe
data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=["A", "B", "C", "D"])

# 进行累计
data = data.cumsum()
# print(data.head(5))
data.plot()
# 展示
plt.show()

ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)
plt.show()