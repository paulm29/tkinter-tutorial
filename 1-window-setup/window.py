from tkinter import * #import all the tkinter classes so that we can use them

root = Tk()  # create a blank window called root

root.title("My awesome App")
root.geometry("450x300+100+100") # width x height + x position + y position
root.wm_iconbitmap('my_app.ico')
root.configure(background="#e6e6fa") #lavender

root.mainloop()  # make the program run forever