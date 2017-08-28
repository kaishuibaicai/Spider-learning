from tkinter import *

root = Tk()

menuBar = Menu(root)

for item in ['文件', '编辑', '视图', '关于']:
    menuBar.add_command(label = item)

root['menu'] = menuBar
root.mainloop()
