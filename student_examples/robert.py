from tkinter import *
import tkinter.messagebox
import winsound

root = Tk()

root.title("My awesome App")
root.geometry("700x610+100+100")
root.wm_iconbitmap('my_app.ico')
root.configure(background="#e6e6fa")

menu = Menu(root)
root.config(menu=menu)
root.option_add("*tearOff", False)
subMenu = Menu(menu)
# Adds a drop down when "File" is clicked
menu.add_cascade(label="File", menu=subMenu)

def exitWithSound():
    saveTimeTable()
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    root.destroy()

subMenu.add_command(label="Exit", command=exitWithSound)

toolbar = Frame(root, bg="blue", width=300)
insertButt = Button(toolbar, text="Exit", command=exitWithSound, anchor=W)
insertButt.grid(row=0, column=0, padx=2, pady=2)
toolbar.grid(row=0, column=0)

periodLabel = Label(root, text="Period")
MondayLabel = Label(root, text="Monday")
TuesdayLabel = Label(root, text="Tuesday")
WednesdayLabel = Label(root, text="Wednesday")
ThursdayLabel = Label(root, text="Thursday")
FridayLabel = Label(root, text="Friday")

r = 0

#periodLabel.grid(row=r, column=0)
MondayLabel.grid(row=r, column=1)
TuesdayLabel.grid(row=r, column=2)
WednesdayLabel.grid(row=r, column=3)
ThursdayLabel.grid(row=r, column=4)
FridayLabel.grid(row=r, column=5)

r += 1
period1 = Label(root, text="Period 1")
period1.grid(row=r, column=0)
r += 1
period2 = Label(root, text="Period 2")
period2.grid(row=r, column=0)
r += 1
period3 = Label(root, text="Period 3")
period3.grid(row=r, column=0)
r += 1
period4 = Label(root, text="Period 4")
period4.grid(row=r, column=0)
r += 1
period5 = Label(root, text="Period 5")
period5.grid(row=r, column=0)
r += 1
period6 = Label(root, text="Period 6")
period6.grid(row=r, column=0)

r = 1
scrollbar11 = Scrollbar(root)
scrollbar11.grid(row=r, column=1, sticky=E)
list11 = Listbox(root, height=2, exportselection=0, yscrollcommand=scrollbar11.set)
list11.grid(row=r, column=1)
scrollbar11.config(command=list11.yview)

list12 = Listbox(root, height=2, exportselection=0)
list12.grid(row=r, column=2)

list13 = Listbox(root, height=2, exportselection=0)
list13.grid(row=r, column=3)

list14 = Listbox(root, height=2, exportselection=0)
list14.grid(row=r, column=4)

list15 = Listbox(root, height=2, exportselection=0)
list15.grid(row=r, column=5)

r += 1
list21 = Listbox(root, height=2, exportselection=0)
list21.grid(row=r, column=1)

list22 = Listbox(root, height=2, exportselection=0)
list22.grid(row=r, column=2)

list23 = Listbox(root, height=2, exportselection=0)
list23.grid(row=r, column=3)

list24 = Listbox(root, height=2, exportselection=0)
list24.grid(row=r, column=4)

list25 = Listbox(root, height=2, exportselection=0)
list25.grid(row=r, column=5)

r += 1
list31 = Listbox(root, height=2, exportselection=0)
list31.grid(row=r, column=1)

list32 = Listbox(root, height=2, exportselection=0)
list32.grid(row=r, column=2)

list33 = Listbox(root, height=2, exportselection=0)
list33.grid(row=r, column=3)

list34 = Listbox(root, height=2, exportselection=0)
list34.grid(row=r, column=4)

list35 = Listbox(root, height=2, exportselection=0)
list35.grid(row=r, column=5)

r += 1
list41 = Listbox(root, height=2, exportselection=0)
list41.grid(row=r, column=1)

list42 = Listbox(root, height=2, exportselection=0)
list42.grid(row=r, column=2)

list43 = Listbox(root, height=2, exportselection=0)
list43.grid(row=r, column=3)

list44 = Listbox(root, height=2, exportselection=0)
list44.grid(row=r, column=4)

list45 = Listbox(root, height=2, exportselection=0)
list45.grid(row=r, column=5)

r += 1
list51 = Listbox(root, height=2, exportselection=0)
list51.grid(row=r, column=1)

list52 = Listbox(root, height=2, exportselection=0)
list52.grid(row=r, column=2)

list53 = Listbox(root, height=2, exportselection=0)
list53.grid(row=r, column=3)

list54 = Listbox(root, height=2, exportselection=0)
list54.grid(row=r, column=4)

list55 = Listbox(root, height=2, exportselection=0)
list55.grid(row=r, column=5)

r += 1
list61 = Listbox(root, height=2, exportselection=0)
list61.grid(row=r, column=1)

list62 = Listbox(root, height=2, exportselection=0)
list62.grid(row=r, column=2)

list63 = Listbox(root, height=2, exportselection=0)
list63.grid(row=r, column=3)

list64 = Listbox(root, height=2, exportselection=0)
list64.grid(row=r, column=4)

list65 = Listbox(root, height=2, exportselection=0)
list65.grid(row=r, column=5)

selectedForEdit = None

def onselect(event):
    global selectedForEdit
    widget = event.widget

    if len(widget.curselection()) > 0:
       # print("selected: " + widget.curselection())
        index = int(widget.curselection()[0])
        value = widget.get(index)
        editEntry.delete(0,END)
        editEntry.insert(0,value)
        selectedForEdit = widget

for period in range(1, 7):
    for day in range(1, 6):
        p = str(period)
        d = str(day)
        listbox = globals()["list" + p + d]
        listbox.bind('<<ListboxSelect>>', onselect)

'''-----------------------------------------------------------------------------------------
END Listboxes
-----------------------------------------------------------------------------------------'''


r = 7

DayLabel = Label(root, text="Day")
DayLabel.grid(row=r, column=0)

listDay = Listbox(root, height=5, exportselection=0)
listDay.grid(row=r, column=1)

listDay.insert(END, "Monday")
listDay.insert(END, "Tuesday")
listDay.insert(END, "Wednesday")
listDay.insert(END, "Thursday")
listDay.insert(END, "Friday")

r += 1

periodLabel = Label(root, text="Period")
periodLabel.grid(row=r, column=0)

listPeriod = Listbox(root, height=6, exportselection=0)
listPeriod.grid(row=r, column=1)

listPeriod.insert(END, "1")
listPeriod.insert(END, "2")
listPeriod.insert(END, "3")
listPeriod.insert(END, "4")
listPeriod.insert(END, "5")
listPeriod.insert(END, "6")

r += 1

detailLabel = Label(root, text="Details:")
detailLabel.grid(row=r, column=0)

detailEntry = Entry(root)
detailEntry.grid(row=r, column=1)

detailEntry.insert(END, "Room 7 - DIO")

r += 1

submitButton = Button(root, width=15,text="Add to Timetable")
submitButton.grid(row=r, column=1)

def isPeriodSelected():
    return len(listDay.curselection()) == 0

def isDaySelected():
    return len(listPeriod.curselection()) == 0

def addToTimetable(event):
    if isDaySelected():
        tkinter.messagebox.showinfo("Oops", "You must select a day")
        return
    if isDaySelected():
        tkinter.messagebox.showinfo("Oops", "You must select a period")
        return
    print(listDay.curselection()[0])
    print(listPeriod.curselection()[0])
    day = str(listDay.curselection()[0] + 1)
    period = str(listPeriod.curselection()[0] + 1)
    addList = globals()["list"+period+day]
    addList.insert(END,detailEntry.get())

submitButton.bind("<ButtonRelease-1>", addToTimetable)

editFrame = Frame(root)
editFrame.grid(row=7,column=2)

editEntry = Entry(editFrame)
editEntry.grid(row=0,column=0)

def editDetail(event):
    if selectedForEdit is None:
        print("nothing selected")
    else:
        index = selectedForEdit.curselection()[0]
        selectedForEdit.delete(index)
        selectedForEdit.insert(0,editEntry.get())

editButton = Button(editFrame, width=10, text="Edit")
editButton.grid(row=1, column=0)
editButton.bind("<ButtonRelease-1>", editDetail)

def deleteFromTimetable(event):
    answer = tkinter.messagebox.askokcancel('Warning!','Delete selected items?')
    if answer == True:
        for period in range(1, 7):
            for day in range(1, 6):
                p = str(period)
                d = str(day)
                selected = globals()["list"+p+d].curselection()
                if selected:
                    globals()["list"+p+d].delete(selected)


deleteButton = Button(editFrame, width=10, text="Delete")
deleteButton.grid(row=2, column=0)
deleteButton.bind("<ButtonRelease-1>", deleteFromTimetable)

photo = PhotoImage(file="python_logo.png")
shrunk = photo.subsample(5,5)
imageLabel = Label(root, image=shrunk)
imageLabel.grid(row=11, column = 3)


status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W, width=100)
status.grid(row=12, column=0, columnspan=7)

def loadTimetable():
    with open("timetable.txt") as f:
        for line in f:
            item = line.split(",")
            if len(item) == 1: # may be '\n'
                continue
            print(item)
            period = item[0]
            if period == "period":
                continue
            day = item[1]
            detail = item[2]
            listbox = globals()["list" + period + day]
            listbox.insert(END,detail)
            print(period + " " + day + " " + detail)

def saveTimeTable():
    f = open("timetable.txt", "w")

    for period in range(1, 7):
        for day in range(1, 6):
            p = str(period)
            d = str(day)
            listbox = globals()["list" + p + d]
            # for each item in the listbox, write to file
            for i, listbox_entry in enumerate(listbox.get(0, END)):
                print(listbox_entry)
                f.write(str(period) + "," + str(day) + "," + listbox_entry + "\n")
    f.close()

root.after(1000,loadTimetable)

root.mainloop()
