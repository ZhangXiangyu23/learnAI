# coding:utf-8
import tkinter as tk

"""
    画布的使用
"""

# 创建窗口
window = tk.Tk()
# 设定窗口的标题
window.title("画布的使用")
# 设定画布的尺寸
window.geometry("1000x500")

# 创建画布
canvas = tk.Canvas(window, bg="blue", height=400, width=700)
# 加载图片文件
image_file = tk.PhotoImage(file="F:\\研究生0年级\\learnAI\\a.png")
# 将图片放在画布中的具体位置
image = canvas.create_image(10, 10, anchor="nw", image = image_file)


# 画布中画各种形状
x0, y0, x1, y1 = 50, 50 ,80, 80
# 画线
line = canvas.create_line(x0, y0, x1, y1)
# 圆型
circular = canvas.create_oval(x0, y0, x1, y1, fill="red")
# 扇形
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=120)
# 正方形,边长为20
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)

canvas.pack()

# 移动函数
def move():
    canvas.move(rect, 0, 20)

# 按钮
b = tk.Button(window, text="移动", command=move)
b.pack()
# 循环起来
window.mainloop()