from tkinter import *

root = Tk()
root.title('我是果果窗口')
lr = Label(root, text = '我是属于果果的窗口')
lr.pack()
canv1 = Canvas(root, width = 400, height = 300, bg = '#00ffaa')
canv1.create_line((0,0), (400,300), width = 3)
canv1.pack()

top = Toplevel(root, width = 30, height = 20)
top.title('我是图图窗口')
lt = Label(top, text = '我是属于图图的窗口')
lt.pack()
canv2 = Canvas(top, width = 400, height = 300, bg = '#00ffaa')
canv2.create_line((400,0), (0,300), width = 3)
canv2.pack()

root.mainloop()