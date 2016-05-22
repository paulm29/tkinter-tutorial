#not the clearest example
# from http://stackoverflow.com/questions/34852925/python-tkinter-quiz
import tkinter as tk
window = tk.Tk()
window.title("6 Questions")
window.geometry("500x150")
score = 0
def inst():
    t = tk.Label(window, text="All you need to do is just answer each question with either a '1, 2, 3' or the actual word.")
    t.pack()

def start():
    def submit():
        print (ans.get())
        #or do whatever you like with this

    root = tk.Tk()
    root.title("question 1")
    q = tk.Label(root, text="what type of input holds whole numbers")
    q.pack()
    a = tk.Label(root, text="1.) int")
    a.pack()
    b = tk.Label(root, text="2.) string")
    b.pack()
    c = tk.Label(root, text="3.) float")
    c.pack()
    ans = tk.Entry(root, width=40)
    ans.pack()
    #here is the button I want to verify the answer
    sub = tk.Button(root, text="Submit", command=submit)
    sub.pack()


greet = tk.Label(window, text="Welcome to the 6 Question Quiz.")
greet.pack()
startButton = tk.Button(window, command=start, text="Start")
startButton.pack()
instr = tk.Button(window, text="Instructions", command=inst)
instr.pack()
end = tk.Button(window, text="Exit", command=window.destroy)
end.pack()

window.mainloop()