from tkinter import * #import all the tkinter classes so that we can use them

root = Tk()  # create a blank window called root

root.title("My awesome App")
root.geometry("450x300+100+100") # width x height + x position + y position
root.wm_iconbitmap('my_app.ico')
topFrame = Frame(root)  # create a top frame
topFrame.pack()
bottomFrame = Frame(root)  # create a bottom frame
bottomFrame.pack(side=BOTTOM) # explicitly position the frame at the bottom
''' Create buttons, giving them a frame to be contained within, text, and a foreground colour '''
red = Button(topFrame, text="Red", fg="red")
yellow = Button(topFrame, text="Yellow", fg="yellow", bg="black")
green = Button(topFrame, text="Green", fg="green")
purple = Button(bottomFrame, text="Purple", fg="purple")
red.pack(side=LEFT)
yellow.pack(side=LEFT)
green.pack(side=LEFT)
purple.pack()
root.mainloop()  # make the program run forever