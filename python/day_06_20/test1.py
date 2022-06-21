# coding:utf-8

# 导入tkinter库，并且重命名为tk
import tkinter as tk

# 通过tk创建窗口
window = tk.Tk()
# 给窗口起个标题
window.title("新的窗口")
# 设定窗口的尺寸
window.geometry("1000x500")

# 创建组件中字符串变量，在组件里面使用
var = tk.StringVar()
# 设定标签，第一个参数是该组件的父组件，其他参数设定具体属性
l = tk.Label(window, textvariable=var, bg="red", font=("Arial", 12), width=15,
             height=2)
# 防止标签
l.pack()

on_hit = False
def hit():
    global on_hit
    # 默认最初没有点
    if on_hit == False:
        on_hit = True
        # 通过set方法设定组件中的变量
        var.set("你点击我了")
    else:
        on_hit = False
        var.set("")

# 创建按钮，并通过command进行点击后的函数处理
b = tk.Button(window, text="hit me", width=15, height=2, command=hit)
# 放置按钮
b.pack()

# 让窗口保持不断更新
window.mainloop()

