# coding:utf-8
import numpy as np
import pandas as pd

"""
    pandas中的合并
"""

# 创建数据框架
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'])

# print("-" * 50)
# print(df1)
# print("-" * 50)
# print(df2)
# print("-" * 50)
# print(df3)

# # 使用函数，在竖直方向进行合并, axis为0时，表示竖直方向的合并
# # axis为1时，表示水平方向的合并
# print("-" * 50)
# # ignore_index=True表示对合并之后的数据进行重新排序
# res = pd.concat([df1, df2, df3], axis=1)
# print(res)

# print("-" * 50)
# df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
# df2 = pd.DataFrame(np.ones((3, 4))*2, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
# print(df1)
# print("-" * 50)
# print(df2)

# # 使用concat进行合并
# # 默认join是outer; 也可以使用inner
# # inner合并相同列；outer全部并起来，没有的列用NaN填充
# # ignore_index使得合并之后，顺序井然
# # inner类似于交集，outer类似于并集
# res = pd.concat([df1, df2], join="inner", ignore_index=True)
# print("-" * 50)
# print(res)

# # 横向合并
# res = pd.concat([df1, df2], axis=1)
# print("-" * 50)
# print(res)

# """
#     append的使用，默认数据框架df进行纵向合并，添加到最下面
# """
df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
# df2 = pd.DataFrame(np.ones((3, 4))*2, columns=['a', 'b', 'c', 'd'], index=[2, 3, 4])
# df3 = pd.DataFrame(np.ones((3, 4))*3, columns=['a', 'b', 'c', 'd'], index=[2, 3, 4])
print("-" * 50)
print(df1)
print("-" * 50)
# print(df2)
# print("-" * 50)
# print(df3)
# print("-" * 50)
# # 参数ignore_index为True是为了让索引有序！！！
# res = df1.append([df2, df3], ignore_index=True)
# print(res)


# 添加序列
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s1)
print("-" * 50)
res = df1.append(s1, ignore_index=True)
print(res)