from tkinter import *

root = Tk()

def openWindow():
    window1 = Toplevel()
    window1.title("About Rocket Shipping.exe")
    #window1.wm_iconbitmap('app.ico')
    window1.geometry("300x200")
    window1.resizable(0,0)
    window1 = Label(window1, text="Open")
    window1.place(x=0, y=0)
    window1['text'] = "change me"
    window1.config(font=('times', 48, 'italic bold underline'))
    window1.config(foreground='yellow', background='black')
    #window1.config(wraplength=200)
    print(window1.config)

button1 = Button(root, text="About RocketShipping", fg="black", bd=5, relief=RAISED, command=openWindow)
button1.place(x=50, y=50)

root.mainloop()