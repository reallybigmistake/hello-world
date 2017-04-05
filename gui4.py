from tkinter import *

def greeting():
	print('Hello stdout world!...')


win = Frame()
win.pack()

Button(win, text='hello', command=greeting).pack(side=LEFT, anchor=NW)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='quit', command=win.quit).pack(side=RIGHT)
mainloop()