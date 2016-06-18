from tkinter import *
import winsound
import time

root = Tk()

soundfile = "X.wav"
winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)

# wait 17.5 seconds
time.sleep(17.5)

# play the system exit sound if set
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

#root.mainloop()

