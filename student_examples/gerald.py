# quiz with multiple choice buttons
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
import random

root = Tk()
root.title("My Quiz")
root.geometry("950x950+50+50") # width x height + x position + y position
root.wm_iconbitmap('my_app.ico')
root.option_add("*tearOff", False)
root.configure(bg="white")

def answer(answerNumber):
    # global means we are using the variables that already exists outside of the function
    global score, questionNumber, quizComplete
    #if quizComplete:
    #    tkinter.messagebox.showinfo("Quiz Complete", "You have answered all the questions!")
    #    return
    #print(questions[questionNumber][1])
    #if answerText.get() == "":
    #    tkinter.messagebox.showerror("Error","You must enter an answer")
    #    return
    print("user's answer: " + questions[questionNumber][answerNumber])
    print("actual answer: " + questions[questionNumber][1])
    if questions[questionNumber][answerNumber] == questions[questionNumber][1]:
        score += 1
        scoreLabel['text'] = "Score: " + str(score)
    questionNumber += 1
    getQuestionsLeft()
    if questionNumber == numberOfQuestions:
        tkinter.messagebox.showinfo("Quiz Complete","You have answered all the questions!")
        getQuestionsLeft()
        quizComplete = True
    else:
        getNextQuestion()

def getNextQuestion():
    global photo
    currentQuestion = questions[questionNumber]
    currentQuestionText = currentQuestion[0]
    print("Next question: " + currentQuestionText)

    questionText.delete(0,END)
    questionText.insert(0,currentQuestionText)

    # randomise answers
    randomOrderList = random.sample(range(1, 5), 4)
    print(randomOrderList)

    firstButton.config(text=currentQuestion[randomOrderList[0]])
    secondButton.config(text=currentQuestion[randomOrderList[1]])
    thirdButton.config(text=currentQuestion[randomOrderList[2]])
    fourthButton.config(text=currentQuestion[randomOrderList[3]])

    firstButton.config(command=lambda: answer(randomOrderList[0]))
    secondButton.config(command=lambda: answer(randomOrderList[1]))
    thirdButton.config(command=lambda: answer(randomOrderList[2]))
    fourthButton.config(command=lambda: answer(randomOrderList[3]))

    print("photo: " + currentQuestion[5])
    photo = PhotoImage(file=currentQuestion[5])
    photoLabel.config(image=photo)

def getQuestionsLeft():
    global numberOfQuestions, questionNumber
    questionsLeftLabel['text'] = "Questions left: " + str(numberOfQuestions - questionNumber)

def resetQuiz(event):
    global questionNumber, score, quizComplete
    quizComplete = False
    questionNumber = 0
    score = 0
    getNextQuestion()
    getQuestionsLeft()



''' variables used throughout the application '''
#questions = ['How bad is Oscar in MATHS', 'How good is Oscar at video games', 'Does Oscar like KFC']
#answers = ['failed/D','very good','He likes it put prefers boc chip']

# questions is a list of lists.
# each list contains a question and answers
# the first answer is the correct answer, and
# there are always 4 answers
# the last part of the list is to store an image name to display
# it must be a PNG or GIF image
questions = [
    ["How bad is Oscar in Maths?","Terrible","Very very bad","very bad","bad","smell.png"],
    ["Does Oscar like KFC?", "Yes, but he prefers boc chip", "Yes, but he prefers Mcdonalds", "No, he doesn't like any fastfood", "No, he isn't a fan of American foods.","ape.png"]
]

r = 6
firstButton = Button(root,text="A",command=lambda: answer(1), bg='white', fg='black')
secondButton = Button(root,text="B",command=lambda: answer(2), bg='white', fg='black')
thirdButton = Button(root,text="C",command=lambda: answer(3), bg='white', fg='black')
fourthButton = Button(root,text="D",command=lambda: answer(4), bg='white', fg='black')
firstButton.grid(row=r,column=0)
secondButton.grid(row=r,column=1)
thirdButton.grid(row=r,column=2)
fourthButton.grid(row=r,column=3)



''' Create widgets '''
scoreLabel = Label(root, text="Score: 0")
questionsLeftLabel = Label(root, text="Questions left: ")
questionText = Entry(root,width=50)

resetQuizButton = Button(root,text="Reset Quiz")
resetQuizButton.bind("<Button-1>", resetQuiz)

''' Place widgets on the grid '''
questionText.grid(row=0, column=0, columnspan=4)
scoreLabel.grid(columnspan = 2, sticky=W)
questionsLeftLabel.grid(columnspan = 10, sticky=W)
r = 9
resetQuizButton.grid(row=r, column=0)

r = 10
photo = PhotoImage(file="quiz.png")
photoLabel = Label(root,image=photo)
photoLabel.grid(row=r, column=0,columnspan=4)


questionNumber = 0 # 0 is the first question
score = 0
quizComplete = False
numberOfQuestions = len(questions)
# show the first question
getNextQuestion()
getQuestionsLeft()
root.mainloop()
