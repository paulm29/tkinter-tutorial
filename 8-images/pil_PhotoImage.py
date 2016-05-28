# to use JPEG images, you need to use Pillow
# PIL, http://pillow.readthedocs.io/en/3.2.x/index.html
from tkinter import *
import PIL.Image
import PIL.ImageTk

root = Tk()

im = PIL.Image.open("seagulls.jpeg")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.grid(row=0,column=0)

root.mainloop()