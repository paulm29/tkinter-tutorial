#  Main Set-up For Program

from tkinter import *  # import all the tkinter classes so that we can use them

root = Tk()  # create a blank window called root
root.title("BRAIN GAME")
root.geometry("400x400+100+100")  # width x height + x position + y position
root.configure(background="#e6e6fa")  # lavender

toolbarFrame = Frame(root,bd=5,relief=RAISED)  # create a frame for the sections
toolbarFrame.pack(fill=X,side=TOP)

#  frame for body
bodyFrame = Frame(root, bd=5, relief=RAISED)
bodyFrame.pack(fill=X,side=TOP)
bottomFrame = Frame(root, bd=5, relief=RAISED)
bottomFrame.pack(fill=BOTH,expand=True, side=BOTTOM)

photo = PhotoImage(file="save.png")

#  creates commands for mouse clicks

def about_click(event):
    print("About pressed")
def about_outcome(event):
    button_1 = Button(root, text="Print Message")
    button_1.pack()
#  hint button click program
#  changes the label
def hint_click(event):
    print("Hint pressed")
def hint_outcome(event):
    button_1 = Button(root, text="Print Message")
    button_1.pack()
#  home button click program
#  changes the label
#def home_click(event):
#    print("Home pressed")

def home_outcome(event):
    print("home_outcome")
    photoLabel_home = Label(bodyFrame,image=photo)
    photoLabel_home.pack()
    button_1 = Button(bottomFrame, text="Print Message",anchor='center')
    button_1.pack(anchor='center')

def start_click(event):
    print("Start pressed")
def start_outcome(event):
    button_1 = Button(bodyFrame, bd=20, text="Print Message", fg="red", bg="red")
    button_1.pack()
'''
#  level button click program
#  changes the label
def level_click(event):
    print("Level pressed")
def level_outcome(event):
    button_1 = Button(root, text="Print Message")
    button_1.pack()
'''
# Creates buttons on the window
home = Button(toolbarFrame, text="Home", fg="yellow", bg= "green")
level = Button(toolbarFrame, text="Topic", fg="green", bg= "yellow")
hint = Button(toolbarFrame, text="Hint", fg="yellow", bg= "green")
about = Button(toolbarFrame, text="ABOUT", fg="yellow", bg= "green")
start = Button(bodyFrame, text='Start Button', fg="white", bg="red")
about.bind("<Button-1>", about_click)  # <Button-1> is an event that means "clicked left mouse button"
home.bind("<Button-1>", home_outcome)  # <Button-1> is an event that means "clicked left mouse button"
start.bind("<Button-1>", start_click)  # <Button-1> is an event that means "clicked left mouse button"
'''
level.bind("<Button-1>", level_click)  # <Button-1> is an event that means "clicked left mouse button"
level.pack(side=LEFT)
'''
home.pack(side=LEFT)
hint.pack(side=RIGHT)
about.pack(side=RIGHT)
start.pack()

root.mainloop()
