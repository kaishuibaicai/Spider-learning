from tkinter import *
from tkinter.dialog import *



def myDialog():
    d = Dialog(None, title = '果果大调查', text = '果果漂亮吗？', bitmap = DIALOG_ICON, default = 0, strings = ('漂亮', '超级漂亮', '漂亮的不忍直视'))
    print(d.num)

btn_begin = Button(None, text = '果果大调查', command = myDialog)
btn_begin.pack()

btn_quit = Button(None, text = '关闭', command = btn_begin.quit)
btn_quit.pack()


btn_begin.mainloop()