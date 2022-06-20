# coding:utf-8
import tkinter as tk
"""
    使用单选按钮
"""

window = tk.Tk()
window.title("抽奖系统")
window.geometry("1000x500")


# tkinter中的变量都是这样的
var = tk.StringVar()
# 使用标签显示单选之后的结果
l = tk.Label(window, text=" ", bg="green", width=30, height=2)
# 放置标签
l.pack()

def job():
    l.config(text = "恭喜您抽到了" + var.get())


# 创建单选按钮A
rb1 = tk.Radiobutton(window, text="礼物A", variable=var, value="MacBook", command=job)
rb1.pack()

# 创建单选按钮B
rb2 = tk.Radiobutton(window, text="礼物B", variable=var, value="iphone", command=job)
rb2.pack()

# 创建单选按钮C
rb3 = tk.Radiobutton(window, text="礼物C", variable=var, value="ipad", command=job)
rb3.pack()


# 循环起来
window.mainloop()