# coding:utf-8
import numpy as np
import pandas as pd

"""
   在指定位置进行替换值 
"""

dates = pd.date_range('20220701', periods=6)
# print(dates)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

# 改变指定位置的值
# 通过位置进行改变
df.iloc[2, 2] = 666
print("-" * 50)
print(df)

# 通过标签进行改变
df.loc['20220701', 'B'] = 999
print("-" * 50)
print(df)

df['D'] = np.NAN
print(df)


# 在DataFrame上新加一列
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20220701', periods=6))
print("-" * 50)
print(df)

# 条件判断，只要A列中有大于0的所有行的所有数据全部改变！
df[df.A > 0] = 2222
print(df)




