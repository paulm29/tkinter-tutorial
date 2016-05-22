
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                                              #
# Coursera class "Intro to Interactive Programming in Python"  #
#         Programming project 2 - "Guess the number"           #
#                   October 25, 2012                           #
#                                                              #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#
#  tk_gtn.py
#
#  converted to tkinter with basic graphics to display your guess and
#    the number of remaining guesses - May 2013
#
#  number of guesses is 6 or 9 so the computer has a fair chance to win too
#
#  tested in Python V2.7.3 IDLE, V3.2.3 IDLE and V3.2.3 PyScripter
#
import random
try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()  # defines the main window, assigned variable name 'root'
root.geometry("600x660+230+10")

root.title('Guess the Number')
frame1 = Frame(root)
frame1.grid(column = 0, row = 1)

frame_spacer_c0 = Frame(root)
frame_spacer_c0.grid(column = 0, row = 0)

frame_spacer_c1 = Frame(root)
frame_spacer_c1.grid(column = 1, row = 0)

canvas = Canvas(root,width=330, height=600, bg='white')
canvas.grid(column = 1, row = 1)

num_range = 100       # set to 100 or 1000 below
num_guesses = 0       # set to 6 or 9 below

BAR_WIDTH = 60
F_HEL_12 = "Helvetica 12"    # text fonts
V6 = "Verdana 8"

LIGHT_PINK = '#FFB6C1'       # non-default colors for color bar, etc
SKYBLUE = '#87CEEB'
LIGHTGREEN = '#90EE90'
DARKORANGE = '#FF8C00'
GOLD = '#FFD700'
YELLOW = '#FFFF00'
LIME = '#00FF00'
LAWNGREEN = '#7CFC00'
YELLOWGREEN = '#9ACD32'
PALETURQUOISE = '#AFEEEE'
ROYALBLUE = '#4169E1'

#  constants for 'number of guesses' color blocks
#
BOTTOM_Y = 540
TOP_Y = 240
LEFT_X = 200
RIGHT_X = 260
MID_X = (LEFT_X + RIGHT_X) // 2

def init():
    """ initialize first game or restart subsequent games """
    global match_me, guesses_left, num_guesses, lower_guess, upper_guess, t_won
    global t_upper, t_lower
    lower_guess = 0
    upper_guess = 100
    if num_range == 100:
        num_guesses = 6
    else:
        num_guesses = 9
    guesses_left = num_guesses
    print ("\nNew game.  Please enter a number between 0 and ", num_range - 1)
    print ("Number of remaining guesses is", num_guesses)
    print ( )

    # random number to guess, in range 0 to num_range - 1
    #
    match_me = random.randrange(0,num_range)
    red = canvas.create_line(100,40,100,540, fill = LIGHT_PINK, width = BAR_WIDTH)
    canvas.itemconfig(t_upper, state = 'hidden')
    canvas.itemconfig(t_lower, state = 'hidden')
    restore_color_bar()
    clear_color_bar()
    restore_color_bar()

    create_1000_color_lines()
    clear_1000_color_lines()
    if num_range == 1000:
        create_1000_color_lines()

    for i in range(6):
        canvas.create_line(LEFT_X, TOP_Y + i *50, RIGHT_X, TOP_Y + i*50, width = 2)

    # you can use the next statement for debugging, it prints the actual
    #  random number we are trying to guess if you remove the # character
    #    ... purely an optional debugging feature, ignore if you wish to
    #      check the game by just playing it but it comes in handy if you
    #        wish to make sure you are checking every number of guesses
    #
    print (match_me)


def create_1000_color_lines():
    """ extend box and colors for 0-1000 mode 'guesses left' countdown """
    global line_h1, line_h2, line_h3, line_v1, line_v2, g_left7, g_left8, g_left9

    g_left9 = canvas.create_line(MID_X,TOP_Y - 150,MID_X,TOP_Y - 100, fill = 'blue', width = 58)
    g_left8 = canvas.create_line(MID_X,TOP_Y - 100,MID_X,TOP_Y - 50, fill = ROYALBLUE, width = 58)
    g_left7 = canvas.create_line(MID_X,TOP_Y - 50,MID_X,TOP_Y, fill = SKYBLUE, width = 58)

    line_h1 = canvas.create_line(LEFT_X, TOP_Y - 150, RIGHT_X, TOP_Y - 150 , width = 2, fill = 'black')
    line_h2 = canvas.create_line(LEFT_X, TOP_Y - 100, RIGHT_X, TOP_Y - 100 , width = 2, fill = 'black')
    line_h3 = canvas.create_line(LEFT_X, TOP_Y - 50, RIGHT_X, TOP_Y - 50 , width = 2, fill = 'black')

    line_v1 = canvas.create_line(LEFT_X,TOP_Y - 150,LEFT_X,TOP_Y, width = 2, fill = 'black')
    line_v2 = canvas.create_line(RIGHT_X,TOP_Y - 150,RIGHT_X,TOP_Y, width = 2, fill = 'black')


def clear_1000_color_lines():
    """ clears the extra lines and color boxes for the 0-1000 mode 'guesses left' countdown """
    global line_h1, line_h2, line_h3, line_v1, line_v2, g_left7, g_left8, g_left9

    canvas.itemconfig(line_h1, state = 'hidden')
    canvas.itemconfig(line_h2, state = 'hidden')
    canvas.itemconfig(line_h3, state = 'hidden')
    canvas.itemconfig(line_v1, state = 'hidden')
    canvas.itemconfig(line_v2, state = 'hidden')

    canvas.itemconfig(g_left7, state = 'hidden')
    canvas.itemconfig(g_left8, state = 'hidden')
    canvas.itemconfig(g_left9, state = 'hidden')


def color_bar_guesses(num_guesses):
    """ turns off a color block when a guess is made - shows # guesses left """
    global g_left6, g_left5, y_left4, a_left3, o_left2, r_left1
    if num_guesses == 0:
        canvas.itemconfig(r_left1, state = 'hidden')
    elif num_guesses == 1:
        canvas.itemconfig(o_left2, state = 'hidden')
    elif num_guesses == 2:
        canvas.itemconfig(a_left3, state = 'hidden')
    elif num_guesses == 3:
        canvas.itemconfig(y_left4, state = 'hidden')
    elif num_guesses == 4:
        canvas.itemconfig(g_left5, state = 'hidden')
    elif num_guesses == 5:
        canvas.itemconfig(g_left6, state = 'hidden')
    elif num_guesses == 6:
        canvas.itemconfig(g_left7, state = 'hidden')
    elif num_guesses == 7:
        canvas.itemconfig(g_left8, state = 'hidden')
    elif num_guesses == 8:
        canvas.itemconfig(g_left9, state = 'hidden')


def restore_color_bar():
    """ restores color bar for tracking remaining guesses """
    global g_left6, g_left5,y_left4,a_left3,o_left2, r_left1

    g_left6 = canvas.create_line(MID_X,TOP_Y + 1, MID_X,BOTTOM_Y-1, fill = LIME, width = 58)
    g_left5 = canvas.create_line(MID_X,TOP_Y + 51, MID_X,BOTTOM_Y-1, fill = YELLOWGREEN, width = 58)
    y_left4 = canvas.create_line(MID_X,TOP_Y + 101, MID_X,BOTTOM_Y-1, fill = YELLOW, width = 58)
    a_left3 = canvas.create_line(MID_X,TOP_Y + 151, MID_X,BOTTOM_Y-1, fill = GOLD, width = 58)
    o_left2 = canvas.create_line(MID_X,TOP_Y + 201, MID_X,BOTTOM_Y-1, fill = DARKORANGE, width = 58)
    r_left1 = canvas.create_line(MID_X,TOP_Y + 250, MID_X,BOTTOM_Y-1, fill = 'red', width = 58)

def clear_color_bar():
    """ clears first 6 blocks of color bar for tracking remaining guesses """
    global g_left6, g_left5,y_left4,a_left3,o_left2, r_left1

    canvas.itemconfig(r_left1, state = 'hidden')
    canvas.itemconfig(o_left2, state = 'hidden')
    canvas.itemconfig(a_left3, state = 'hidden')
    canvas.itemconfig(y_left4, state = 'hidden')
    canvas.itemconfig(g_left5, state = 'hidden')
    canvas.itemconfig(g_left6, state = 'hidden')


def range100():
    global num_range
    num_range = 100
    clear_color_bar()
    clear_1000_color_lines()
    init()

def range1000():
    global num_range
    num_range = 1000
    clear_1000_color_lines()
    clear_color_bar()
    init()

def rb_handler():
    """ radiobutton handler ... calls range100() or range1000() """
    choice = rb_var.get()
    print (choice)
    if choice == 100:
        range100()
    else:
        range1000()

def get_input(guess):
    """ takes user's guess and compares to computer's random number"""
    global guesses_left, lower_guess, upper_guess, t_won, t_message, t_upper, t_lower
    canvas.itemconfig(t_won, state = 'hidden')
    canvas.itemconfig(t_message, state = 'hidden')

    guess = entry_box.get()
    entry_box.delete(0,END)

    # error trap on non-integer value, does not accept the input
    #
    try:
        if int(guess) < match_me:
            pass
    except ValueError:
        print ()
        print ("Input Error!  Please input an integer!")
        return

    int_guess = int(guess)

    # checks that inputs are not out of range, sets to 0 or 1000/100 if they are
    #
    if int_guess > 1000 and num_range == 1000:
        int_guess = 1000
    elif int_guess > 100 and num_range == 100:
        int_guess = 100
    elif int_guess < 0:
        int_guess = 0

    # this section handles guesses lower than the target number
    #
    if int_guess < match_me:
        guesses_left = guesses_left - 1
        color_bar_guesses(guesses_left)
        lower_guess = int_guess

        if num_range == 1000:
            lower_guess = lower_guess//10   # just for scaling the print line

        lower = canvas.create_line(100,540,100, 540 - lower_guess * 5, fill = SKYBLUE, width = BAR_WIDTH)
        canvas.itemconfig(t_lower, state = 'hidden')
        t_lower = canvas.create_text(140, 540 - lower_guess * 5 , text = str(int_guess), font = V6, anchor = 'w')

        print ("\nYour guess was", guess, ", which is too low")
        if guesses_left == 0:
            print ("\nYou used all your guesses and lost the game!")
            print ("   The number was ", match_me)
            print ( )
            message_info = "You lost!  Number =  " +  str(match_me)
            t_message = canvas.create_text(50, 590, text = message_info, font = F_HEL_12, anchor = 'sw')
            clear_1000_color_lines()
            init()
        else:
            print ("Guess again (higher).  You have", guesses_left, "guesses left")
            message_info = "Guess higher. "+ str(guesses_left) + " guesses left"
            t_message = canvas.create_text(50, 590, text = message_info, font = F_HEL_12, anchor = 'sw')

    # this section handles guesses higher than the target number
    #
    elif int_guess > match_me:
        guesses_left = guesses_left - 1
        color_bar_guesses(guesses_left)
        upper_guess = int_guess
        print ("\nYour guess was", guess, ", which is too high")
        if num_range == 1000:
            upper_guess = upper_guess//10

        upper = canvas.create_line(100,40,100,40 + 5*(100-upper_guess), fill = 'blue', width = BAR_WIDTH)
        canvas.itemconfig(t_upper, state = 'hidden')
        t_upper = canvas.create_text(60,40 + 5*(100-upper_guess) , text = str(int_guess), font = V6, anchor = 'e')

        if guesses_left == 0:
            print ("\nYou used all your guesses and lost the game!")
            print ("   The number was", match_me)
            print ( )
            message_info = "You lost!  Number =  " +  str(match_me)
            t_message = canvas.create_text(50, 590, text = message_info, font = F_HEL_12, anchor = 'sw')
            clear_1000_color_lines()
            init()
        else:
            print ("Guess again (lower).  You have", guesses_left, "guesses left")
            message_info = "Guess lower. "+ str(guesses_left) + " guesses left"
            t_message = canvas.create_text(50, 590, text = message_info, font = F_HEL_12, anchor = 'sw')

    # this section handles correct guesses
    #
    if int_guess == match_me:
        if num_guesses == guesses_left:
            print ("\nYou won in only one guess!  Great job!")
            message_won = "You won in only one guess! "
            t_won = canvas.create_text(50, 570, text = message_won, font = F_HEL_12, anchor = 'sw')
        else:
            print ("\nYou won in only", num_guesses - guesses_left + 1, "guesses!!")
            message_won = "You won in only " + str(num_guesses - guesses_left + 1) + " guesses!"
            t_won = canvas.create_text(50, 570, text = message_won, font = F_HEL_12, anchor = 'sw')
        clear_1000_color_lines()
        init()

LAB_WIDTH = 20
BOX_WIDTH = 12

top_spacing = 5      # change to increase margin at top of Canvas

# blank labels for spacing top of the Canvas
#
Lblank_top_c0 = Label(frame_spacer_c0, text=" ")
Lblank_top_c0.grid(column = 0, row = 0, pady = top_spacing)

Lblank_top_c1 = Label(frame_spacer_c1, text=" ")
Lblank_top_c1.grid(column = 0, row = 0, pady = top_spacing)

#  blank label for spacing between Frame and Canvas ... change padx to get
#    more or less spacing
#
Lblank0_vert = Label(frame1, text=" ")
Lblank0_vert.grid(column = 1, row = 2, padx = 10)

text_label = Label(frame1, text="'Guess the Number' game\n \n 6 guesses between 0-99\n 9 guesses between 0-999")
text_label.grid(column = 2, row = 0, padx = 2, pady = 2)

Lblank2 = Label(frame1, text=" ")
Lblank2.grid(column = 2, row = 1, padx = 2, pady = 2)

#  these are the old buttons used in direct translation from simplegui
#     replaced with the radio buttons
#
#b_r100 = Button(frame1, text='Range is [0,100)', command=range100, width = LAB_WIDTH, pady = 2)
#b_r100.grid(column = 2, row = 3 )

#b_r1000 = Button(frame1, text='Range is [0,1000)', command=range1000, width = LAB_WIDTH, pady = 2)
#b_r1000.grid(column = 2, row = 4)

#  radio buttons for mode choic
#
rb_var = IntVar()
rb_var.set(100)   # sets 0-100 mode active at start-up

rb_r100 = Radiobutton(frame1, text = "Range = [0,100)", width = LAB_WIDTH,
value = '100', variable = rb_var, command = rb_handler, indicatoron = 0)
rb_r100.grid(column = 2, row = 3)

rb_r1000 = Radiobutton(frame1, text = "Range = [0,1000)", width = LAB_WIDTH,
value = '1000', variable = rb_var, command = rb_handler, indicatoron = 0)
rb_r1000.grid(column = 2, row = 4)

Lblank = Label(frame1, text=" ")
Lblank.grid(column = 2, row = 5, padx = 2, pady = 2)

L_enter_guess = Label(frame1, text="Enter your guess:")
L_enter_guess.grid(column = 2, row = 6, padx = 2, pady = 2)

entry_box = Entry(frame1, width=BOX_WIDTH)
entry_box.grid(column = 2, row = 7, padx = 2, pady = 2)
entry_box.bind('<Return>', get_input)

#  blank label for spacing between Frame and Canvas ... change padx to get
#    more or less spacing
#
Lblank_vert = Label(frame1, text=" ")
Lblank_vert.grid(column = 3, row = 0, padx = 20)


# initialize various text message variables (last high guess, last low guess, general message)
#
t_lower = canvas.create_text(60,40 , text = " ", font = V6, anchor = 'e')
t_won = canvas.create_text(50, 580, text = " ", font = F_HEL_12, anchor = 'sw')
t_message = canvas.create_text(50, 590, text = " ", font = F_HEL_12, anchor = 'sw')
t_upper = canvas.create_text(60,40 , text = " ", font = V6, anchor = 'e')

# box that holds the color blocks showing remaining guesses
#
box_guesses = canvas.create_rectangle(LEFT_X, TOP_Y, RIGHT_X, BOTTOM_Y, width = 2.0)

init()
mainloop()