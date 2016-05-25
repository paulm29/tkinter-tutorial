from tkinter import *  #import all the tkinter classes so that we can use them
from tkinter import ttk

win = Tk()  # create a blank window called root
win.title("Video Rental Application")
win.geometry("640x480+100+100")  # width x height + x position + y position
#win.wm_iconbitmap('Video Rental.ico')
win.configure(background="#e5e5e5")  #A Shade of Grey

root = Frame(win,width=400)
root.pack(fill=BOTH,expand=TRUE)

def SAVE():
    print("Working")



label_1 = Label(root, text="Date Rented", background="#e5e5e5")
label_2 = Label(root, text="Date Due", background="#e5e5e5")
label_3 = Label(root, text="Select Video", background="#e5e5e5")
label_4 = Label(root, text="Available Copies", background="#e5e5e5")
label_5 = Label(root, text="OverDue", background="#e5e5e5")
label_6 = Label(root, text="Total Amount", background="#e5e5e5")
label_10 = Label(root, text="                    ", background="#e5e5e5")
label_11 = Label(root, text="                    ", background="#e5e5e5")
label_12 = Label(root, text="Name", background="#e5e5e5")
label_13 = Label(root, text="Address", background="#e5e5e5")
label_14 = Label(root, text="Phone Number", background="#e5e5e5")
label_15 = Label(root, text="Customer ID", background="#e5e5e5")
label_16 = Label(root, text="Member", background="#e5e5e5")

entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_4 = Entry(root)
entry_5 = Entry(root)
entry_6 = Entry(root)

# widgets centered by default, sticky option to change
label_1.grid(row=2, column=1, sticky=W) # E is for east or right alignment
label_2.grid(row=4, column=1, sticky=W)
label_3.grid(row=0, column=1, sticky=W)
label_4.grid(row=6, column=1, sticky=W)
label_5.grid(row=8, column=1, sticky=W)
label_6.grid(row=9, column=1, sticky=W)
label_10.grid(row=0, column=2, sticky=W)
label_11.grid(row=0, column=4, sticky=W)
label_12.grid(row=0, column=3, sticky=W)
label_13.grid(row=2, column=3, sticky=W)
label_14.grid(row=4, column=3, sticky=W)
label_15.grid(row=6, column=3, sticky=W)
label_16.grid(row=8, column=3, sticky=W)
entry_1.grid(row=3, column=1)
entry_2.grid(row=5, column=1)
entry_3.grid(row=1, column=3)
entry_4.grid(row=3, column=3)
entry_5.grid(row=5, column=3)
entry_6.grid(row=7, column=3)

c1 = Checkbutton(root)
c1.grid(row=8, column=1)

c2 = Checkbutton(root)
c2.grid(row=8, column=3)

def printValue(event):
    print(value.get())
value = StringVar()
box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
box.bind('<<ComboboxSelected>>',printValue) #when a value is selected, call printValue()
box.current(0)
box.grid(row=7, column=1, sticky=W)

def printValue(event):
    print(value.get())
value = StringVar()
box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('Mad Max: Fury Road', 'The Hateful Eight', 'The Revenant', 'Deadpool')
box.bind('<<ComboboxSelected>>',printValue) #when a value is selected, call printValue()
box.current(0)
box.grid(row=1, column=1)

# Tkinter puts menus at the top by default


button = Button(root, text="Save", command=SAVE, background="#e5e5e5")
button.grid(row=1, column=5, sticky=E)

button = Button(root, text="Exit", command=root.destroy, background="#e5e5e5")
button.grid(row=3, column=5, sticky=E)



#exitWithSound

def updateStatus():
    status.config(text="......Saved......")

# bd is border, relief is type of border

statusFrame = Frame(win)
statusFrame.pack(fill=X)

status = Label(statusFrame, text="......Idle......", bd=1, relief=SUNKEN, anchor=W)
status.pack(fill=X,expand=True,side=LEFT)

root.after(3000,updateStatus) # after 3 seconds update the status

menu = Menu(win)
win.config(menu=menu)
win.option_add("*tearOff", False)
subMenu = Menu(menu)
# Adds a drop down when "File" is clicked
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Save...", command=SAVE)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=win.destroy)

win.mainloop()  # make the program run forever