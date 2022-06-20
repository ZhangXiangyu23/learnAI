# coding:utf-8
import tkinter as tk

window = tk.Tk()
window.title("新的窗口")
window.geometry("1000x500")

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg="red", font=("Arial", 12), width=15,
             height=2)
l.pack()

on_hit = False
def hit():
    global on_hit
    # 默认最初没有点
    if on_hit == False:
        on_hit = True
        var.set("你点击我了，滚开")
    else:
        on_hit = False
        var.set("")

b = tk.Button(window, text="hit me", width=15, height=2, command=hit)
b.pack()

window.mainloop()

