from tkinter import *

root = Tk()

myLabel = Label(root,text='Hello')
myLabel.grid(row=0, column=0)

'''
#pack version
myLabel = Label(root,text='Hello')
myLabel.pack()
'''

myLabel['text'] = "c\nhange text" # using \n the newline character

# Font is a tuple of (font_family, size_in_points, style_modifier_string)
myLabel.config(font=('times', 48, 'italic bold underline'))

myLabel.config(foreground='yellow', background='black')

myLabel.config(wraplength=70)

print(myLabel.config())

root.mainloop()