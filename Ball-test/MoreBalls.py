from random import randint
from tkinter import *
from tkinter.ttk import *

# 创建一个随机球处理类
class SettingBalls:
    def __init__(self, canvas, scrnwidth, scrnheight):
    	# __init__函数里设置对象的属性
        
        # 对象自己的属性，接受canvas参数
        # Canvas是一个长方形的面积，图画或其他复杂的布局。可以放置在画布上的图形，文字，部件，或是帧
        self.canvas = canvas

        # tkinter绘图采用屏幕坐标系，原点在左上角，x从左往右 递增, y从上往下 递增
        # 在绘图区域内，随机产生当前 球的圆心 的 x坐标 和 y坐标，用于制定出现的位置
        self.xpos = randint(10, int(scrnwidth))
        self.ypos = randint(10, int(scrnheight))

        # 在绘图区域内，随机产生当前球的 x坐标 和 y坐标 的向量
        # 在数学中，几何向量（也称矢量），指具有大小和方向的量
        # 这里我们可以用来表示球的速度
        self.xvelocity = randint(6, 12)
        self.yvelocity = randint(6, 12)

        # 随机产生表示当前球的大小，也就是半径长度
        self.radius = randint(40, 70)

        # 通过lambda表达式创建函数对象r，每次调用 r() 都会产生 0 ~ 255之间的数字
        r = lambda : randint(0, 255)

        # 三次调用的数字取前两位，用十六进制数方式存储到 self.color里，作为球的颜色
        # #RRGGBB，前2是红色，中2是绿色，后2是蓝色，最小是0，最大是F，
        # 如 全黑#000000  全白#FFFFFF 全红#FF0000
        self.color = "#%02x%02x%02x" % (r(), r(), r())

        # 获取整个绘图场景的宽度和高度（也就是屏幕分辨率大小）
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight


    def create_ball(self):

        # canvas.create_oval() 可以绘制一个圆
        # 但是需要传入圆的左、上、右、下四个坐标
        # 所以我们先产生四个坐标，通过这个四个坐标，绘制圆的大小

        # 左坐标 = x坐标 - 半径 
        x1 = self.xpos - self.radius
        # 上左边 = y坐标 - 半径
        y1 = self.ypos - self.radius
        # 右坐标 = x坐标 + 半径
        x2 = self.xpos + self.radius
        # 下坐标 = y坐标 - 半径
        y2 = self.ypos + self.radius

        # 通过canvas.create_oval()方法绘出整个圆，填充色 和 轮廓色分别是 self.color 生成的颜色
        self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = self.color)


    def move_ball(self):
        """
            进行相应的移动，如果坐标超过屏幕边缘则向相反方向移动
        """
        # 让球的x坐标和y坐标，按照向量的大小进行增加，表示球的运行，向下和向右
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 如果球的y坐标 大于等于 屏幕高度 和 球的半径 的差，则调整球的运行y轴方向朝上
        if self.ypos >= self.scrnheight - self.radius:
            self.yvelocity = -self.yvelocity

        # 如果球的y坐标 小于等于 屏幕高度 和 球的半径 的差，则调整球的y轴运行方向朝下
        if self.ypos <= self.radius:
            self.yvelocity = abs(self.yvelocity)

        # 如果球的x坐标 大于等于 屏幕宽度 和 球的半径 的差，则调整球的运行x轴方向朝左
        if self.xpos >= self.scrnwidth - self.radius:
            self.xvelocity = -self.xvelocity

        # 如果球的x坐标 小于等于 屏幕宽度 和 球的半径 的差，则调整球的运行x轴方向朝右
        if self.xpos <= self.radius:
            self.xvelocity = abs(self.xvelocity)

         # 调用canvas对象的move()方法可以让对象动起来，参数是对象，以及对象x轴和y轴的向量大小
        self.canvas.move(self.ball, self.xvelocity, self.yvelocity)

class MoreBalls:
    '''
        获取屏幕参数，绑定相关事件，以及启动生成小球的迭代器
        @ num: 从__main__里接受小球的数量
    '''
	# 定义一个列表，用来存储所有的球对象
    balls = []

    # num 是球的数量
    def __init__(self, num):

    	# 创建一个Tk()窗口实例
        self.root = Tk()

        # w 和 h 分别获取了屏幕分辨率的宽度和高度
        scrnw, scrnh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        #self.root.title("小球弹弹弹")
        # 去除窗口边框和任务栏显示
        self.root.overrideredirect(1)
        #self.root.iconbitmap("test.ico")
        # 设置窗口的透明度，0-1 之间，1是不透明，0是全透明。
        self.root.attributes("-alpha", 0.4)

        # 绑定退出事件（键盘任意键、鼠标任意点击、鼠标任意移动）
        self.root.bind("<Any-KeyPress>", self.myquit)
        self.root.bind("<Any-Button>", self.myquit)
        self.root.bind("<Motion>", self.myquit)

        # Canvas提供绘图功能(直线、椭圆、多边形等等)， 宽度和高度是屏幕分辨率大小
        self.canvas = Canvas(self.root, width = scrnw, height = scrnh)

        # 让画布按pack()布局
        self.canvas.pack()

        # 获取球的数量生成迭代器，每次迭代创建一个球
        for i in range(num):
        	# ball是SettingBalls()类对象，传入self.canvas画布，以及屏幕的宽高
            ball = SettingBalls(self.canvas, scrnwidth = scrnw, scrnheight = scrnh)

            # 调用 创建球的方法
            ball.create_ball()

            # 将生成的球对象放到 balls 列表里
            self.balls.append(ball)

        # 调用 run_ball()方法，启动小球运动
        self.run_ball()

        # 调用mainloop() 消息循环机制
        self.root.mainloop()

    def run_ball(self):
        for ball in self.balls:
            ball.move_ball()
        # run_ball 每隔20毫秒会被调用一次
        self.canvas.after(20, self.run_ball)

    # destroy() 是结束整个程序进程
    def myquit(self, event):
        self.root.destroy()

if __name__ == "__main__":
    ball = MoreBalls(20)

