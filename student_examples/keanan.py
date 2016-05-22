from tkinter import *
from tkinter import ttk
root = Tk()

root.title("MealMasters Meal Planner")
root.geometry("450x300+100+100")
#root.wm_iconbitmap('MM.ico')
root.configure(background="#e6e6fa")
label_1 = Label(root, text="Choose one of our fresh meals!")
def printValue(event):
    print(value.get())
    print(box.current())

value = StringVar()
box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('A', 'B', 'C')
box.bind('<<ComboboxSelected>>',printValue) #when a value is selected, call printValue()
box.current(0)
box.grid(column=0, row=0)
root.mainloop()