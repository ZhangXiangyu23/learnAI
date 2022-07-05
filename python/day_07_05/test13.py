# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

"""
    在一张图里面画多张图的其他方法
"""


# 方法一：subplot2grid
# plt.figure()
# ax1 = plt.subplot2grid((3,3), (0,0), rowspan=1, colspan=3)
# ax1.plot([1, 2], [1, 2])
# ax1.set_title("ax1_title")
# ax2 = plt.subplot2grid((3, 3), (1, 0), rowspan=1, colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2, colspan=1)
# ax4 = plt.subplot2grid((3, 3), (2, 0), rowspan=1, colspan=1)
# ax5 = plt.subplot2grid((3, 3), (2, 1), rowspan=1, colspan=1)

# 方法二：
# plt.figure()
# gs = gridspec.GridSpec(3, 3)
# ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1, :2])
# ax3 = plt.subplot(gs[1:, 2])
# ax4 = plt.subplot(gs[-1,0])
# ax5 = plt.subplot(gs[-1,-2])

# 方法三：
# 共享X轴和Y轴
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])
ax12.scatter([1, 2], [1, 2])
ax21.scatter([1, 2], [1, 2])
ax22.scatter([1, 2], [1, 2])

plt.show()