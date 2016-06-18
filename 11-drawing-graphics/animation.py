from tkinter import *

def move_rectangle():
    # move rectangle
    canvas.move(my_rectangle,5,0)

    # run move_rectangle again after 100ms (0.1s)
    root.after(100, move_rectangle) # function name without ()

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()

my_rectangle = canvas.create_rectangle(10, 10, 50, 50)

# run `move_rectangle` first time after 100ms (0.1s)
root.after(100, move_rectangle) # function name without ()

root.mainloop()