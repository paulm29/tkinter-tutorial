from tkinter import *

class MyButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text="Print Message", command=self.print_message)
        self.printButton.pack(side=LEFT)
        self.quitButton = Button(frame, text="Quit", command=root.destroy)
        self.quitButton.pack(side=LEFT)
    def print_message(self):
        print("Wow, this actually worked!")

root = Tk()
b = MyButtons(root)
root.mainloop()