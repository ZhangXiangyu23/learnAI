# coding:utf-8
import tkinter as tk
"""
    列表的使用
"""

# 获取窗口
window = tk.Tk()
# 设定窗口的名称
window.title("列表的使用")
# 设定窗口的尺寸
window.geometry("1000x500")

var1 = tk.StringVar()
# 创建标签
l = tk.Label(window, textvariable=var1, bg="yellow", width=15, height=2)
# 放置标签
l.pack()


def job():
    # 获取现在鼠标点击项的内容
    v = lb.get(lb.curselection())
    # 设定标签内容
    var1.set(v)


# 创建按钮
b = tk.Button(window, text="你给我上去", command=job)

# 放置按钮
b.pack()

var2 = tk.StringVar()
var2.set(("清华大学", "北京大学", "复旦大学", "交通大学"))
# 创建列表盒子
lb =tk.Listbox(window, listvariable=var2)
list_item = [1, 2, 3, 4]
# 循环插入
for m in list_item:
    lb.insert("end", m)

lb.insert(1, "first")
lb.insert(2, "second")
lb.delete(2)
lb.pack()

# 循环窗口
window.mainloop()