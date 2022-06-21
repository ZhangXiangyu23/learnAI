# coding:utf-8
import tkinter as tk
"""
    pack、grid、place三种放置方式
"""


# 获取窗口
window = tk.Tk()
# 设定窗口的标题
window.title("放置组件的三种方法")
# 设定窗口尺寸
window.geometry("1000x500")

# 以最西北方向为坐标原点，在具体的xy坐标位置,放置
tk.Label(window, text="啊啊啊啊").place(x=100, y=100, anchor="nw")

# 循环起来
window.mainloop()
