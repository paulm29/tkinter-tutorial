from tkinter import *


def doNothing():
    print("ok ok I won't...")

root = Tk()

root.option_add('*tearOff',False)  # hide the dotted line below the window

# Tkinter puts menus at the top by default
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
# Adds a drop down when "File" is clicked
menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()