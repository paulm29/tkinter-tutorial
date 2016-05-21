from tkinter import *

root = Tk()
root.geometry("250x150+300+300")

def move(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))
    newX = event.x + dragmeLabel.winfo_width() / 2
    newY = event.y + dragmeLabel.winfo_height() / 2
    dragmeLabel.place_configure(x=newX,y=newY)

def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

def onLeftDrag(event):
    print('Got left mouse button drag:',
    move(event))

def onLeftRelease(event):
    print('Got left mouse button release:',
    showPosEvent(event))

dragmeLabel = Label(root,text="dragme",bd=1,relief=SUNKEN)
dragmeLabel.bind("<B1-Motion>",onLeftDrag) # <ButtonPress-1>
dragmeLabel.bind('<ButtonRelease-1>', onLeftRelease)
dragmeLabel.place(x=0,y=0)

root.mainloop()