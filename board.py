"""
CS5001, Spring 2023
Final Project, 2048 Game
Seunghan, Lee

This file contains implementation of Board Class.
"""
from random import *
from utils import *
from copy import deepcopy

class Board():
    '''
    Board class is the Model in MVC model. Board class includes following
    attributes and methods. 
    Attributes
        size int: size of the board
        matrix int[][]: 2d int array of input size
        status str: status to display in the renderer
        score int: score of the game 

    Methods
        create_matrix: creates a 2d array of given size with null value
        generate: randomly generates numbers, either 2 or 4 and mutate the 
            matrix
        rotate_n: rotates the board input times in place
        swipe: swipe the board from left to right
        update: updates the board using user input, called in Game class
        can_generate: return if new number can be generated in the matrix
        can_swipe: return if the board can be swiped in any of the four 
            directions
        reset: resets the board class; score to 0, matrix to empty matrix, 
            status variable to new game has started
        get_[instance variable]: get method for size, matrix, status, score 
        set_[instance variable]: set method for size, matrix, status, score 
    '''
    def __init__(self, size):
        '''
        This is the costructor for the Board class.
        '''
        self.size = size
        self.matrix = self.create_matrix(self.size)
        self.status = ""
        self.score = 0

    def create_matrix(self, size):
        '''
        Method used to create the 2D array of input size, and initiates each 
        coordinate with null value. This method is called when the Board class 
        is initially constructed, and assign the created empty matrix to the
        matrix instance variable.
        @Param int size: size of the 2d array
        @Return int[][]: 2d int array of input size
        '''
        return [[None] * size for _ in range(size)]
    
    def generate(self):
        '''
        Randomly generates number, either 2 or 4 on the empty cell of the matrix. 
        Only inputs number in the grid if there is an empty space in the grid.
        Number is randomly generated through the generate_number function in the
        utils.py file.
        @Return void: if new number can be generated, mutate the board in place
        '''
        matrix = self.get_matrix()
        num = generate_number()
        if self.can_generate():
            empty = empty_grid(matrix)
            row, col = random.choice(empty)
            matrix[row][col] = num

    def rotate_n(self, n):
        '''
        Rotate in place the board n times by 90 degress clockwise.
        @Param int n: number of times to rotate
        @Return void: rotates the board in place
        '''
        matrix = self.get_matrix()
        for _ in range(n): # rotate the board n times
            rotate(matrix) 

    def swipe(self):
        '''
        Swipes the board from left to right in place. One swipe operation
        includes sliding the matrix from left to right and merging the numbers
        that are same and sliding the matrix. Sliding a matrix will take the
        existing non-None values to the right of the matrix, leaving None values
        at the left of the matrix. Merging the matrix will, if there are cells
        with same values adjacent to each other, add the adjacent value and add
        to the right of the matrix, leaving the left of the cell as a None value.
        When a valid merge is performed, score instance variable will be updated
        by the the value of the merged cell.
        @Return void: slide and  merge will be performed in-place.
        '''
        matrix = self.get_matrix()
        score = 0

        slide(matrix) # slide the matrix to the right
        score += merge(matrix) # merge the matrix
        slide(matrix) # slide the matrix to the right

        self.add_score(score) # update the score

    def update(self, n):
        '''
        Updates the board by rotating n number of times based on the user input 
        in the Game class, and updates each rows by calling swipe method and 
        rotates back 4 - n times, back to its original position.
        @Param int n: number of times to rotate before swiping
        @Return void: mutates the board in place
        '''
        # m is the number of times to rotate after swiping
        # when it is swipe right; n == 0, no need to rotate after swipe
        keys = {0: "Right Key", 1: "Up Key", 2: "Left Key", 3: "Down Key"}
        m = 4 - n if n else 0 # if n is 0, no need to rotate after swipe
        self.rotate_n(n) # rotates the board n times
        self.swipe() # swipe the board from left to right
        self.rotate_n(m) # rotates the board m times
        self.set_status(keys[n]) # set status instance variable

    def can_generate(self):
        '''
        Checks if new number can be generated. New number can be generated
        only when there is an empty cell in the matrix
        @Return bool: return true if the board is not full, otherwise false
        '''
        return not is_full(self.get_matrix())

    def can_swipe(self):
        '''
        Checks if the user can swipe in any of the four directions. Checks by
        creating a deep copy of the matrix and checking if we can generate a
        number after swiping in four directions. If we can generate after
        performing rotation and swiping in any of the  four directions, 
        return true, otherwise false.
        @Return bool: return true if the player can swipe, otherwise false.
        '''
        matrix_copy = deepcopy(self) # make a deepcopy of the Board instance
        # we need to create a deepcopy as swipe and rotate methods mutates the
        # matrix in place.
        
        for _ in range(4): # check all four sides
            matrix_copy.rotate_n(1) # rotate one time
            matrix_copy.swipe() # swipe one time
            if matrix_copy.can_generate(): # if can be generated after swipe 
                return True # return true
        return False # return false if nothing merges in all four directions
    
    def reset(self):
        '''
        Resets board with the empty matrix and sets score to 0. This method is 
        called when user starts a new game.
        @Return void: mutates the values in-place
        '''
        self.matrix = self.create_matrix(self.get_size())
        self.score = 0

    def get_size(self):
        '''
        Return the size of the 2D array.
        @Return int: size of the Board instance
        '''
        return self.size
    
    def get_matrix(self):
        '''
        Return the matrix instance variable of the Board instance.
        @Return int[][]: matrix instance variable
        '''
        return self.matrix
    
    def get_score(self):
        '''
        Return the score instance variable of the Board instance.
        @Return int: score of the Board
        '''
        return self.score
    
    def get_status(self):
        '''
        Return the status instance variable of the Board instance.
        @Return str: status of the Board
        '''
        return self.status
    
    def set_matrix(self, new_matrix):
        '''
        Sets the matrix instance variable as the input new_matrix.
        @Param int[][] new_matrix: new 2D array of int to set as 
            the new matrix
        @Return void: mutates the matrix instance variable in-place  
        '''
        self.matrix = new_matrix
    
    def set_status(self, new_status):
        '''
        Sets the status instance variable as the input new_status.
        @Param str new_status: new status of the Board instance
        @Return void: mutates the status instance variable in-place
        '''
        self.status = new_status
    
    def add_score(self, new_score):
        '''
        Adds the score by given new_score.
        @Param int new_score: score to add to the existing score variable
        @Return void: mutates the score instance variable in-place        
        '''
        self.score += new_score