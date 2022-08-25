# coding:utf-8
import numpy as np
import pandas as pd

"""
    merge的使用
"""

# # 可以将dataframe的格式理解成数据库中的表
# left = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
#                     'A':['A0', 'A1', 'A2', 'A3'],
#                     'B':['B0', 'B1', 'B2', 'B3']})
#
# right = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
#                     'C':['C0', 'C1', 'C2', 'C3'],
#                     'D':['D0', 'D1', 'D2', 'D3']})
#
# print(left)
# print("-" * 50)
# print(right)
# print("-" * 50)
# # 通过merge进行合并
# # 基于key列进行合并
# res = pd.merge(left, right, on='key')
# print(res)

# print("-" * 50)
# left = pd.DataFrame({'key1':['K0', 'K0', 'K1', 'K2'],
#                      'key2':['K0', 'K1', 'K0', 'K1'],
#                     'A':['A0', 'A1', 'A2', 'A3'],
#                     'B':['B0', 'B1', 'B2', 'B3']})
#
# right = pd.DataFrame({'key1':['K0', 'K1', 'K1', 'K2'],
#                       'key2':['K0', 'K0', 'K0', 'K0'],
#                     'C':['C0', 'C1', 'C2', 'C3'],
#                     'D':['D0', 'D1', 'D2', 'D3']})
#
# print(left)
# print("-" * 50)
# print(right)
#
# # 使用merge进行合并,默认合并方式是inner,去掉
#
# # how四种方式：inner 、outer 、left 、right
# print("-" * 50)
# res = pd.merge(left, right, on=['key1', 'key2'], how="left")
# print(res)

# df1 = pd.DataFrame({'col1':[0, 1], 'col_left':['a', 'b']})
# df2 = pd.DataFrame({'col1':[1, 2, 2], 'col_right':[2, 2, 2]})
# print("-" * 50)
# print(df1)
# print("-" * 50)
# print(df2)
#
# # indicator参数表示显示合并方式，indicator_column为显示合并方式列的列名
# res = pd.merge(df1, df2, on='col1', how='outer', indicator="indicator_column")
# print("-" * 50)
# print(res)

# left = pd.DataFrame({'A':['A0', 'A1', 'A2'],
#                      'B':['B0', 'B1', 'B2']},
#                     index=['K0', 'K1', 'K2'])
#
# right = pd.DataFrame({'C':['C0', 'C1', 'C2'],
#                       'D':['D0', 'D1', 'D2']},
#                      index=['K0', 'K2', 'K3'])
#
# print("-" * 50)
# print(left)
# print("-" * 50)
# print(right)
# print("-" * 50)
# # 这里的how参数outer指的是，合并左侧索引和右侧索引
# res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
# print(res)

boys = pd.DataFrame({'k':['K0', 'K1', 'K2'], 'age':[1, 2, 3]})
girls = pd.DataFrame({'k':['K0', 'K0', 'K3'], 'age':[4, 5, 6]})

print("-" * 50)
print(boys)
print("-" * 50)
print(girls)

# suffixes参数合并之后，重命名列名，在原来列表后面进行修改，以显示不同
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer')
print("-" * 50)
print(res)