# coding:utf-8
import tkinter as tk
from tkinter import messagebox
"""
    登录案例
"""
# 数据库
date_base = [{"username":"zxy", "password" :"123456"},
             {"username":"lxy", "password" :"123456"},
             ]


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
password_l = tk.Label(window, text="密码", font="楷体", )
password_l.place(x=301, y=301)

var_username = tk.StringVar()
var_password = tk.StringVar()

# 用户名输入框
username_entry = tk.Entry(window, width=30, textvariable=var_username)
username_entry.place(x=401, y=251)

# 密码输入框
password_entry = tk.Entry(window, width=30, textvariable=var_password, show="*")
password_entry.place(x=401, y=301)

var_register_username = tk.StringVar()
var_register_password = tk.StringVar()
var_confirm_password = tk.StringVar()


def do_register():
    register_username_v = var_register_username.get()
    register_password_v = var_register_password.get()
    confirm_password_v = var_confirm_password.get()
    if register_username_v == "":
        messagebox.showwarning(title="注册失败", message="用户名不能为空!")
    if register_password_v == "":
        messagebox.showwarning(title="注册失败", message="密码不能为空!")


    for item in date_base:
        if item.get("username") == register_username_v:
            messagebox.showwarning(title="注册失败", message="此用户名已经被注册！")


    if register_password_v != confirm_password_v:
        messagebox.showwarning(title="两次密码不一致", message="您两次输入的密码不一致啊!")

    if register_username_v != "" and register_password_v != "" and confirm_password_v != "" and register_password_v == confirm_password_v:
        date_base.append({"username": register_username_v, "password": register_password_v})
        messagebox.showinfo(title="注册成功", message=f"恭喜用户:{register_username_v}注册成功")


# 注册工作
def to_register():
    # 子窗口
    sub_window = tk.Toplevel(window)
    sub_window.title("注册界面")
    sub_window.geometry("800x400")

    # 用户名标签
    username_l = tk.Label(sub_window, text="用户名", font="楷体")
    username_l.place(x=201, y=51)

    # 密码标签
    password_l = tk.Label(sub_window, text="密码", font="楷体", )
    password_l.place(x=201, y=121)

    # 密码标签
    confirm_password_l = tk.Label(sub_window, text="确认密码", font="楷体", )
    confirm_password_l.place(x=201, y=191)

    # 用户名输入框
    username_entry = tk.Entry(sub_window, width=30, textvariable=var_register_username)
    username_entry.place(x=351, y=51)

    # 密码输入框
    password_entry = tk.Entry(sub_window, width=30, textvariable=var_register_password, show="*")
    password_entry.place(x=351, y=121)

    # 确认密码输入框
    confirm_password_entry = tk.Entry(sub_window, width=30, textvariable=var_confirm_password, show="*")
    confirm_password_entry.place(x=351, y=191)

    # 注册按钮
    register_button = tk.Button(sub_window, text="注册", font="楷体", command=do_register)
    register_button.place(x=351, y=251)


# 登录工作
def login_job():
    username_value = var_username.get()
    password_value = var_password.get()
    count = 0
    # 先看看有没有这个用户
    for j in date_base:
        count += 1
        # 存在的话，跳出循环
        if username_value == j.get("username"):
            break
        # 不存在时
        if username_value != j.get("username") and count == len(date_base):
            result = messagebox.askokcancel(title="该用户不存在", message="该用户不存在，亲，您是否马上去注册？")
            if result == True:
                to_register()


    for i in date_base:
        if username_value == i.get("username") and password_value == i.get("password"):
            messagebox.showinfo(title="登录成功", message=f"{username_value}，恭喜您登录成功!")
            break
        elif username_value == i.get("username") and password_value != i.get("password"):
            messagebox.showerror(title="登录失败", message="密码错误")




# 登录按钮
login_button =tk.Button(window, text="登录", font="楷体", command=login_job)
login_button.place(x=401, y=351)

# 注册按钮
register_button = tk.Button(window, text="注册", font="楷体", command=to_register)
register_button.place(x=521, y=351)





# 将窗口循环起来
window.mainloop()

