# coding:utf-8
import numpy as np
import pandas as pd
"""
    pandas从DateFrame中选取一行
"""

# 生成日期序列
dates = pd.date_range('2022.07.01', periods=6)

# 生成DateFrame
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
# # 选取第A列
# print(df.A)
# print("-" * 50)
# print(df['A'])

# print("-" * 50)
# # 按行切片,左闭右开
# print(df[1:3])
# print("&" * 50)
#
# # 按行索引名进行切片，左闭右闭
# print(df['20220703':'20220705'])

# # 根据行标签(行名)进行选取值
# print("-" * 50)
# print(df.loc['20220701'])

# # 选取列标签
# print("-" * 50)
# # 所有行中的B、C两列
# print(df.loc[:, ['B', 'C']])

# # 输出指定行中的，指定列
# print("-" * 50)
# print(df.loc["20220702", ['C', 'D']])

# # 根据位置进行筛选
# print("-" * 50)
# print(df.iloc[3])

# print("-" * 50)
# print(df.iloc[[1,3,5], 1:3])

# # 混合筛选：既用标签，又用位置   现在ix已经被抛弃了
# print(df.ix[:3, ['A', 'C']])

# 通过条件进行筛选,通过A列进行筛选，显示所有的信息
print("-" * 50)
print(df[df.A > 8])