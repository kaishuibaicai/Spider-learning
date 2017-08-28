from tkinter import *

timeA = 0
timeB = 0

def funA():
    global timeA, btnA, lab
    if timeA % 2 == 0:
        timeA += 1
        lab['text'] = '果果被选中'
    else:
        timeA += 1
        lab['text'] = '果果被取消选中'

def funB():
    global timeB, btnB, lab
    if timeB % 2 == 0:
        timeB +=1
        lab['text'] = '图图被选中'
    else:
        timeB +=1
        lab['text'] = '图图被取消选中'

root = Tk()
root.title('果果图图大选择')
btnA = Checkbutton(root, text = '果果', command = funA)
btnA.pack()

btnB = Checkbutton(root, text = '图图', command = funB)
btnB.pack()

lab = Label(root, text = '选图图还是果果？')
lab.pack()

reason = Label(root, text = '理由：')
reason.pack(side=LEFT)

t = Text(root, width = 50, height = 3)
t.pack()
root.mainloop()