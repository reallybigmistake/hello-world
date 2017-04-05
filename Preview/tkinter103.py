from tkinter import *
from tkinter.messagebox import showinfo
'''
def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')
top.iconbitmap('sexy_girl.ico')

Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
#btn = Button(top, text='Submit', command=reply(ent.get()))
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

top.mainloop()
'''
def reply():
    global ent
    name = ent.get()
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')
top.iconbitmap('sexy_girl.ico')

Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=reply)
btn.pack(side=LEFT)

top.mainloop()
