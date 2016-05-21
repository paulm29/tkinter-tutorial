from tkinter import *

root = Tk()
frame = Frame(root, relief=RIDGE)
frame.pack() # pack is being used inside root

#add button to frame, not root
button = Button(frame,text="A button")
button.grid(row=0, column=0) # grid is being used inside the frame

root.mainloop()