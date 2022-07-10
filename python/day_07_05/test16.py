# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


"""
    使用动画显示数据
"""
# 生成子图，相当于fig = plt.figure(),ax = fig.add_subplot(),其中ax的函数参数表示把当前画布进行分割
fig, ax = plt.subplots()

# 范围是0~2π， 步长为0.01
x = np.arange(0, 2*np.pi, 0.01)
line, =ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,




# 生成动画
'''
函数FuncAnimation(fig,func,frames,init_func,interval,blit)是绘制动图的主要函数，其参数如下：
    a.fig 绘制动图的画布名称
    b.func自定义动画函数，即程序中定义的函数animate
    c.frames动画长度，一次循环包含的帧数，在函数运行时，其值会传递给函数animate(i)的形参“i”
    d.init_func自定义开始帧，即传入刚定义的函数init,初始化函数
    e.interval更新频率，以ms计
    f.blit选择更新所有点，还是仅更新产生变化的点。应选择True，但mac用户请选择False，否则无法显示
'''
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=True)

plt.show()