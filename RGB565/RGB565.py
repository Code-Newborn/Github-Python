# 借鉴于 https://blog.csdn.net/wild_lee/article/details/122009234
# RGB888 转换 RGB565

from tkinter import *
import re

window = Tk()
window.title("RGB888 转换 RGB565")
window.geometry("450x300+300+250")


def scalecommand(color):

    # print(s1.get(),s2.get(),s3.get())
    b = s3.get()
    g = s2.get()
    r = s1.get()

    R = r & 0xF8
    G = g & 0xFC
    B = b & 0xF8

    rgb565 = (R << 8) | (G << 3) | (B >> 3)

    rgb888 = (r << 16) | (g << 8) | b

    rgb888_text = "RGB888: " + "#%06x" % rgb888
    rgb888_Label.configure(text=rgb888_text)

    rgb565_text = "RGB565: " + "%#06x" % rgb565
    rgb565_Label.configure(text=rgb565_text)

    # print("%#08X"%rgb)
    info_Label.configure(bg="#%06x" % rgb888)


def HexToDec(value):
    try:
        return int(value, 16)
    except ValueError:
        return "Invalid Hexadecimal Value"


def buttonClick1():
    # RGB888 转 RGB565

    try:
        c888 = int(rgb1_Entry.get(), 16)  # 字符转16进制整数
    except ValueError:
        print("Invalid Hexadecimal Value")
        return

    rgb2_Entry.delete(0, END)

    if c888 == None:
        return
    else:

        b = c888 & 0xFF  # 转换RB 取得rgb颜色B
        g = int((c888 & 0xFF00) >> 8)  # 转换G 取得rgb颜色G
        r = int((c888 & 0xFF0000) >> 16)  # 转换R 取得rgb颜色R
        R = r & 0xF8  # 取得RGB565的5位R
        G = g & 0xFC  # 取得RGB565的5位G
        B = b & 0xF8  # 取得RGB565的5位B

        rgb565 = (R << 8) | (G << 3) | (B >> 3)

        # print("%#06x" %rgb565)

        # 设置滑块位置
        s1.set(r)
        s2.set(g)
        s3.set(b)

        # 显示RGB888和RGB565颜色码
        info_Label.configure(bg="#%06x" % c888)
        rgb888_text = "RGB888: " + "#%06x" % c888
        rgb888_Label.configure(text=rgb888_text)
        rgb565_text = "RGB565: " + "%#06x" % rgb565
        rgb565_Label.configure(text=rgb565_text)


def buttonClick2():
    # RGB565 转 RGB888
    rgb1_Entry.delete(0, END)

    try:
        c565 = int(rgb2_Entry.get(), 16)
    except ValueError:
        print("Invalid Hexadecimal Value")
        return

    if c565 == None:
        return
    else:
        b = c565 & 0x001F  # 转换R
        g = int((c565 & 0x07E0))  # 转换G
        r = int((c565 & 0xF800))  # 转换B
        R = r >> 8
        G = g >> 3
        B = b << 3

        rgb888 = (R << 16) | (G << 8) | B

        # print("%#06x" %rgb888)

        s1.set(R)
        s2.set(G)
        s3.set(B)
        info_Label.configure(bg="#%06x" % rgb888)
        rgb888_text = "RGB888: " + "#%06x" % rgb888
        rgb888_Label.configure(text=rgb888_text)
        rgb565_text = "RGB565: " + "%#06x" % c565
        rgb565_Label.configure(text=rgb565_text)


Rgb1_Label = Label(window, text="RGB888 代码：", height=2, fg="#191970")
Rgb1_Label.place(x=20, y=25, anchor=NW)

R1_Label = Label(window, text="#", height=2, fg="#191970")
R1_Label.place(x=20, y=50, anchor=NW)
rgb1_Entry = Entry(window, width=10)
rgb1_Entry.place(x=40, y=60, anchor=NW)

Rgb2_Label = Label(window, text="RGB565 代码：", height=2, fg="#191970")
Rgb2_Label.place(x=20, y=85, anchor=NW)

R2_Label = Label(window, text="0x", height=2, fg="#191970")
R2_Label.place(x=20, y=110, anchor=NW)
rgb2_Entry = Entry(window, width=10)
rgb2_Entry.place(x=40, y=120, anchor=NW)


button1 = Button(window, text="转换", bg="#8FBC8F", command=buttonClick1)  # 转换按键
button1.place(x=160, y=40, anchor=NW)

button2 = Button(window, text="转换", bg="#8FBC8F", command=buttonClick2)  # 转换按键
button2.place(x=160, y=110, anchor=NW)

info_Label = Label(window, text="", height=10, width=20)  # 色块
info_Label.configure(bg="#FFFFFF")
info_Label.place(x=280, y=20, anchor=NW)

R_Label = Label(window, text="R", height=1, width=1)
R_Label.place(x=20, y=170, anchor=NW)
s1 = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=200, showvalue=1, tickinterval=0, resolution=1, command=scalecommand)  # 滑块R
s1.place(x=40, y=150, anchor=NW)

G_Label = Label(window, text="G", height=1, width=1)
G_Label.place(x=20, y=210, anchor=NW)
s2 = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=200, showvalue=1, tickinterval=0, resolution=1, command=scalecommand)  # 滑块G
s2.place(x=40, y=190, anchor=NW)

B_Label = Label(window, text="B", height=1, width=1)
B_Label.place(x=20, y=250, anchor=NW)
s3 = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=200, showvalue=1, tickinterval=0, resolution=1, command=scalecommand)  # 滑块B
s3.place(x=40, y=230, anchor=NW)

rgb888_Label = Label(window, text="RGB888:", height=1, width=18, fg="blue", anchor="w")
rgb888_Label.place(x=280, y=210)

rgb565_Label = Label(window, text="RGB565:", height=1, width=18, fg="blue", anchor="w")
rgb565_Label.place(x=280, y=250)


window.mainloop()
