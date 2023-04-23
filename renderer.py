"""
CS5001, Spring 2023
Final Project, 2048 Game
Seunghan, Lee

This file contains renderer for the game, using the turtle library.
"""
import turtle
import string
from utils import *
from board import *

class Renderer():
    '''
    Renderer class is a Viewer of the game as in Model Viewer Controller model.
    Renderer will be initialized by calling initialize() method, which sets 
    up the screen to given size 

    Attributes
        screen: instance of a turtle screen object
        t: instance of a turtle instance of Turtle
        board: an instance of the Board class
        matrix: 2D int array that represents the matrix
        size: size of the matrix
        score: score to display in the screen
        status: status to display in the screen
    '''
    def __init__(self, board):
        """
        Constructor for the Renderer. Using the board instance passed in,
        assigns matrix, size, score and status variable to Renderer class'
        own instance variable.
        """
        self.screen = turtle.Screen()
        self.t = turtle.Turtle()
        self.board = board
        self.matrix = board.get_matrix()
        self.size = board.get_size()
        self.score = 0
        self.status = ""

        # Default setup
        turtle.tracer(False) # skips the drawing process
        turtle.hideturtle() # hide the turtle from the screen
        turtle.colormode(255) # set color mode to 255 instead of 1.0
        
    def initialize(self):
        '''
        Initializes the game screen. Screen will be initialized based on the size 
        of the matrix. Width will increase by 50 pixels with marginal increase in 
        the size of the matrix. Sets the color of the turtle to black and the speed
        to the fastest, and start the event loop.
        '''
        # Get instance variables
        size = self.get_size()
        t = self.get_turtle()
        screen = self.get_screen()

        # Set up the screen
        width = size * 50 + 300
        height = width + 80
        screen.setup(width, height)

        # Set up for the turtle
        t.color('black')
        t.speed('fastest')

    def event_loop(self):
        '''
        This function will set the event listener on the turtle for both valid
        and invalid key press. Valid key press includes, up/right/left/down arrow key,
        n and q key. For all valid key-press, respective function is called. For all
        other keys, function for invalid key is called. 
        '''
        valid = ["Up", "Right", "Left", "Down", "n", "q"] # define valid keys
        invalid = filter(lambda c: c not in valid, string.printable)
        for key in invalid: # add eventlistener to the invalid keys
            turtle.onkey(self.invalid, key)

        # Add eventlistener to the valid keys
        turtle.onkey(self.up, "Up")
        turtle.onkey(self.right, "Right")
        turtle.onkey(self.left, "Left")
        turtle.onkey(self.down, "Down")
        turtle.onkey(self.newgame, "n")
        turtle.onkey(self.quitgame, "q")
        turtle.listen()

    def render(self, board_inst):
        '''
        Renders the game screen. If user input is not valid, renders 
        the screen that displays message accordingly.
        @Param Board class board_inst: takes an instance of a Board class
        '''
        # Get instance variable of the input board_inst
        t = self.get_turtle()
        matrix = board_inst.get_matrix()
        score = board_inst.get_score()
        status = board_inst.get_status()
        
        # Update the screen with new values, and with the updated values
        # write text and draw matrix
        t.clear() # clear the screen
        self.update(matrix, score, status)
        self.write_text()
        self.draw_matrix()

    def write_text(self):
        '''
        Write the text on the screen. Text to be written includes;
            1) title - top mid
            2) score - top mid, below title
            3) status - top mid, below score
            4) instructions - top left and right, below status
            5) name - bottom right 
        '''
        # Get instance variables
        t = self.get_turtle()
        width = turtle.window_width()
        height = turtle.window_height()

        # Write the title
        t.penup()
        t.goto(0, height / 2 - 75)
        t.pendown()
        t.write("2048 Game", align="center", font=("Verdana", 18, "bold"))

        # Write the Score
        t.penup()
        t.goto(0, height / 2 - 105)
        t.pendown()
        t.write(f"Score : {self.get_score()}", align="center",\
                font=("Verdana", 15, "normal"))

        # Write Status
        t.penup()
        t.goto(0, height / 2 - 135)
        t.pendown()
        t.write(f"Status: {self.get_status()}", align="center",\
                font=("Verdana", 15, "normal"))

        # Write instructions
        # Write instruction for the new start
        t.pencolor('purple')
        t.penup()
        t.goto(- width / 2 + 50, height / 2 - 175)
        t.pendown()
        t.write(f"Press (n) to restart", align="left",\
                font=("Verdana", 10, "normal"))

        # Write instruction for the quitting the game
        t.penup()
        t.goto(width / 2 - 50, height / 2 - 175)
        t.pendown()
        t.write(f"Press (q) to quit", align="right",\
                font=("Verdana", 10, "normal"))
        t.pencolor('black')

        # Write name
        t.penup()
        t.goto(width / 2 - 20, - height / 2 + 20)
        t.pendown()
        t.write(f"By - Seunghan, Lee", align="right",\
                font=("Verdana", 10, "normal"))
        t.pencolor('black')

    def draw_matrix(self):
        '''
        Draw matrix by drawing a single square and moving the pen to the top right
        corner of the previous square and iterating by the size of the matrix.
        '''
        # Get instance variable of the Renderer instance
        width = turtle.window_width()
        height = turtle.window_height()
        matrix = self.get_matrix()
        t = self.get_turtle()
        size = self.get_size()

        # Draw the board
        t.penup()
        x, y = - width / 2 + 150, height / 2 - 270
        t.goto(x, y) # set initial position of the turtle

        for row in matrix: # iterate over the rows in the matrix
            for num in row: # iterate over each number in the row 
                self.draw_square(num) # draw one square given the value of the number
                x, y = x + 25, y - 35
                t.penup()
                t.goto(x, y) # move to the right of the previous square
                t.pendown()
                if num: # draw number only when number is in the cell
                    t.write(num, align="center", font=("Verdana", 15, "bold"))
                x, y = x + 25, y + 35
                t.penup()
                t.goto(x, y)
                t.pencolor((0, 0, 0))
            x, y = x - size * 50, y - 50
            t.goto(x, y) # move the pen to the next row

    def draw_square(self, num):
        '''
        Draw a single square with number in the middle of the square.
        @Param int num: value to be written inside the square. Based on the value
            different color is assigned for the background and the pen color
        '''
        t = self.get_turtle() # get turtle

        # Set up color for background and pen
        back, pen = self.get_rgb(num)
        t.fillcolor(back)

        # Draw square
        t.begin_fill() # begin fill
        t.pendown()
        for _ in range(4):
            t.forward(50)
            t.right(90)
        t.pencolor(pen)
        t.end_fill() # end fill

    def get_rgb(self, num):
        '''
        Return a tuple of r, g, b values; background color and pencolor based on 
        the input integer number. If number is not in the backcolor dictionary,
        return white color as the background color and black color as text color.
        @Param int num: number in the board
        '''
        BACKCOLOR = {2: (249, 242, 236), 4: (232, 204, 176), 8: (215, 166, 117),\
                     16: (198, 128, 57), 32: (119, 77, 34), 64: (60, 38, 17),\
                        128: (51, 51, 255), 256: (255, 77, 166), 512: (179, 0, 89),\
                            1024: (163, 102, 255), 2048: (82, 0, 204)}
        PENCOLOR = {2: (0, 0, 0), 4: (0, 0, 0), 8: (0, 0, 0), 16: (0, 0, 0),\
                    32: (0, 0, 0), 64: (242, 242, 242), 128: (255, 230, 255),\
                        256: (242, 242, 242), 512: (242, 242, 242),\
                            1024: (204, 204, 255), 2048: (240, 230, 255)}
        
        if num not in BACKCOLOR:
            return ((255, 255, 255), (0, 0, 0)) # back, pen = white, black

        return (BACKCOLOR[num], PENCOLOR[num])
     
    # Functions that are called when each key is pressed
    def event_callback(self, num):
        '''
        This method is called when each arrow key is pressed.
        @Param int num: number of rotations passed into the update method
            in the board instance. 
        '''
        board = self.get_board()
        board.update(num)
        board.generate()
        self.check_status(board)
        self.render(board)

    def up(self):
        '''
        Method called when Up arrow key is pressed.
        For up swipe, initial rotation is 1.
        '''
        self.event_callback(1)

    def right(self):
        '''
        Method called when Right arrow key is pressed.
        For right swipe, initial rotation is 0.
        '''
        self.event_callback(0)

    def left(self):
        '''
        Method called when Left arrow key is pressed.
        For left swipe, initial rotation is 2.
        '''
        self.event_callback(2)

    def down(self):
        '''
        Method called when Down arrow key is pressed.
        For down swipe, initial rotation is 3.
        '''
        self.event_callback(3)

    def invalid(self):
        '''
        This method is called when the user presses invalid keys. 
        When the method is called board status will be set to "Invalid input!".
        '''
        board = self.get_board()
        board.set_status("Invalid input!")
        self.render(board)

    def newgame(self):
        '''
        This method is called when the 'n' key is pressed. When the method is 
        called the board will be reset to empty matrix, score to 0, and the 
        status variable will be set to the "New game has started!"
        '''
        board = self.get_board()
        board.reset()
        board.set_status("New game has started!")
        self.render(board)

    def quitgame(self):
        '''
        This method is called when the user presses 'q' key. When the method is 
        called the program will be terminated.
        '''
        turtle.bye()

    def check_status(self, board):
        '''
        Check the status of the board whether the player has won the game or lost 
        game. For every user input, win and lose condition will be checked before
        rendering a new screen.
        @Param Board class board: board instance variable of the Renderer instance. 
        '''
        # Check if player has won the game
        if win(board.get_matrix()):
            board.set_status("You have won the game!")
            self.render(board)

        # Check if player has lost the game
        if not board.can_generate() and not board.can_swipe():
            board.set_status("You have lost the game!")
            self.render(board)

    def update(self, new_matrix, new_score, new_status):
        '''
        Update instance variables with given input.
        @Param int[][] new_matrix: matrix with which to update the current matrix
        @Param int new_score: score with which to update the current score
        @Param str new_status: status with which to update the current status
        '''
        self.set_matrix(new_matrix)
        self.set_score(new_score)
        self.set_status(new_status)

    def set_score(self, new_score):
        '''
        Setter method for the score instance variable.
        '''
        self.score = new_score

    def set_status(self, new_status):
        '''
        Setter method for the status instance variable.
        '''
        self.status = new_status

    def set_matrix(self, new_matrix):
        '''
        Setter method for the matrix instance variable.
        '''
        self.matrix = new_matrix

    def set_board(self, new_board):
        '''
        Setter method for the board instance variable.
        '''
        self.board = new_board

    def get_board(self):
        '''
        Getter method for the board instance variable.
        '''
        return self.board

    def get_size(self):
        '''
        Getter method for the size instance variable.
        '''
        return self.size
    
    def get_score(self):
        '''
        Getter method for the score instance variable.
        '''
        return self.score
    
    def get_status(self):
        '''
        Getter method for the status instance variable.
        '''
        return self.status
    
    def get_matrix(self):
        '''
        Getter method for the board instance variable.
        '''
        return self.matrix

    def get_turtle(self):
        '''
        Getter method for the turtle instance variable.
        '''
        return self.t
    
    def get_screen(self):
        '''
        Getter method for the screen instance variable.
        '''
        return self.screen
    
    def main_loop(self):
        '''
        Starts the turtle eventlistener mainloop. This method is 
        called in the game class.
        '''
        turtle.mainloop()