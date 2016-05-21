from tkinter import *
root = Tk()

'''
You must know the number of rows and columns in your grid before using the following
Remember range(0,2) is for numbers 0 and 1; it does not include 2
This is for a 2 x 2 grid with row and column numbers starting at zero
For a 4 x 4 grid, you would use range(0,4), etc.
'''
for x in range(0,2):
    root.grid_rowconfigure(x,weight=1)
    root.grid_columnconfigure(x,weight=1)

t=Entry(root)
t.grid(sticky=N+E+S+W) # must have sticky=N+E+S+W to expand widgets proportionally
t.insert(END, "test")

t2=Entry(root)
t2.grid(sticky=N+E+S+W)
t2.insert(END, "test")

root.mainloop()
