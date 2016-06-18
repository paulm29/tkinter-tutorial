from tkinter import *
import time

root = Tk()

# ******* Creating a Status Bar for the Bottom *******

def updateStatus():
    status.config(text="yay!")

# bd is border, relief is type of border
status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.after(3000,updateStatus) # after 3 seconds update the status

root.mainloop()