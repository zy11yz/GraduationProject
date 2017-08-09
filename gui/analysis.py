from tkinter import *
import os
from analysis_ import time_analysis, artical_analysis, act_analysis, sourece_analysis, emotion_analysis, world_cloud, word_count, logistics
path = "..\\pic"
os.chdir(path)


def analysis():
    # 界面框架
    root = Tk()
    root.geometry('350x250')
    frame1 = Frame(root)
    frame2 = Frame(root)
    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open..')
    filemenu.add_separator()
    filemenu.add_command(label='Exit')

    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About..', command=callable)

    # Widget设计
    label_1 = Label(frame1, text='数据分析', font='YaHei 16', height=3)
    la = Button(frame2, text='时间分析', width=8, height=3, command=lambda: time_analysis.time_anls())
    lb = Button(frame2, text='来源分析', width=8, height=3, command=lambda: sourece_analysis.src_anal())
    lc = Button(frame2, text='文章分析', width=8, height=3, command=lambda: print(artical_analysis.artical_anls()))
    ld = Button(frame2, text='行为分析', width=8, height=3, command=lambda: act_analysis.act_anls())
    le = Button(frame2, text='词频分析', width=8, height=3,)
    lf = Button(frame2, text='词云生成', width=8, height=3,)
    lg = Button(frame2, text='回归评价', width=8, height=3,)
    lh = Button(frame2, text='情感判断', width=8, height=3,)
    ver_l = Label(root, text='版本 v1.0beta', bd=0, relief=SUNKEN, anchor=W)
    info = Label(root, font='Yahei 10')

    # 界面布局设计
    frame1.pack()
    frame2.pack()
    label_1.pack()
    la.grid(row=0, column=0, padx=1, pady=1)
    lb.grid(row=0, column=1, padx=1, pady=1)
    lc.grid(row=0, column=2, padx=1, pady=1)
    ld.grid(row=0, column=3, padx=1, pady=1)
    le.grid(row=1, column=0, padx=1, pady=1)
    lf.grid(row=1, column=1, padx=1, pady=1)
    lg.grid(row=1, column=2, padx=1, pady=1)
    lh.grid(row=1, column=3, padx=1, pady=1)
    ver_l.pack(side=BOTTOM, fill=X)
    info.pack(side=BOTTOM, fill=BOTH)

    root.title('Web页面抓取与分析工具')
    root.iconbitmap('z.ico')
    mainloop()

if __name__ == '__main__':
    analysis()
