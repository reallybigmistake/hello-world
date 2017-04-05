from tkinter import *
import sys
import os
import _thread


def loadCalc():
    os.system('calc')


def cmd():
    _thread.start_new_thread(loadCalc, ())


def handler():
    funcs = []
    for i in 'abcdef':
        def fun(i=i):
            return i
        funcs.append(fun)
    return funcs


for fun in handler():
    print(fun())


root = Tk()
widget = Button(root, text='hello', command=cmd)
widget.pack(side=LEFT, expand=YES, fill=X)
root.title('button')
root.mainloop()
