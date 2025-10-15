from tkinter import *
from tkinter.colorchooser import askcolor


class Paintset(object):
    DEFAULTPENSIZE = 5.0
    DEFAULTPENCOLOR = "black"
    def __init__(self):
        self.root = Tk()
        self.penbutton = Button(self.root, text="Pen", command=self.usepen)
        self.penbutton.grid(row=0, column=0)
        self.brushbutton = Button(self.root, text="Brush", command=self.usebrush)
        self.brushbutton.grid(row=0, column=1)
        self.color = Button(self.root, text="Color", command=self.usecolor)
        self.color.grid(row=0, column=2)
        self.eraser = Button(self.root, text="Eraser", command=self.useeraser)
        self.eraser.grid(row=0, column=3)
        self.pensize = Scale(self.root, from_=1, to=10, orient=VERTICAL)
        self.pensize.grid(row=0, column=4)
        
        self.canvas = Canvas(self.root, bg="white", width = 500, height = 500)
        self.canvas.grid(row=1, columnspan=5)
        self.root.mainloop()
    
    def usepen(self):
        self.activatebutton(self.penbutton)
    def usebrush(self):
        self.activatebutton(self.brushbutton)
    def usecolor(self):
        self.eraseron=False
        self.color=askcolor(color=self.color) [1]
        print(askcolor (color=self.color))
    def useeraser(self):
        self.activatebutton(self.eraserbutton, erasermode=True)
    def pensize(self):
        pass
    
Paintset()