from tkinter import *
import sys
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.master)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向fm1中添加3个按钮
        # 设置按钮从顶部开始排列，且按钮只能在垂直（X）方向填充
        Label(fm1, text='Please Enter your Path:').pack(side=TOP, fill=X, expand=YES)
        Label(fm1, text='Please Enter your Pwd:').pack(side=TOP, fill=X, expand=YES)
        Label(fm1, text='      ').pack(side=TOP,  fill=X, expand=YES)
        # 创建第二个容器
        fm2 = Frame(self.master)
        # 该容器放在左边排列，就会挨着fm1
        fm2.pack(side=LEFT, padx=10, expand=YES)
        # 向fm2中添加3个按钮
        # 设置按钮从右边开始排列
        Entry(fm2).pack(side=TOP, fill=Y, expand=YES)
        Entry(fm2).pack(side=TOP, fill=Y, expand=YES,pady=5)
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)
        # 创建第三个容器
        fm3 = Frame(self.master)
        # 该容器放在右边排列，就会挨着fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        # 向fm3中添加3个按钮
        # 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向填充
        Button(fm3, text='E x i t', command=sys.exit).pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES)
        #fm4 = Frame(self.master)
        #fm4.pack(side=BOTTOM, fill=BOTH, expand=YES)
        #Text(fm4).pack(side=BOTTOM, fill=Y, expand=YES)
root = Tk()
root.title("Pack布局")
display = App(root)
root.mainloop()