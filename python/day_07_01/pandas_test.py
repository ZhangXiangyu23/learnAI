# coding:utf-8
import pandas as pd
import numpy as np
# 通过pandas生成序列

# NAN :not a number,但是类型是float
s = pd.Series([1, 3, 6, np.NAN, 66, 88])
print(s)

# 生成一个日期序列
dates = pd.date_range('20220701', periods=6)
print(dates)

# 6行4列 ，日期使用的是上面的7.01到7.06
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

print("-" * 50)
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

# 使用字典作为DateFrame的参数
df2 = pd.DataFrame({'A': 1.0, 'B': pd.Timestamp('20210701'),
                    'C': pd.Categorical(['test1', 'test2', 'test3', 'test4']), 'D': 'ff'})
print(df2)
print(df2.dtypes)
# 打印序列号
print(df2.index)
# 打印列号
print(df2.columns)

# 打印值
print(df2.values)
# 描述信息
print(df2.describe())

# 转置
print(df2.T)

# 排序, axis1指的是行头；axis0指的是列头
df2 = df2.sort_index(axis=0, ascending=False)
print("-" * 50)
print(df2)

# 根据值进行排序
df2 = df2.sort_values(by='C')
print(df2)