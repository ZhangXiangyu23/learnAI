import numpy as np
import pandas as pd
"""
    用pandas导入导出数据
"""

# 读取数据，可以读取各自格式的数据。比如：read_csv、read_excel、read_html
data = pd.read_csv("AAH691(2).csv", encoding='gb18030')
# print(data)

# 保存成pickle格式的文件,也可以保存成其他格式的问题，比如csv、html等。与读取一一对应
# 保存数据
data.to_pickle('test.pickle')