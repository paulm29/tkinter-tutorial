from tkinter import *
from tkinter import ttk

root = Tk()

notebook = ttk.Notebook(root)

def tabChangedEvent(event):
    print(event.widget.tab(event.widget.index("current"), "text"))

notebook.bind_all("<<NotebookTabChanged>>", tabChangedEvent)
notebook.pack()

tab1 = Frame(root, width=400, height=300)
notebook.add(tab1, text="TAB 1")

firstCheckbox = DoubleVar()
secondCheckbox = DoubleVar()
thirdCheckbox = DoubleVar()
fourthCheckbox = DoubleVar()

c1 = Checkbutton(tab1, text="call of duty", variable=firstCheckbox, onvalue=49.00, offvalue=0.00, height=1, width = 20)
c2 = Checkbutton(tab1, text="Halo 4", variable=secondCheckbox, onvalue=47.49, offvalue=0.00, height=1, width = 20)
c3 = Checkbutton(tab1, text="need for speed", variable=thirdCheckbox, onvalue=66.96, offvalue=0.00, height=1, width = 20)
c4 = Checkbutton(tab1, text="half life 3", variable=fourthCheckbox, onvalue=100.00, offvalue=0.00, height=1, width = 20)
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
button_1.bind("<Button-1>", print_total)
button_1.grid(row=6,column=0)

# ====================================================================

tab2 = Frame(root, width=400, height=300)
notebook.add(tab2, text="TAB 2")

tab2Label = Label(tab2,text="a label")
tab2Label.grid(row=0,column=0)

# ====================================================================

tab3 = Frame(root, width=400, height=300)
notebook.add(tab3, text="TAB 3")

tab3Label = Label(tab3,text="a label")
tab3Label.grid(row=0,column=0)


root.mainloop()