from tkinter import *

root = Tk()

photo = PhotoImage(file="save.png")
button = Button(root, image=photo)
button.grid(row=0,column=0)

'''
# pack version
photo = PhotoImage(file="save.png")
button = Button(root, image=photo)
button.pack()
'''

root.mainloop()