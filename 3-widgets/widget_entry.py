from tkinter import *
root = Tk()

myEntry = Entry(root,text="test")
myEntry.grid(row=0, column=0)

#get the text that a user has entered
theText = myEntry.get()
print(theText)

# To change the text in an Entry
myEntry.delete(0, END) # delete existing text
myEntry.insert(0, "new text") # enter new text

myEntry.config(state="disabled") # prevent user entering text

myEntry.grid_remove() # remove widget, leaving a blank space
myEntry.grid() # bring it back, exactly where it was before

root.mainloop()