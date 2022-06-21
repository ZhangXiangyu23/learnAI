# coding:utf-8
import tkinter as tk
"""
    entry和text控件的使用
"""

# 获取上窗口
window = tk.Tk()
# 设定窗口的名称
window.title("小把戏")
# 设定窗口的尺寸
window.geometry("1000x500")

# 设定输入框
entry = tk.Entry(window, show=None)
# 放置输入框
entry.pack()

# 末尾插入
def insert_end():
    e_content = entry.get()
    t.insert("end", e_content)


# 插入点进行插入
def insert_point():
    e_content = entry.get()
    t.insert("insert", e_content)


# 设定按钮1,最末尾进行插入
b1 = tk.Button(window, text="end insert", command=insert_end)
# 设定按钮2，在插入点进行插入
b2 = tk.Button(window, text="point insert", command=insert_point)


# 放置按钮1
b1.pack()
# 放置按钮2
b2.pack()

# 设定显示框
t = tk.Text()
# 放置位置
t.pack()


# 让窗口循环起来,保持不断的更新
window.mainloop()