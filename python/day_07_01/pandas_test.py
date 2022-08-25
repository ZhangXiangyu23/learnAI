# coding:utf-8
import pandas as pd
import numpy as np
# 通过pandas生成序列

# # NAN :not a number,但是类型是float
# s = pd.Series([1, 3, 6, np.NAN, 66, 88])
# print(s)

# 生成一个日期序列，生成六个数据
dates = pd.date_range('20220822', periods=6)
# print(dates)

# # 6行4列 ，日期使用的是上面的8.22到8.27
# # DataFrame非常类似于Excel表格，最左侧为行名称，最上面是列名称
# # index代表行名称，column代表列名称
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
# print(df)
#
# print("-" * 50)
# # 使用DataFrame的默认行名称和列名称
# df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
# print(df1)

# # 使用字典作为DateFrame的参数
# # 字典的key作为列名，value作为一列中的数值，行数取决于列中最多元素数量
df2 = pd.DataFrame({'A': 1.0, 'B': pd.Timestamp('20210701'),
                    'C': pd.Categorical(['test1', 'test2', 'test3', 'test4']), 'D': 'ff'})
# print(df2)
# # 输出数据类型
# print(df2.dtypes)
# # 打印行名称
# print(df2.index)
# # 打印列名称
# print(df2.columns)
#
# # 打印值
# print(df2.values)
# # 打印描述信息
# print(df2.describe())

# 转置
print(df2.T)

# # 排序, axis=1指的是列名称；axis=0指的是行名称，ascending=False表示逆序
# df2 = df2.sort_index(axis=1, ascending=False)
#
# print(df2)
# print("-" * 50)
# df2 = df2.sort_index(axis=0, ascending=False)
# print(df2)
#
# print("%" * 50)
# # 根据C列数值进行排序
# df2 = df2.sort_values(by='C')
# print(df2)