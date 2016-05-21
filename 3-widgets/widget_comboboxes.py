from tkinter import *
from tkinter import ttk

root = Tk()

def printValue(event):
    print(value.get())
    print(box.current())

value = StringVar()
box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('A', 'B', 'C')
box.bind('<<ComboboxSelected>>',printValue) #when a value is selected, call printValue()
box.current(0)
box.grid(column=0, row=0)

# add more values, have to convert tuple to list first
newList = list(box['values']) # get values of combobox as a list
newList.append("D") # add D to the end
box['values'] = newList

root.mainloop()