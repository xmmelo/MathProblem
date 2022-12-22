from tkinter import * 
from Util.handler import *

def getRightFrame(root):
    frame=Frame(root,width=680,height=700, bg="dark gray")
    frame.pack(side = RIGHT)
    frame.pack_propagate(0)

    canvasFrame = Frame(root, width = 500, height = 500)
    canvas = Canvas(canvasFrame, bg="white", width = 500, height = 500)
    canvas.pack()
    canvasFrame.place(in_=frame, anchor="c", relx=.5, rely=.5)
    return canvas


def getLeftFrame(root, canvas):
    frame=Frame(root,width=680,height=700, bg="dark gray")
    frame.pack(side = LEFT)
    frame.pack_propagate(0)
    button1 = Button(frame, text='Hello', command=(lambda: handleTriangle(canvas)) )
    button1.pack(side=RIGHT)
    button2 = Button(frame, text='HelloQ', command=(lambda: handleQuadrilateral(canvas)))
    button2.pack(side=LEFT)


def start():
    root = Tk(  )
    canvas = getRightFrame(root)
    getLeftFrame(root, canvas)
    root.mainloop()

start()