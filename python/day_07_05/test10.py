# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
    图像image
"""

a = np.array([0.313660827978,0.365348418405,0.423733120134,0.365348418405,0.439599930621,0.525083754405,
0.423733120134,0.525083754405,0.651536351379]).reshape(3,3)

plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')

# shrink参数是将colorbar高度压缩为图像的0.5
plt.colorbar(shrink=0.5)

plt.xticks(())
plt.yticks(())
plt.show()