# coding:utf-8
import numpy as np
import pandas as pd

dates = pd.date_range('20220701', periods=6)
# print(dates)
df = pd.DataFrame(np.arange(24).reshape(6,4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

# 改变数据
df.iloc[0, 1] = np.NAN
df.iloc[1, 2] = np.NAN
print("-" * 50)
print(df)


"""
    丢弃nan
"""

# 丢弃nan, anis表示行， how的方式是：
# all的话，就是一整行或者一整列都是nan的话,才进行丢弃
# any的话，只要一行里面或者一列里面有nan,就丢弃整行或者整列
df = df.dropna(axis=1, how='all')
print("-" * 50)
print(df)


"""
    替换nan
"""
# df = df.fillna(value=0)
print(df.fillna(value=0))

# 看看是否确实数据
print(df.isnull())

# 看看df中是否有True
print("-" * 50)
print(np.any(df.isnull()) == True)