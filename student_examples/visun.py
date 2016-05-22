from tkinter import * #import all the tkinter classes so that we can use them

root = Tk()  # create a blank window called root

root.title("Booking System for Brisbane Airport")
root.geometry("450x300+100+100") # width x height + x position + y position
#root.wm_iconbitmap('people.ico')
root.configure(background="#e6e6fa") #lavender

def bookflight():
    print("I'm going to 9/11 this plane.")

myButton = Button(root, text="Book this flight", command=bookflight)
myButton.grid(row=0,column=4)
myButton = Button(root, text="Book this flight", command=bookflight)
myButton.grid(row=1, column=4)
myButton = Button(root, text="Book this flight", command=bookflight)
myButton.grid(row=1, column=4)
myButton = Button(root, text="Book this flight", command=bookflight)
myButton.grid(row=3, column=4)
myButton = Button(root, text="Book this flight", command=bookflight)
myButton.grid(row=4, column=4)
myButton = Button(root, text="Book this flight", command=bookflight)
myButton.grid(row=5, column=4)
myButton = Button(root, text="Book this flight", command=bookflight)
myButton.grid(row=6, column=4)

myListbox = Listbox(root,exportselection=0, width=40)
myListbox.insert(2, "Brisbane to JFK (Departure 6:45pm)")
myListbox.insert(3, "Brisbane to Wellington (Departure 6:45pm)")
myListbox.insert(4, "Brisbane to Hong Kong (Departure 7:00pm)")
myListbox.insert(5, "Brisbane to Singapore (Departure 7:00pm)")
myListbox.insert(6, "Brisbane to London (Departure 7:10pm)")
myListbox.insert(7, "Brisbane to LAX (Departure 7:10pm)")
myListbox.insert(8, "Brisbane to Rome (Departure 7:30pm)")
myListbox.grid(row=0, column=0, rowspan=7)


root.mainloop()