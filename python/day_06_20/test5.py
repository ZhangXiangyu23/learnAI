# coding:utf-8
import tkinter as tk
"""
    scale的使用
"""

# 获取窗口
window = tk.Tk()
# 设置窗口的标题
window.title("调节音量")
# 设置窗口的尺寸
window.geometry("1000x500")



# 设置标签
l = tk.Label(window, bg="yellow", width=30, height=2, text="")
# 放置标签
l.pack()

# scale部件，默认会将自己的值作为参数进行传递
def job(v):
    l.config(text="现在的音量是" + v)

# 定义一个scale，设定其长度，具体起始点，水平方向，精度等
scale = tk.Scale(window, length=500, orient=tk.HORIZONTAL,from_ = 0,to=100,
                 tickinterval=10, resolution=0.01, showvalue=1, command=job)
# 放置scale
scale.pack()



# 让窗口循环起来
window.mainloop()