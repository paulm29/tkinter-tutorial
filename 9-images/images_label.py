from tkinter import *

root = Tk()

photo = PhotoImage(file="save.png")
label = Label(root, image=photo)
label.grid(row=0,column=0)

'''
# pack version
photo = PhotoImage(file="python_logo.png")
label = Label(root, image=photo)
label.pack()
'''

root.mainloop()