from tkinter import *
from tkinter.ttk import *

def doNothing():
    print("This button currently does nothing. Make it do something you lazy bastard! Like she cared in the first place")

def New_Timetable():
    print("This will create a new timetable with clear values")

def Save_Timetable():
    print("This will save the current timetable")

def Load_Timetable():
    print("This will load a previously saved timetable")

def Reset_Timetable():
    print("This will clear the current timetable")

def Redo():
    print("This will redo the previous action")

def Undo():
    print("This will undo the previous action")

def Change_Timetable_Layout():
    print("This will allow the user to change how many subjects he has in a day, how long a period goes for, and when they have periods")

def Add_Subject():
    print("This will allow the user to allocate subjects to certain times, and it will allow them to colour code their subjects [Put colour into variable and have that variable be the same for all other subjects]")



mainWindow = Tk()

mainWindow.title("School Timetable")

mainWindow.geometry("850x450+250+100") # widthxheight+xposition+yposition

mainWindow.wm_iconbitmap('my_app.ico')

mainWindow.configure(background="#e6e6fa") # Change background colour

label_1 = Label(mainWindow, text="Name")
#Widgets are centered by default, sticky option to change

#Top Menu Open
menu = Menu(mainWindow)
mainWindow.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label="New Timetable...", command=New_Timetable)
fileMenu.add_command(label="Save Timetable...", command=Save_Timetable)
fileMenu.add_command(label="Load Timetable...", command=Load_Timetable)
fileMenu.add_separator()
fileMenu.add_command(label="Reset...", command=Reset_Timetable)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=mainWindow.destroy)

editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)

editMenu.add_command(label="Redo", command=Redo)
editMenu.add_command(label="Undo", command=Undo)
editMenu.add_separator()
editMenu.add_command(label="Change Timetable Layout...", command=Change_Timetable_Layout)
editMenu.add_command(label="Add Subject...", command=Add_Subject)
# Top Menu Close

# Right Side Stuff Open
addSubject = Button(mainWindow, text="Add Subject", command=Add_Subject)
addSubject.grid(column=5, row=1)

changeSubject = Button(mainWindow, text="Change Timetable", command=Change_Timetable_Layout)
changeSubject.grid(column=5, row=2)

currentSubject = Label(mainWindow, text='Current Subject')
currentSubject.grid(column=5, row=3)
# Right Side Stuff Close

#Timetable Open
innerGrid = Frame(mainWindow) #Makes a frame inside the grid - everything between this is the actual Timetable

firstDailysubject = Label(innerGrid, text="First Subject")
secondDailysubject = Label(innerGrid, text="Second Subject")
thirdDailysubject = Label(innerGrid, text="Third Subject")
fourthDailysubject = Label(innerGrid, text="Fourth Subject")
fifthDailysubject = Label(innerGrid, text="Fifth Subject")
sixthDailysubject = Label(innerGrid, text="Sixth Subject")

firstDailysubject.grid(column=0, row=1)
secondDailysubject.grid(column=0, row=2)
thirdDailysubject.grid(column=0, row=3)
fourthDailysubject.grid(column=0, row=4)
fifthDailysubject.grid(column=0, row=5)
sixthDailysubject.grid(column=0, row=6)


dayText = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
days = {}
n=1
for text in dayText:
    dayName = text.strip().lower()
    days[dayName] = Label(innerGrid, text=text)
    days[dayName].grid(column=n, row=1)
    n+=1

innerGrid.grid(row=2, column=2)
#Timetable Close

mainWindow.mainloop()