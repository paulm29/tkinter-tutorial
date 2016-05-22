# Example to show the different widgets that come with tkinter

from tkinter import *


def button():
    master = Tk()

    def callback():
        print("click!")

    b = Button(master, text="Button", command=callback)
    b.pack()
    mainloop()


def canvas():
    master = Tk()
    master.title("Canvas")
    w = Canvas(master, width=200, height=100)
    w.pack()
    w.create_line(0, 0, 200, 100)
    w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
    w.create_rectangle(50, 25, 150, 75, fill="blue")
    mainloop()


def checkbutton():
    master = Tk()
    var = IntVar()
    c = Checkbutton(master, text="Checkbutton", variable=var)
    c.pack()
    mainloop()


def entry():
    master = Tk()
    master.title("Entry")
    e = Entry(master)
    e.pack()
    mainloop()


def frame():
    master = Tk()
    master.title("Frame")
    Label(text="above Frame separator").pack()
    separator = Frame(height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)
    Label(text="below Frame separator").pack()
    mainloop()


def label():
    master = Tk()
    w = Label(master, text="Label")
    w.pack()
    mainloop()


def labelframe():
    master = Tk()
    group = LabelFrame(master, text="LabelFrame", padx=5, pady=5)
    group.pack(padx=10, pady=10)
    w = Entry(group)
    w.pack()
    mainloop()


def listbox():
    master = Tk()
    master.title("Listbox")
    listbox = Listbox(master)
    listbox.pack()
    for item in ["one", "two", "three", "four"]:
        listbox.insert(END, item)
    mainloop()


def menu():
    root = Tk()
    root.title("Menu")

    def hello():
        print
        "hello!"

    # create a toplevel menu
    menubar = Menu(root)
    menubar.add_command(label="Menu1", command=hello)
    menubar.add_command(label="Menu2", command=root.quit)
    # display the menu
    root.config(menu=menubar)
    mainloop()


def message():
    master = Tk()
    master.title("Message")
    w = Message(master, text="this is a message")
    w.pack()
    mainloop()


def optionmenu():
    master = Tk()
    master.title("OptionMenu")
    variable = StringVar(master)
    variable.set("one")  # default value
    w = OptionMenu(master, variable, "one", "two", "three")
    w.pack()
    mainloop()


def panedwindow():
    m1 = PanedWindow()
    m1.pack(fill=BOTH, expand=1)
    left = Label(m1, text="PanedWindow left")
    m1.add(left)
    m2 = PanedWindow(m1, orient=VERTICAL)
    m1.add(m2)
    top = Label(m2, text="PanedWindow top")
    m2.add(top)
    bottom = Label(m2, text="PanedWindow bottom")
    m2.add(bottom)
    mainloop()


def radiobutton():
    master = Tk()
    master.title("RadioButton")
    v = IntVar()
    Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
    Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W)
    mainloop()


def scale():
    master = Tk()
    master.title("Scale")
    w = Scale(master, from_=0, to=100)
    w.pack()
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()
    mainloop()


def scrollbar():
    master = Tk()
    master.title("Scrollbar")
    scrollbar = Scrollbar(master)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(master, yscrollcommand=scrollbar.set)
    listbox.insert(END, "Listbox")
    for i in range(1000):
        listbox.insert(END, str(i))
    listbox.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=listbox.yview)
    mainloop()


def spinbox():
    master = Tk()
    master.title("Spinbox")
    w = Spinbox(master, from_=0, to=10)
    w.pack()
    mainloop()


def text():
    master = Tk()
    master.title("Text")
    textBox = Text(master, wrap=WORD)
    textBox.grid()
    mainloop()


def bitmapimage():
    BITMAP = """
    #define im_width 32
    #define im_height 32
    static char im_bits[] = {
    0xaf,0x6d,0xeb,0xd6,0x55,0xdb,0xb6,0x2f,
    0xaf,0xaa,0x6a,0x6d,0x55,0x7b,0xd7,0x1b,
    0xad,0xd6,0xb5,0xae,0xad,0x55,0x6f,0x05,
    0xad,0xba,0xab,0xd6,0xaa,0xd5,0x5f,0x93,
    0xad,0x76,0x7d,0x67,0x5a,0xd5,0xd7,0xa3,
    0xad,0xbd,0xfe,0xea,0x5a,0xab,0x69,0xb3,
    0xad,0x55,0xde,0xd8,0x2e,0x2b,0xb5,0x6a,
    0x69,0x4b,0x3f,0xb4,0x9e,0x92,0xb5,0xed,
    0xd5,0xca,0x9c,0xb4,0x5a,0xa1,0x2a,0x6d,
    0xad,0x6c,0x5f,0xda,0x2c,0x91,0xbb,0xf6,
    0xad,0xaa,0x96,0xaa,0x5a,0xca,0x9d,0xfe,
    0x2c,0xa5,0x2a,0xd3,0x9a,0x8a,0x4f,0xfd,
    0x2c,0x25,0x4a,0x6b,0x4d,0x45,0x9f,0xba,
    0x1a,0xaa,0x7a,0xb5,0xaa,0x44,0x6b,0x5b,
    0x1a,0x55,0xfd,0x5e,0x4e,0xa2,0x6b,0x59,
    0x9a,0xa4,0xde,0x4a,0x4a,0xd2,0xf5,0xaa
    };
    """
    master = Tk()
    master.title("BitmapImage")
    bitmap = BitmapImage(data=BITMAP)
    label = Label(image=bitmap)
    label.pack()
    mainloop()


def photoimage():
    master = Tk()
    master.title("PhotoImage")
    photo = PhotoImage(file="akeric.gif")
    label = Label(image=photo)
    label.image = photo  # keep a reference!
    label.pack()
    mainloop()


if __name__ == "__main__":
    which = input("Type: ")

    if which == "Button":
        button()
    elif which == "Canvas":
        canvas()
    elif which == "Checkbutton":
        checkbutton()
    elif which == "Entry":
        entry()
    elif which == "Frame":
        frame()
    elif which == "Label":
        label()
    elif which == "LabelFrame":
        labelframe()
    elif which == "Listbox":
        listbox()
    elif which == "Menu":
        menu()
    elif which == "Message":
        message()
    elif which == "OptionMenu":
        optionmenu()
    elif which == "PanedWindow":
        panedwindow()
    elif which == "RadioButton":
        radiobutton()
    elif which == "Scale":
        scale()
    elif which == "Scrollbar":
        scrollbar()
    elif which == "Spinbox":
        spinbox()
    elif which == "Text":
        text()
    elif which == "BitmapImage":
        bitmapimage()
    elif which == "PhotoImage":
        photoimage()

    else:
        print("fail")

