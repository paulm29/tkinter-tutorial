from tkinter import *
root = Tk()

breakfast = StringVar()
r1 = Radiobutton(root, text = "SPAM", variable = breakfast, value = 'SPAM')
r2 = Radiobutton(root, text = "Eggs", variable = breakfast, value = 'Eggs')
r3 = Radiobutton(root, text = "Sausage", variable = breakfast, value = 'Sausage')
r4 = Radiobutton(root, text = "Iggy", variable = breakfast, value = 'Iggy')
breakfast.set(None) # have to set so that not all are selected on Windows

r1.grid(row=0,column=0)
r2.grid(row=1,column=0)
r3.grid(row=2,column=0)
r4.grid(row=3,column=0)

def getradio():
    print(breakfast.get())

b1 = Button(root,text="Press me",command=getradio)
b1.grid(row=5,column=0)

root.mainloop()