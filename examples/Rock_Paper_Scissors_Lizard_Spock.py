#-------------------------------------------------------------------------------
# Name:        tk_graphical_rpsls.py
#
# Purpose:   learn Tkinter using games we coded in Dr. Warren's and Dr. Rixner's
#                 Python class and convert them to a graphical format with
#                   tkinter
#
# Author:      Bill
#
#
# Created:     Nov 1, 2012  (edits for font color and size)
#
# Licence:     feel free to modify this
#-------------------------------------------------------------------------------
#
#
#  demonstrates tkinter widgets Frame, Canvas, Radiobutton, Label and Text
#   plus drawing circles and text in the canvas
#

try:
    from tkinter import *     # Python 3.x
except ImportError:
    from Tkinter import *     # Python 2.5 - 2.7

import random
import os   # this is just to ring the bell when computer wins

root = Tk()  # defines the main window, assigned variable name 'root'
root.geometry("600x520+230+180")
"""
 creates window 600 x 500 pixels that is offset 230 pix in x and
 180 pix in y from upper left corner of YOUR window.  To see the benefit
 of the optional '+230+180' code comment out root.geometry(...) above
 and uncomment the next line and note the new window is too high and left
  """
#root.geometry("600x520")

root.title('Rock Paper Scissors Lizard Spock')
frame1 = Frame(root)
frame1.grid(row = 0, column = 0)

canvas = Canvas(root,width=500, height=520, bg='white')
canvas.grid(row = 0, column = 1)


#  initialize variables
#
rb_var = IntVar()        # radio button for player choices
rb_mode_var = IntVar()

rb_var.set(" ")   # if you omit this line then the first button ('rock') is
                  # assigned at start-up; uncomment this and none are selected
                  #  at start-up, which is better since it forces the
                  #  player to push a button to start the game
"""
 radio button group variables.  IntVar() is a tkinter class name required
 for tracking Checkbutton or Radiobutton results (here I'm generating integers)
 ... http://effbot.org/tkinterbook/variable.htm for more info
>
 this is important ... if you just assign rb_var as an integer variable then
 the radio buttons won't work ... try it by commenting out the
 rb_var = IntVar()  line and writing rb_var = 0  ...
"""

player_wins = 0   # initialize score keeping variables
comp_wins = 0
ties = 0

b_Rixner = False  # boolean flag, set True when in Scott Rixner mode

"""
   the advantage of setting these values in constants is that if I want to
    change a color I can just enter one new value here instead of having
    to copy/paste that number every time a circle is filled with that
    number, which happens often in the code below
"""

FILL_CIRCLES = "#FFF8DC"   # color fill for unselected circles
C_GUESS = '#FF69B4'        #  color fill for computer guess circle
PLAYER_GUESS = '#87CEFA'   #  color fill for player's selection
TIE_COLOR = '#FFD700'      #  color used for a tie

CIRCLE_FONT = "Verdana 10"  # font for circle names
F_HEL_12 = "Helvetica 12"   # font for displaying who won game

LAB_WIDTH = 14             #  width of buttons/labels in frame
FUDGE = 3                  #  set to 1 in "Rixner mode" to see what this does!

#  functions
#
def rb_pushed():
    """ when a radio button is selected this changes colors on the circle """

    pick = rb_var.get()
    """
    .get() is a method used to grab text associated
    with rb_var, which was assigned below to the radio
    button group when I created the radio buttons.
    so it shows which of the five choices the player
    made when they clicked one of the 5 radio buttons

    code below  re-colors the circles (1 or 2 will be different after each game)

     'canvas' is the variable name for my Canvas, 'itemconfig' is a reserved
      tkinter instruction allowing you to change a configuration, 'rock' is
      the variable name I gave a circle below when I created it, 'fill' is
      the color inside a circle
    """
    canvas.itemconfig(rock, fill=FILL_CIRCLES)
    canvas.itemconfig(paper, fill=FILL_CIRCLES)
    canvas.itemconfig(scissors, fill=FILL_CIRCLES)
    canvas.itemconfig(lizard, fill=FILL_CIRCLES)
    canvas.itemconfig(Spock, fill=FILL_CIRCLES)

    # this block fills the selected block with PLAYER_GUESS color
    #
    if pick == 0:
        canvas.itemconfig(rock, fill=PLAYER_GUESS)
    elif pick == 1:
        canvas.itemconfig(Spock, fill=PLAYER_GUESS)
    elif pick == 2:
        canvas.itemconfig(paper, fill=PLAYER_GUESS)
    elif pick == 3:
        canvas.itemconfig(lizard, fill=PLAYER_GUESS)
    elif pick == 4:
        canvas.itemconfig(scissors, fill=PLAYER_GUESS)

    """  clear the text message in the center of the circles describing who won
         the previous game ... state='hidden' leaves the text in place but
         doesn't display it
    """
    canvas.itemconfig(t_player_wins, state = 'hidden')
    canvas.itemconfig(t_comp_wins, state = 'hidden')
    canvas.itemconfig(t_tie, state = 'hidden')
    canvas.itemconfig(t_rix_wins, state = 'hidden')

def rb_mode():
    """ set mode flag - HAL 9000 isn't supported so it's 'Rixner mode' or normal """
    global b_Rixner
    mode = rb_mode_var.get()
    if mode == 2:
        b_Rixner = True
    else:
        b_Rixner = False

def reset_scores():
    """ handler for reset button ... clears scores """
    global player_wins, comp_wins, ties
    player_wins = 0
    comp_wins = 0
    ties = 0
    update_scores()

def update_scores():
    global player_wins, comp_wins, ties
    t_disp.delete(0.0, END)  # clears text box
    t_disp.insert(END, '\n')
    t_disp.insert(END, " You   = \t" + str(player_wins))  # \t for a tab
    t_disp.insert(END, '\n')
    if b_Rixner:
        t_disp.insert(END, " Scott = \t" + str(comp_wins))
    else:
        t_disp.insert(END, " Comp  = \t" + str(comp_wins))
    t_disp.insert(END, '\n')
    t_disp.insert(END, " Ties  = \t" + str(ties))
    t_disp.insert(END, '\n')

def play_game():
    """ main rpsls function - generates computer guess and decides on winner """

    global player_wins, comp_wins, ties

    player_pick = rb_var.get()
    comp_number = random.randrange(0,5)
    if b_Rixner and (player_wins + comp_wins + ties) % FUDGE == 0:
        if player_pick == 4:
            comp_number = 1
        else:
            comp_number = player_pick + 1

    # this block colors the circle for the computer's guess
    #
    if comp_number == 0:
        canvas.itemconfig(rock, fill=C_GUESS)
    elif comp_number == 1:
        canvas.itemconfig(Spock, fill=C_GUESS)
    elif comp_number == 2:
        canvas.itemconfig(paper, fill=C_GUESS)
    elif comp_number == 3:
        canvas.itemconfig(lizard, fill=C_GUESS)
    elif comp_number == 4:
        canvas.itemconfig(scissors, fill=C_GUESS)

    # modulo 5 to decide on the winner
    #
    diff = (comp_number - player_pick) % 5
    if diff == 0:
        ties = ties + 1

        #  state = 'normal' makes the print visible in the center of the circles
        #
        canvas.itemconfig(t_tie, state = 'normal')

        # in case of a tie we change the color of the chosen circle
        #
        if comp_number == 0:
            canvas.itemconfig(rock, fill=TIE_COLOR)
        elif comp_number == 1:
            canvas.itemconfig(Spock, fill=TIE_COLOR)
        elif comp_number == 2:
            canvas.itemconfig(paper, fill=TIE_COLOR)
        elif comp_number == 3:
            canvas.itemconfig(lizard, fill=TIE_COLOR)
        elif comp_number == 4:
            canvas.itemconfig(scissors, fill=TIE_COLOR)

    elif diff == 3 or diff == 4:
            canvas.itemconfig(t_player_wins, state = 'normal')
            player_wins = player_wins + 1
    else:
        comp_wins = comp_wins + 1
        os.system('\a')  # this rings the bell
        if b_Rixner:
            canvas.itemconfig(t_rix_wins, state = 'normal')
        else:
            canvas.itemconfig(t_comp_wins, state = 'normal')

    update_scores()

    #  stop displaying the rules texts after 3 games
    #
    if ((comp_wins + player_wins + ties) >= 4):
        canvas.itemconfig(t_rules1, state = 'hidden')
        canvas.itemconfig(t_rules2, state = 'hidden')


"""
create circles and text on the canvas

  to take one line in detail,
  'rock' is just a variable I assigned to thiscircle.
  'canvas' is my variable name for this Canvas widget.
  '.create_oval' is a tkinter function for creating an oval ... if you define
     a square it's a circle; a rectangle gives an oval.  200,100 are the x,y
     coordinates of one corner of my square, 300,200 the other corner.
  'width' is the width of the line drawing the circle
  'fill' is as described above in the rb_pushed() function.
"""

rock = canvas.create_oval(200, 100, 300, 200, width=2, fill= FILL_CIRCLES)
scissors = canvas.create_oval(75, 180, 175, 280, width=2, fill=FILL_CIRCLES)
Spock = canvas.create_oval(325, 180, 425, 280, width=2, fill=FILL_CIRCLES)
lizard = canvas.create_oval(125, 300, 225, 400, width=2, fill=FILL_CIRCLES)
paper = canvas.create_oval(275, 300, 375, 400, width=2, fill=FILL_CIRCLES)

# text labels that go with the circles
#
t_rock = canvas.create_text(250, 150, text = "rock", font = CIRCLE_FONT)
t_scissors = canvas.create_text(125, 230, text = "scissors", font = CIRCLE_FONT)
t_Spock = canvas.create_text(378, 230, text = "Spock", font = CIRCLE_FONT)
t_lizard = canvas.create_text(175, 350, text = "lizard", font = CIRCLE_FONT)
t_paper = canvas.create_text(328, 350, text = "paper", font = CIRCLE_FONT)

t_rules1 = canvas.create_text(20,40, justify = 'left', anchor = 'w', font = "Helvetica 9",
text = "Rules: \n\nrock crushes lizard or scissors\nscissors cuts paper, decapitates lizard\nSpock smashes scissors, vaporizes rock")

t_rules2 = canvas.create_text(260,450, justify = 'left', font = "Helvetica 9",
text = "Rules (con't): \n\nlizard poisons Spock or eats paper\npaper covers rock or disproves Spock")

"""
4 centered hidden text strings ... will enable one when winner is chosen

  by now you should see the pattern ... 't_comp_wins' is a variable,
  'canvas' is my variable for this Canvas, '.create_text' is obvious etc
"""
t_comp_wins = canvas.create_text(250,250, text = "Computer Wins!",
   fill = "magenta", font = F_HEL_12 )
canvas.itemconfig(t_comp_wins, state = 'hidden')

t_player_wins = canvas.create_text(250,250, text = "You Won!",
   fill = "blue", font = F_HEL_12 )
canvas.itemconfig(t_player_wins, state = 'hidden')

t_tie = canvas.create_text(250,250, text = "We Have a Tie",
   state = 'hidden', font = F_HEL_12 )
canvas.itemconfig(t_tie, state = 'hidden')

t_rix_wins = canvas.create_text(250,250, text = "Scott Rixner Wins!",
   fill = "magenta", font = F_HEL_12 )
canvas.itemconfig(t_rix_wins, state = 'hidden')

"""
  load labels and five radio buttons on the left (frame1) for player to make
   a choice

  this is a Label widget in tkinter-speak ... 'L_sel' is my variable name,
  'Label' the tkinter keyword, 'frame1' my variable name for the Frame, text
  is what appears on the label, and 'width' is in characters, not pixels
"""
L_sel = Label(frame1, text="Select One", width = 12)
L_sel.grid(column = 0, row = 0, pady = 2)

"""
  OK, here are the radio buttons ... 'rb_rock' is my variable name for
  the rock choice, 'Radiobutton' the tkinter keyword for this type widget,
  frame1 signifies this Frame ... 'text' is what shows on the screen beside
  the button ... now it gets interesting so try to follow this next part ...

  'variable' is how buttons are grouped together, i.e., the buttons that share
  the same variable are considered a group so only one can be on at a time.
  so here it's 'rb_var' and we used rb_var.get() above in rb_pushed() to
  load the 'value' in that function.  'value' is what gets passed, in this
  group for example I passed 0,1,2,3,4 instead of the names to make it easier
  to do the modulo math.

  'command' is the event handler function.  'width' is in characters, pady
   is for creating a bit of y-spacing between cells, and 'anchor = W'
   left-justifies the buttons instead of centering them.  Feel free to modify
   some of these fields to see what happens (though it's wise to keep a
   clean copy)
"""

rb_rock = Radiobutton(frame1, text="rock",variable = rb_var, value=0,
command = rb_pushed, width = LAB_WIDTH, pady = 2,anchor = W)
rb_rock.grid(row = 2, column = 0)

rb_paper = Radiobutton(frame1, text ="paper",variable = rb_var, value=2,
command = rb_pushed, width = LAB_WIDTH, pady = 2, anchor = W)
rb_paper.grid(row = 4, column = 0)

rb_scissors = Radiobutton(frame1, text = "scissors",variable = rb_var, value=4,
command = rb_pushed, width = LAB_WIDTH,pady = 2, anchor = W)
rb_scissors.grid(row = 5, column = 0)

rb_lizard = Radiobutton(frame1, text = "lizard",variable = rb_var, value=3,
command = rb_pushed, width = LAB_WIDTH,pady = 2, anchor = W)
rb_lizard.grid(row = 6, column = 0)

rb_Spock = Radiobutton(frame1, text = "Spock",variable = rb_var, value=1,
command = rb_pushed, width = LAB_WIDTH, pady = 2,anchor = W)
rb_Spock.grid(row = 7, column = 0)

# 'play the game' button, score Text field
#
Lblank = Label(frame1, text="", width = 12)  # blank label for spacing ...
Lblank.grid(column = 0, row = 8, pady = 2)

#  this is a simple Button, which links to the function play_game().
#
b_play = Button(frame1, text='Push to Play', command=play_game, width = LAB_WIDTH,
pady = 2, background = "white")
b_play.grid(row = 9, column = 0)

Lblank2 = Label(frame1, text="", width = LAB_WIDTH)  # blank label for spacing ...
Lblank2.grid(column = 0, row = 10, pady = 2)

L_score = Label(frame1, text="Scores", width = LAB_WIDTH)
L_score.grid(column = 0, row = 11, pady = 2)

# this is a widget of type Text, where I update the cumulative scores in
#   the 'play_game()' function above
#
t_disp = Text(frame1, width = LAB_WIDTH, height = 5)
t_disp.grid(row = 13, column = 0)


Lblank_text = Label(frame1, text="", width = LAB_WIDTH)  # blank label for spacing ...
Lblank_text.grid(column = 0, row = 15, pady = 2)

b_reset = Button(frame1, text='Reset Scores', command=reset_scores, width = LAB_WIDTH,
pady = 2, background = "white")
b_reset.grid(row = 16, column = 0)


# change mode radio buttons
#
Lblank_mode = Label(frame1, text="", width = 12)  # blank label for spacing ...
Lblank_mode.grid(column = 0, row = 17, pady = 2)

L_sel_mode = Label(frame1, text="Select Mode", width = 12)
L_sel_mode.grid(column = 0, row = 18, pady = 2)

rb_randy = Radiobutton(frame1, text="Random",variable = rb_mode_var, value=0,
command = rb_mode, width = LAB_WIDTH, pady = 2, indicatoron=0)
rb_randy.grid(row = 19, column = 0)

rb_HAL = Radiobutton(frame1, text ="HAL 9000",variable = rb_mode_var, value=1,
command = rb_mode, width = LAB_WIDTH, pady = 2, indicatoron=0)
rb_HAL.grid(row = 20, column = 0)

rb_Rixner = Radiobutton(frame1, text = "Scott Rixner",variable = rb_mode_var, value=2,
command = rb_mode, width = LAB_WIDTH,pady = 2, indicatoron=0)
rb_Rixner.grid(row = 22, column = 0)

#  graceful exit
#
def quit_this():
    root.quit()
    root.destroy()

rb_Quit = Radiobutton(frame1, text = "QUIT", variable = rb_mode_var, value=3,
    command = quit_this, width = LAB_WIDTH, pady = 6, indicatoron=0)
rb_Quit[ "fg" ] = "DarkRed"
rb_Quit[ "bg" ] = "Bisque"
rb_Quit.grid(row = 25, column = 0)

#  and this kicks it off ... hope you enjoyed the tour of tkinter widgets!
#
mainloop()

"""
Some suggested additions and improvements (feel free to modify my code!)

1) The 'rules' text disappears after 4 games ... add a button 'Show Rules' that
turns this text back on if clicked, then hides them if clicked again.

2) Turn off that annoying beep when the computer wins (search for \a string)

3) Keep track of the actual choices the player makes and display them numerically
in the upper-right corner for one game after every 20 games, then hide them after
one more game.

4) If the player doesn't click a radio button the game will still play, using
his last pick, but colors won't be reset so the colors for the circles will eventually
have four magenta and one yellow circle, and all three text options will overwrite
each other in the center of the circles.  Change it so this doesn't happen
(either with a message to the player to select a button, or by clearing things
properly).

5) This is a boring game because it's too random.  I added a "Scott Rixner" mode
(Scott somehow manages to win a lot, no matter what the player does).

Scott takes the place of the computer but the scores don't reset unless you
  push the reset button, so fix that.

Now we need to add the "HAL 9000" mode that uses the machine learning algorithm
  so the computer 'learns' an advantage over predictable players.  If you don't
  know what HAL 9000 is check on youtube.com (from the movie "2001: A Space Odyssey").

  This code should look for patterns in the user's choices
  and then select computer choices to give the computer a slight edge.

"""