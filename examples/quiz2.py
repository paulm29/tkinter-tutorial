from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox


def answerQuestion(event):
    # global means we are using the variables that already exists outside of the function
    global score, questionNumber, quizComplete

    if quizComplete:
        tkinter.messagebox.showinfo("Quiz Complete", "You have answered all the questions!")
        return

    print(answerText.get())
    if answerText.get() == "":
        tkinter.messagebox.showerror("Error","You must enter an answer")
        return

    if answerText.get() in answers[questionNumber]:
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
    print(questions[questionNumber])
    questionText.delete(0,END)
    questionText.insert(0,questions[questionNumber])
    answerText.delete(0,END)

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

root = Tk()

root.title("My Quiz")
root.geometry("450x300+100+100") # width x height + x position + y position
root.wm_iconbitmap('my_app.ico')
root.option_add("*tearOff", False)

''' Create widgets '''
questionLabel = Label(root, text="Question:")
answerLabel = Label(root, text="Answer:")
scoreLabel = Label(root, text="Score: 0")
questionsLeftLabel = Label(root, text="Questions left: ")
questionText = Entry(root)
answerText = Entry(root)
answerQuestionButton = Button(root,text="Submit answer")
answerQuestionButton.bind("<Button-1>", answerQuestion)
resetQuizButton = Button(root,text="Reset Quiz")
resetQuizButton.bind("<Button-1>", resetQuiz)

#loadQuizButton
#filename = askopenfile()

''' Place widgets on the grid '''
questionLabel.grid(row=0, sticky=E) # E is for east or right alignment
answerLabel.grid(row=1, sticky=E)
questionText.grid(row=0, column=1)
answerText.grid(row=1, column=1)
answerQuestionButton.grid(row=2, column=1)
scoreLabel.grid(columnspan = 2, sticky=W)
questionsLeftLabel.grid(columnspan = 2, sticky=W)
resetQuizButton.grid(row=5, column=1)

''' variables used throughout the application '''
questions = ['first question', 'second question', 'third question']
answers = ['answer1','answer2','answer3']
questionNumber = 0 # 0 is the first question
score = 0
quizComplete = False
numberOfQuestions = len(questions)

# show the first question
getNextQuestion()
getQuestionsLeft()

root.mainloop()