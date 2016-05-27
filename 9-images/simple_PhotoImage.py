from tkinter import *

root = Tk()

# Labels
photo = PhotoImage(file="save.png")
label = Label(root, image=photo)
label.grid(row=0,column=0)

'''
# pack version
photo = PhotoImage(file="python_logo.png")
label = Label(root, image=photo)
label.pack()
'''

# Buttons
photo2 = PhotoImage(file="save.png")
button = Button(root, image=photo2)
button.grid(row=1,column=0)

'''
# pack version
photo = PhotoImage(file="save.png")
button = Button(root, image=photo)
button.pack()
'''

root.mainloop()