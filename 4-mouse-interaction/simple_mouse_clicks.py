from tkinter import *

def print_name(event):
    print("Hello my name is Vader.")
root = Tk()
button_1 = Button(root, text="Print Message")
# <Button-1> is an event that means "clicked left mouse button"
button_1.bind("<Button-1>", print_name)
button_1.pack()
root.mainloop()