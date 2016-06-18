from tkinter import *

import os
root = Tk()
root.title('Audio Player')
canvas = Canvas(bg='black',height = 600, width = 800)

def sound1():
    os.system("X.wav")
    
var = IntVar()
rb1 = Radiobutton(root,text="Play Audio 1",variable=var,value=1,command=sound1)
rb1.pack(anchor=W)
canvas.pack()
root.mainloop()