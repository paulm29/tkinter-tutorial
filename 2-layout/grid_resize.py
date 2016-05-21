from tkinter import *
root = Tk()

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

t=Entry(root)
t.grid(sticky=N+E+S+W)
t.insert(END, "test")

t2=Entry(root)
t2.grid(sticky=N+E+S+W)
t2.insert(END, "test")

root.mainloop()
