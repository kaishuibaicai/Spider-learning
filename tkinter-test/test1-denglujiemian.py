from tkinter import *
from tkinter.ttk import *

def reg():
    myAccount = a_entry.get()
    myPassword = p_entry.get()
    a_len = len(myAccount)
    p_len = len(myPassword)

    if myAccount == 'guoguo' and myPassword == 'love':
        msg_label['text'] = '登陆成功'
    elif myAccount == 'guoguo' and myPassword != 'love':
        msg_label['text'] = '密码错误'
        p_entry.delete(0, p_len)
    else:
        msg_label['text'] = '用户名错误'
        a_entry.delete(0, a_len)
        p_entry.delete(0, p_len)

root = Tk()

a_label = Label(root, text = '用户名：')
a_label.grid(row = 0, column = 0, sticky = W)
a_entry = Entry(root)
a_entry.grid(row = 0, column = 1, sticky = E)

p_label = Label(root, text = '密码：')
p_label.grid(row = 1, column = 0, sticky = W)
p_entry = Entry(root)
p_entry.grid(row = 1, column = 1, sticky = E)

btn = Button(root, text = '登录', command = reg)
btn.grid(row = 3)

msg_label = Label(root, text = '')
msg_label.grid(row = 3)
root.mainloop()