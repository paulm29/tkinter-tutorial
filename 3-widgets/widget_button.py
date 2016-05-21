from tkinter import *

root = Tk()

def sayHello():
   print("hello")

myButton = Button(root, text="Hello", command=sayHello)
myButton.grid(row=0,column=0)

root.mainloop()