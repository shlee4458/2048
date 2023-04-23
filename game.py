"""
CS5001, Spring 2023
Final Project, 2048 Game
Seunghan, Lee

This file contains game class. Game class is instantiated in the 
main.py program.
"""
from board import *
from renderer import *

class Game():
    '''
    Game class contains following attributes and methods.

    Attributes 
        size: size of the board
        board: instance of a Board class. the board is mutated according
        to the user input
    
    Methods
        start: starts the game, and update the screen according to input.
        This method is called in the main.py program. 
        get_board: getter method for board instance variable
        get_size: getter method for size instance variable    
    ''' 
    def __init__(self, size) -> None:
        '''
        Constructor for Game class. In the construction stage, Board
        class will be initialized with the input size.
        '''
        self.size = size
        self.board = Board(self.size)

    def start(self):
        '''
        Starting game will pass the created board to the Renderer class.
        Rendering, and updating the user screen based on the user input
        is handled in the Renderer class.
        '''
        # Get instance variables
        board = self.get_board()

        # Instantiate Renderer class
        renderer = Renderer(board)
        renderer.initialize() # initialize the renderer instance
        board.generate() # generate a number in the matrix
        renderer.event_loop()
        renderer.render(board) # render the board
        renderer.main_loop() # start the main loop of the event listener
    
    def get_board(self):
        '''
        Get board instance variable.
        @Return Board class
        '''
        return self.board
    
    def get_size(self):
        '''
        Get size instance variable.
        @Return int size: size of the board
        '''
        return self.size