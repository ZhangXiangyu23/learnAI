# coding:utf-8
import tkinter as tk
"""
    登录案例
"""

# 获取窗口
window = tk.Tk()
# 设置窗口的标题
window.title("登录界面")
# 设置窗口的尺寸
window.geometry("1000x500")

# 建立一个画布
canvas = tk.Canvas(window, width=1000, height=200, bg="blue")
# 防止画布
canvas.pack()
image_file = tk.PhotoImage(file="img_1.png")
# 将图片文件放到画布中
canvas.create_image(0, 0,anchor="nw", image = image_file)

# 用户名标签
username_l = tk.Label(window, text="用户名", font="楷体")
username_l.place(x=301, y=251)

# 密码标签
password_l = tk.Label(window, text="密码", font="楷体")
password_l.place(x=301, y=301)


# 用户名输入框
username_entry = tk.Entry(window)
username_entry.place(x=401, y=251)

# 密码输入框
password_entry = tk.Entry(window)
password_entry.place(x=401, y=301)





# 将窗口循环起来
window.mainloop()

