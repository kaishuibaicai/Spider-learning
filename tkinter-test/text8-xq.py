from tkinter import *

root = Tk()
root.title('中国象棋盘机绘')

canv = Canvas(root, width = 400, height = 450)
canv.create_line((0,2), (400,2), width = 2)

for i in range(10):
    canv.create_line((0, i*50), (400, i*50), width = 2)
canv.create_line((3,0), (3,450), width = 2)

for i in range(8):
    canv.create_line((i*50, 0), (i*50, 200), width = 2)

for i in range(8):
    canv.create_line((i*50, 250), (i*50, 450), width = 2)

canv.create_line((397, 0), (397, 450), width = 2)
canv.create_line((150, 0), (250, 100), width = 2)
canv.create_line((150, 100), (250, 0), width = 2)
canv.create_line((150, 450), (250, 350), width = 2)
canv.create_line((150, 350), (250, 450), width = 2)
canv.create_text(110, 220, text = '楚河')
canv.create_text(290, 220, text = '汉界')

canv.pack()
root.mainloop()