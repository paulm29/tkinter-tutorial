from tkinter import *
from tkinter.ttk import *

root = Tk()

tree = Treeview(root)

tree["columns"]=("one","two")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("" , 0,    text="Line 1", values=("1A","1b"))
tree.insert("" , 1,    text="Line 2", values=("2A","2b"))

tree.pack()
root.mainloop()