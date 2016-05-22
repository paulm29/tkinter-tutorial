questionNumber = 0
answers = ['A','C','B']

def checkAnswerA():
    if answers[questionNumber] == "A":
        print("you got it right")
    else:
        print("you got it wrong")

def checkAnswerB():
    if answers[questionNumber] == "B":
        print("you got it right")

aButton = Button(root, text="A")
bButton.bind("<Button-1>", checkAnswerA)