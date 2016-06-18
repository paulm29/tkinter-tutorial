from tkinter import *

root = Tk()

#IMAGE CODE
photo = PhotoImage(file="harold2.png")
label = Label(root, image=photo)
label.grid(row=11,column=15)
label.grid_remove() # hide the image

def hideThePainHarold():
    label.grid() # show the image


#Again i would love if i could fit this code into the menu code.
# MENU CODE
menu = Menu(root)
root.config(menu=menu)
root.option_add("*tearOff", False)
subMenu1 = Menu(menu)
subMenu2 = Menu(menu)
subMenu3 = Menu(menu)
menu.add_cascade(label="File", menu=subMenu1)
subMenu1.add_command(label="Exit?", command=root.destroy)
menu.add_cascade(label="Images.exe", menu=subMenu2)
subMenu2.add_command(label="HIDE THE PAIN HAROLD", command=hideThePainHarold)
menu.add_cascade(label="YEE", menu=subMenu3)
subMenu3.add_command(label="Yeebusters", command=root.destroy)

root.mainloop()