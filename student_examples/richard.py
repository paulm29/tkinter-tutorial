from tkinter import *
import winsound
import tkinter.messagebox

phonelist = []

def loadTimetable():
    with open("phonelist.txt") as f:
        for line in f:
            item = line.split(",")
            if len(item) == 1:
                continue
            name = item[0]
            if name == "name":
                continue
            phone = item[1]
            address = item[2]
            csd = item[3]
            phonelist.append(item)
            select.insert(END, name)
            print(name + " " + phone + " " + address + " " + csd)

def whichSelected():
    print("At %s of %d" % (select.curselection(), len(phonelist)))
    return int(select.curselection()[0])

def addEntry():
    phonelist.append([nameVar.get(), phoneVar.get(), addressVar.get(), csdVar.get()])
    setSelect()

def updateEntry():
    phonelist[whichSelected()] = [nameVar.get(), phoneVar.get(), addressVar.get(), csdVar.get()]
    setSelect()

def deleteEntry():
    del phonelist[whichSelected()]
    setSelect()

def saveEntry():
    with open("phonelist.txt","w") as file:
        file.write("name, phone, address, csd\n")
        for item in phonelist:
            print(item)
            #item = item.split(",")
            file.write(item[0] + "," + item[1] + "," + item[2] + "," + item[3])

def makeWindow():
    global nameVar, phoneVar, addressVar, csdVar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Name").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Phone").grid(row=1, column=0, sticky=W)
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Address").grid(row=2, column=0, sticky=W)
    addressVar = StringVar()
    address = Entry(frame1, textvariable=addressVar)
    address.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Current Symptoms & Diagnosis").grid(row=3, column=0, sticky=W)
    csdVar = StringVar()
    csd = Entry(frame1, textvariable=csdVar)
    csd.grid(row=3, column=1, sticky=W)

    frame2 = Frame(win)
    frame2.pack()
    b1 = Button(frame2, text=" Add  ", command=addEntry)
    b2 = Button(frame2, text="Update", command=updateEntry)
    b3 = Button(frame2, text="Delete", command=deleteEntry)
    b4 = Button(frame2, text=" Save ", command=saveEntry)
    b1.pack(side=LEFT);
    b2.pack(side=LEFT)
    b3.pack(side=LEFT);2
    b4.pack(side=LEFT)

    frame3 = Frame(win)
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)

    menu = Menu(win)
    win.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="Options", menu=subMenu)
    subMenu.add_command(label="Exit", command=win.destroy)

    loadTimetable()

    return win

win = makeWindow()

def setSelect():
    phonelist.sort()
    select.delete(0, END)
    for name, phone, address, csd in phonelist:
        select.insert(END, name)

def onselect(event):
    global select
    widget = event.widget

    if len(widget.curselection()) > 0:
        index = int(widget.curselection()[0])
        value = widget.get(index)
        print("selected: " + value)

        print(phonelist[index])
        nameVar.set(phonelist[index][0])
        phoneVar.set(phonelist[index][1])
        addressVar.set(phonelist[index][2])
        csdVar.set(phonelist[index][3])

select.bind('<<ListboxSelect>>', onselect)

win.title("Patient Record Keeper")
win.geometry("450x300+100+100")
win.wm_iconbitmap('my_app.ico')
win.configure(background="#FF00D1")

status = Label(win, text="Application Execution Complete", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

answer = tkinter.messagebox.askquestion('READ BEFORE USING', 'I will use this application responsibly and legally.')

if answer == 'no':
    win.destroy()

win.mainloop()
