# coding:utf-8
import tkinter as tk

"""
    多选按钮的使用
"""

# 创建窗口
window = tk.Tk()

# 设置窗口的标题
window.title("练习多选按钮")
# 设置窗口的尺寸
window.geometry("1000x500")

# 组件中的整数变量写法
var1 = tk.IntVar()
var2 = tk.IntVar()
# 标签
l = tk.Label(window, bg="yellow", text="", width=20, height=2)
# 放置标签
l.pack()

def job():
    if var1.get() == 1 and var2.get() == 0:
        l.config(text="I only love C++")
    elif var1.get() == 0 and var2.get() == 1:
        l.config(text="I only love Python")
    elif var1.get() == 0 and var2.get() == 0:
        l.config(text="I don't love either")
    else:
        l.config(text="I both love them")


# 多选按钮
cb1 = tk.Checkbutton(window, text="C++", variable=var1, onvalue=1, offvalue=0, command=job)
cb2 = tk.Checkbutton(window, text="Python", variable=var2, onvalue=1, offvalue=0, command=job)
cb1.pack()
cb2.pack()



# 循环
window.mainloop()