from tkinter import *


class HelloPackage:
    def __init__(self, parent=None):
        self.top = Frame(parent)
        self.top.pack()
        self.makeWidget()
        self.data = 0

    def __getattr__(self, name):
        return getattr(self.top, name)

    def makeWidget(self):
        Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)

    def message(self):
        self.data += 1
        print('Hello number', self.data)


if __name__ == '__main__':
    frm = Frame()
    frm.pack()
    Label(frm, text='hello').pack()
    part = HelloPackage(frm)
    part.pack(side=RIGHT)  # FAILS!--need part.top.pack(side=RIGHT)
    frm.mainloop()
