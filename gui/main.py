from tkinter import *
import os
import gui.analysis
path = "..\\pic"
os.chdir(path)


def analysis(root, info):
    if 'df.csv' in os.listdir('..\\file'):
        root.destroy()
        gui.analysis.analysis()
    else:
        print(os.listdir('..\\file'))
        info['text'] = '请先执行抓取数据'


def mainfuc():
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
    label_1 = Label(frame1, text='Web页面抓取与分析工具', font='YaHei 16', height=3)
    button_crwl = Button(frame2, text='抓取数据', width=10, height=4)
    button_anal = Button(frame2, text='分析数据', width=10, height=4, command=lambda: analysis(root, info))
    ver_l = Label(root, text='版本 v1.0beta', bd=0, relief=SUNKEN, anchor=W)
    info = Label(root, font='Yahei 10')

    # 界面布局设计
    frame1.pack()
    frame2.pack()
    label_1.pack()
    button_crwl.grid(row=0, column=0, padx=1.5)
    button_anal.grid(row=0, column=1, padx=1.5)
    ver_l.pack(side=BOTTOM, fill=X)
    info.pack(side=BOTTOM, fill=BOTH)

    root.title('Web页面抓取与分析工具')
    root.iconbitmap('z.ico')
    mainloop()


if __name__ == '__main__':
    mainfuc()
