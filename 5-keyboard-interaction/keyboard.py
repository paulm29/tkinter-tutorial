from tkinter import *
from math import *
def calculate(event):
    ''' Don't worry if you don't get this code now! '''
    answer.configure(text = "Answer: " + str(eval(entry.get())))
root = Tk()
Label(root, text="Your Expression:").pack() # this is a shortcut for creating a label
entry = Entry(root)
entry.bind("<Return>", calculate)
entry.pack()
answer = Label(root)
answer.pack()
root.mainloop()