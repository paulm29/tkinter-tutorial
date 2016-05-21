from tkinter import *
root = Tk()
myListbox = Listbox(root,exportselection=0)
myListbox.insert(1, "Python")
myListbox.insert(2, "Perl")
myListbox.insert(3, "C")
myListbox.insert(4, "PHP")
myListbox.pack()

myList = ["one", "two", "three", "four"]
for item in myList:
    myListbox.insert(END, item) # END is the last position

myListbox.curselection() # get currently selected

for i, listbox_entry in enumerate(myListbox.get(0, END)):
    print (listbox_entry)

root.mainloop()