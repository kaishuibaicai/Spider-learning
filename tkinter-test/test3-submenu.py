from tkinter import *


root = Tk()
menuBar = Menu(root)
mouseBar = Menu(root)
fMenu = Menu(menuBar)
def myLabel():
    global root
    Label(root, text = '我的Python课程').pack()


for item in ['C/C++', 'JavaEE', 'Android', 'PHP', 'UI设计', 'ios', '前端与移动开发', '网络营销', '云计算']:
    mouseBar.add_radiobutton(label = item)
mouseBar.add_separator()

for item in ['和果果学', '和图图学', '大家一起学', '自学']:
    mouseBar.add_checkbutton(label = item)

mouseBar.add_separator()

for item in ['新建', '打开', '保存', '另存为', '退出']:
    fMenu.add_command(label = item)

eMenu = Menu(menuBar)
for item in ['复制', '粘贴', '剪切', '撤销']:
    eMenu.add_command(label = item)

vMenu = Menu(menuBar)
for item in ['默认视图', '全屏视图', '显示/隐藏视图']:
    vMenu.add_command(label = item)

aMenu = Menu(menuBar)
for item in ['版权信息', '帮助文档']:
    aMenu.add_command(label = item)

menuBar.add_cascade(label = '文件', menu = fMenu)
menuBar.add_cascade(label = '编辑', menu = eMenu)
menuBar.add_cascade(label = '视图', menu = vMenu)
menuBar.add_cascade(label = '关于', menu = aMenu)
mouseBar.add_command(label = 'Python', command = myLabel)



def pop(event):
    mouseBar.post(event.x_root, event.y_root)

root.bind('<Button-3>', pop)

root['menu'] = menuBar

root.mainloop()