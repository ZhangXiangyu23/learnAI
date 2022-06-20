# coding:utf-8
import tkinter as tk
"""
    框架frame的使用
"""

# 创建窗口
window = tk.Tk()
# 设定窗口的标题
window.title("其实就是划分区域呗")
# 设定窗口的尺寸
window.geometry("1000x500")

# 先创建标签,并放置
l = tk.Label(text="on the window").pack()
# 窗口里面的大框架
frm = tk.Frame(window)
# 放置这个框架
frm.pack()


# 左侧框架
frm1 = tk.Frame(frm,)
# 将框架放置到左侧
frm1.pack(side="left")

# 右侧框架
frm2 = tk.Frame(frm,)
# 将框架放置到右侧
frm2.pack(side="right")

# 划分好区域之后，进行分区域放标签
tk.Label(frm1, text="左侧标签1").pack()
tk.Label(frm1, text="左侧标签2").pack()
tk.Label(frm2, text="右侧标签").pack()



# 使窗口循环起来
window.mainloop()