# coding:utf-8
import numpy as np
import pandas as pd

"""
    merge的使用
"""

left = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                    'D':['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

# 通过merge进行合并
res = pd.merge(left, right, on='key')
print(res)

print("-" * 50)
left = pd.DataFrame({'key1':['K0', 'K0', 'K1', 'K2'],
                     'key2':['K0', 'K1', 'K0', 'K1'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1':['K0', 'K1', 'K1', 'K2'],
                      'key2':['K0', 'K0', 'K0', 'K0'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                    'D':['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

# 使用merge进行合并,默认合并方式是inner,去掉

# how四种方式：inner 、outer 、left 、right
print("-" * 50)
res = pd.merge(left, right, on=['key1', 'key2'], how="outer")
print(res)