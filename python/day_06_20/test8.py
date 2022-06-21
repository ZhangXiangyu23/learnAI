# coding:utf-8
import tkinter as tk
"""
    menubar菜单栏
"""

# 获取窗口
window = tk.Tk()
# 设定窗口名称
window.title("菜单栏的使用")
# 设定窗口的大小
window.geometry("1000x500")

# 放一个标签
l = tk.Label(window, text="", width=50, height=5, bg="yellow")
l.pack()

counter = 0
def job():
    global counter
    l.config(text="do %d" %counter)
    counter += 1


# 获取菜单栏
menubar = tk.Menu(window)

# 菜单1之文件菜单
filemenu = tk.Menu(menubar, tearoff=0)
# 使用菜单栏将文件菜单添加进去
menubar.add_cascade(label="文件", menu=filemenu)
filemenu.add_command(label="新建", command=job)
filemenu.add_command(label="打开", command=job)
filemenu.add_command(label="保存", command=job)
# 分割线
filemenu.add_separator()
# 退出
filemenu.add_command(label="退出", command=window.quit)

# 菜单2之大学
universitymenu = tk.Menu(menubar, tearoff=0)
# 使用菜单栏将菜单2添加进去
menubar.add_cascade(label="大学", menu=universitymenu)
universitymenu.add_command(label="清华大学", command=job)
universitymenu.add_command(label="北京大学", command=job)
universitymenu.add_command(label="浙江大学", command=job)


# 创建二级菜单，文件菜单是一级菜单，所以是父组件
second_menu = tk.Menu(filemenu)
# 文件菜单父组件将二级菜单进行添加
filemenu.add_cascade(label="导入", menu=second_menu, underline=0)
# 二级菜单中放具体项
second_menu.add_command(label="你好",command=job)



# 将创建的菜单栏，修改进原窗口中
window.config(menu=menubar)
# 循环起来
window.mainloop()
