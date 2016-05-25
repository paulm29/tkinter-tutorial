from tkinter import *
from tkinter import ttk

root = Tk()

notebook = ttk.Notebook(root)

def tabChangedEvent(event):
    print(event.widget.tab(event.widget.index("current"), "text"))

notebook.bind_all("<<NotebookTabChanged>>", tabChangedEvent)
notebook.pack()

tab1 = Frame(root, width=600, height=500)
notebook.add(tab1, text="select game's")

firstCheckbox = DoubleVar()
secondCheckbox = DoubleVar()
thirdCheckbox = DoubleVar()
fourthCheckbox = DoubleVar()

c1 = Checkbutton(tab1, text="call of duty", variable=firstCheckbox, onvalue=49.99, offvalue=0.00, height=1, width = 20)
c2 = Checkbutton(tab1, text="Halo 4", variable=secondCheckbox, onvalue=48.10, offvalue=0.00, height=1, width = 20)
c3 = Checkbutton(tab1, text="need for speed", variable=thirdCheckbox, onvalue=67.69, offvalue=0.00, height=1, width = 20)
c4 = Checkbutton(tab1, text="half life 3", variable=fourthCheckbox, onvalue=100.31, offvalue=0.00, height=1, width = 20)
c1.grid(row=0,column=0)
c2.grid(row=1,column=0)
c3.grid(row=2,column=0)
c4.grid(row=3,column=0)

totalLabel = Label(tab1,text="Total:")
totalLabel.grid(row=4,column=0)
totalEntry = Entry(tab1)
totalEntry.grid(row=5,column=0)

def print_total(event):
    total = firstCheckbox.get() + secondCheckbox.get() + thirdCheckbox.get() + fourthCheckbox.get()
    totalEntry.delete(0,END)
    totalEntry.insert(0,total)
    print(total)

button_1 = Button(tab1, text="Add Total")
# <Button-1> is an event that means "clicked left mouse button"
button_1.bind("<Button-1>",print_total)
button_1.grid(row=6,column=0)

tab1Next = Button(tab1, text="next")
tab1Next.grid(row=7,column=0)
# ====================================================================
# ====================================================================
# ====================================================================


tab2 = Frame(root, width=600, height=500)
notebook.add(tab2, text="delivery options")

tab2Label = Label(tab2,text="anwer the folowing so we can diliver the package to you")
tab2Label.grid(row=0,column=0)


countryLabel = Label(tab2,text="what country do you live in:")
countryLabel.grid(row=1,column=0)
countryLabel = Entry(tab2)
countryLabel.grid(row=2,column=0)


stateLabel = Label(tab2,text="what state do you live in:")
stateLabel.grid(row=3,column=0)
stateLabel = Entry(tab2)
stateLabel.grid(row=4,column=0)


cittyLabel = Label(tab2,text="what citty do you live in:")
cittyLabel.grid(row=5,column=0)
cittyLabel = Entry(tab2)
cittyLabel.grid(row=6,column=0)


adressLabel = Label(tab2,text="what is youre adress:")
adressLabel.grid(row=7,column=0)
adressLabel = Entry(tab2)
adressLabel.grid(row=8,column=0)

tab2Next = Button(tab2, text="next")
tab2Next.grid(row=9,column=0)
# ====================================================================
# ====================================================================
# ====================================================================

tab3 = Frame(root, width=600, height=500)
notebook.add(tab3, text="TAB 3")

tab3Label = Label(tab3,text="a label")
tab3Label.grid(row=0,column=0)

tab3Next = Button(tab3, text="next")
tab3Next.grid(row=1,column=0)
# ====================================================================
# ====================================================================
# ====================================================================


tab4 = Frame(root, width=500, height=400,)
notebook.add(tab4, text="TAB 4")

tab4Label = Label(tab4,text="a label")
tab4Label.grid(row=0,column=0)

def gotoTab2(event):
    notebook.select(1)
    root.update()

def gotoTab3(event):
    notebook.select(2)
    root.update()

def gotoTab4(event):
    notebook.select(3)
    root.update()

tab1Next.bind("<Button-1>",gotoTab2)
tab2Next.bind("<Button-1>",gotoTab3)
tab3Next.bind("<Button-1>",gotoTab4)

root.mainloop()