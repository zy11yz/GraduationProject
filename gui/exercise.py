from tkinter import *

def callback():
    frame1.destroy()
    frame2.pack()
root = Tk()
frame1 = Frame(root, bg='red', width=100, height=100)
frame2 = Frame(root, bg='yellow', width=100, height=100)
b = Button(root, text='切换', command=callback)

frame1.pack()
b.pack(side=BOTTOM)
mainloop()
