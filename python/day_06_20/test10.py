# coding:utf-8
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
"""
    弹窗的使用
"""

# 获取窗口
window = tk.Tk()
# 设置窗口标题
window.title("弹窗的使用")
# 设置窗口的大小
window.geometry("1000x500")

def job():
    # 弹窗展示信息
    tkinter.messagebox.showinfo(title="Hi", message='hahahah')
    # warning
    # tkinter.messagebox.showwarning(title="warining", message="警告")
    # error
    # tkinter.messagebox.showerror(title="error", message="错误")
    # 询问框,返回yes或者no
    # print(tk.messagebox.askquestion(title="询问yes或no", message="Are you OK?"))
    # 询问框，返回True或者FALSE
    # print(tk.messagebox.askyesno(title="询问true或false", message="Do you love me?"))
    # 询问确认还是取消,返回true和false
    # print(tk.messagebox.askokcancel(title="购物", message="确定要购买吗?"))
    # 询问重试还是取消，返回true和false
    # print(tk.messagebox.askretrycancel(title="爱", message="你爱我吗?"))


b = tk.Button(window, text="点我试试", command=job).pack()


# 循环起来
window.mainloop()
