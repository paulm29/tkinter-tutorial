from tkinter import *
root = Tk()

''' Create two special variables to store checkbox values '''
firstCheckbox = StringVar()
secondCheckbox= StringVar()

c1 = Checkbutton(root, text = "Star Wars", variable = firstCheckbox, onvalue = 'yes', offvalue = 'no', height=5, width = 20)
c2 = Checkbutton(root, text = "Star Trek", variable = secondCheckbox, onvalue = 'yes', offvalue = 'no', height=5, width = 20)

c1.grid(row=0,column=0)
c2.grid(row=1,column=0)

root.mainloop()