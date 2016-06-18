from tkinter import *
from tkinter.filedialog import *

lines = [] # contains lines of the file

def openfile():
    global lines # global means use the lines variables defined above
    filename = askopenfilename(parent=root) # ask user for filename
    file = open(filename)

    # for each line in the file, print it, and add to list
    for line in file:
       print(line) # print to the PyCharm console
       lines.append(line) # add to end of list

    # add each line in lines to the Listbox
    for eachLine in lines:
        myListbox.insert(END,eachLine) # END is the last position


root = Tk()

''' Create menu'''
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

''' Create listbox that will display each line of the file '''
myListbox = Listbox(root)
myListbox.grid(row=0,column=0)

root.mainloop()