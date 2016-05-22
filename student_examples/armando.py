from tkinter import *
root = Tk()

def focusin(event):
    myEntry.select_range(0,END)

myEntry = Entry(root)
myEntry.insert(0,"Oscar is a hag")
myEntry.bind("<FocusIn>",focusin)
myEntry.grid()

root.mainloop()