from tkinter import *
root = Tk()

firstCheckbox = DoubleVar()
secondCheckbox = DoubleVar()
thirdCheckbox = DoubleVar()
fourthCheckbox = DoubleVar()

c1 = Checkbutton(root, text="call of duty", variable=firstCheckbox, onvalue=49.00, offvalue=0.00)
c2 = Checkbutton(root, text="Halo 4", variable=secondCheckbox, onvalue=47.49, offvalue=0.00)
c3 = Checkbutton(root, text="need for speed", variable=thirdCheckbox, onvalue=66.96, offvalue=0.00)
c4 = Checkbutton(root, text="half life 3", variable=fourthCheckbox, onvalue=100.00, offvalue=0.00)
c1.grid(row=0,column=0)
c2.grid(row=1,column=0)
c3.grid(row=2,column=0)
c4.grid(row=3,column=0)

def print_total(event):
    total = firstCheckbox.get() + secondCheckbox.get() + thirdCheckbox.get() + fourthCheckbox.get()
    print(total)

button_1 = Button(root, text="Add Total")
# <Button-1> is an event that means "clicked left mouse button"
button_1.bind("<Button-1>", print_total)
button_1.grid(row=4,column=0)

root.mainloop()