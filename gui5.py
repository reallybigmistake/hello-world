from tkinter import *


class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('Goodbye world...')
        self.quit()
class MyButton(HelloButton):
    def callback(self):
        print('ignoring...')
if __name__ == '__main__':
    MyButton(text='Hello subclass world').mainloop()
