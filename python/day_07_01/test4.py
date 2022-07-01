import numpy as np
import pandas as pd
"""
    用pandas导入导出数据
"""

# 读取数据
data = pd.read_csv("AAH691(2).csv", encoding='gb18030')
print(data)

# 保存成pickle格式的文件
# 保存数据
data.to_pickle('test.pickle')