import mysql.connector
import os
from tkinter import *
import gui.main
conn = mysql.connector.connect(user='root', password='1211', host='localhost', database='data_analysis', port=3306)
cursor = conn.cursor()
path = "..\\pic"
os.chdir(path)


# 回调函数设计
def callback():
    sql1 = "select password from user_info where name = '%s'" % e1.get()
    cursor.execute(sql1)
    try:
        password = cursor.fetchall()[0][0]
        if e2.get() == password:
            sql2 = "select level from user_info where name = '%s'" % e1.get()
            cursor.execute(sql2)
            level = cursor.fetchall()[0][0]
            if level > 0:
                root.destroy()
                gui.main.mainfuc()
            else:
                info['text'] = '没有权限'
        else:
            info['text'] = '用户名或密码错误'
    except:
        info['text'] = '用户名或密码错误'


def key(event):
    print('a')
    if event.keycode == 13:
        print(event.keycode)
        callback()

# 界面框架
root = Tk()
root.geometry('350x250')
frame1 = Frame(root)
frame2 = Frame(root)

# Widget设计
label_1 = Label(frame1, text='Web页面抓取与分析工具', font='YaHei 16', height=3)
user_l = Label(frame2, text='用户名:')
pw_l = Label(frame2, text='密码:')
e1 = Entry(frame2, width=12,)
e2 = Entry(frame2, width=12,  show="*")
subm = Button(frame2, text='登陆', width=10, bd=1, command=callback)
ver_l = Label(root, text='版本 v1.0beta', bd=0, relief=SUNKEN, anchor=W)
info = Label(root, font='Yahei 10')

# 界面布局设计
frame1.bind('<Key>', key)
frame1.pack()
frame2.pack()
label_1.pack()
user_l.grid(row=1, column=1, sticky=W)
pw_l.grid(row=2, column=1, sticky=W, pady=5)
e1.grid(row=1, column=2)
e2.grid(row=2, column=2, pady=5)
subm.grid(row=3, column=2, pady=10)
ver_l.pack(side=BOTTOM, fill=X)
info.pack(side=BOTTOM, fill=BOTH)

root.title('Web页面抓取与分析工具')
root.iconbitmap('z.ico')
mainloop()
