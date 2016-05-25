from tkinter import *

def left_click(event):
    print("Left")

def middle_click(event):
    print("Middle")

def right_click(event):
    print("Right")
root = Tk()
frame = Frame(root, width=300, height=200)
# Event is something the user does to the widget, function that gets called
frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click) # scroll wheel
frame.bind("<Button-3>", right_click)
frame.pack()
root.mainloop()