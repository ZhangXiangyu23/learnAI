# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    图像image
"""
# 表示把一个一维数组重新生成一个3行3列的二维数组
a = np.array([0.313660827978,0.365348418405,0.423733120134,0.365348418405,0.439599930621,0.525083754405,
0.423733120134,0.525083754405,0.651536351379]).reshape(3,3)

# interpolation表示间隔形式  cmap表示颜色  origin:绘制方向，lower从下向上绘制，upper从上向下绘制
plt.imshow(a, interpolation='nearest', cmap='rainbow', origin='lower')

# shrink参数是将colorbar高度压缩为图像比例的0.5
plt.colorbar(shrink=0.5)

plt.xticks(())
plt.yticks(())
plt.show()