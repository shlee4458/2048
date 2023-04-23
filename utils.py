"""
CS5001, Spring 2023
Final Project, 2048 Game
Seunghan, Lee

This file contains implementation of utility functions.
"""
import random

def num_rotate(dir):
    '''
    Returns number of rotations to position the original matrix to
    the position that we can swipe from left to right.
    @Param dir str: user's directional input
        'w': signifies swipe up -> rotates by 1
        'd': signifies swipe right -> rotates by 0
        'a': signifies swipe left -> rotates by 2
        's': signifies swipe down -> rotates by 3
    '''
    ROTATE = {'w': 1, 'd': 0, 'a': 2,'s': 3} # define rotate constant variable
    return ROTATE[dir]

def generate_number():
    '''
    Randomly generates numbers; either 2 or 4 that can be included
    in the empty cell of the matrix.
    @Return int: 2 or 4
    '''
    return random.choice([2, 4])

def empty_grid(matrix):
    '''
    Return array of row, column pair of empty grid in the matrix.
    @Param int[][] matrix: 2d array of int
    @Return int[][]: row and column pair of empty grid in the matrix
    '''
    row, col = len(matrix), len(matrix[0])
    res = []
    for r in range(row): # iterate over row 
        for c in range(col): # iterate over col
            if not matrix[r][c]: # if the value is None
                res.append([r, c]) # add to the res
    return res

def is_full(matrix):
    '''
    Takes 2d array and returns if every grid has a positive integer in it.
    @Param int[][] matrix: 2d Array of integer
    @Return bool: return true if all cells has number in it, else return false
    '''
    row, col = len(matrix), len(matrix[0])
    for r in range(row): # iterate over row 
        for c in range(col): # iterate over col
            if not matrix[r][c]: # if the value is None in the r, c coordinate
                return False # return false
    return True

def rotate(matrix):
    '''
    Rotate a 2d array single time clockwise by 90 degrees in place.
    @Return void: mutates the matrix in place
    '''
    l, r = 0, len(matrix) - 1 # sets l as the leftmost and r as the rightmost col
    while l < r: # iterate from the left to the right pointer
        for i in range(r - l): # iterate from 0 to r - l
            top, bottom = l, r # set top and bottom as the l and r 

            # cache the topleft
            topLeft = matrix[top][l + i] 

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft
        r -= 1 # update r pointer by 1
        l += 1 # update l pointer by 1

def slide(matrix):
    '''
    Move all the elements that has value in each row from left to right.
    For example, [None, 1, None, 2] will be mutated to [None, None, 1, 2].
    @Param int[][] board: 2D array of integers
    @Return void: mutate the matrix in place with the newRows
    '''
    size = len(matrix) # size of the matrix
    for i in range(size): # iterate over the rows
        count = 0 # count the number of non null elements in the row
        tmpRow = [] # temporary array that stores the number in the row
        for num in matrix[i]:
            if num != None:
                count += 1 # increase the count
                tmpRow.append(num) # append each non null to the tmpRow
        
        newRow = (size - count) * [None] + tmpRow # create a newRow
        matrix[i] = newRow # mutate the row of the matrix with newRow

def merge(matrix):
    '''
    Merge the elements in a row if two adjacent elements are the same.
    Merging will add the left value to the right adjacent cell and mutate
    the left cell as None and right cell with the added value. For example, 
    [4, 4, 2, 2] will be merged to [None, 8, None, 4]. After mutation, the
    sum of the merged value will be returned. For example, in the previous
    example, 12 will be returned.
    @Param int[][] matrix: 2d array of integers
    @Return int: score to be added to the Board instance variable
    '''
    score = 0
    size = len(matrix)
    changed = False # switch turned on when previous element is merged

    for row in matrix: # iterate over rows
        for i in range(size - 1, 0, -1): # Iterate from the right of the array
            # not including the element in the index 0
            if changed: # if previous cell was changed
                changed = False # update the changed variable
                continue # then continue with the loop
            else:
                if row[i] and row[i] == row[i - 1]:
                    changed = True # update changed
                    score += row[i] * 2 # update score
                    row[i] += row[i - 1] # double the cell on the right
                    row[i - 1] = None # replace left cell with none
        changed = False # Update changed to False after end of each row
    return score

def win(matrix):
    '''
    Returns true if the matrix includes 2048 in the grid, false otherwise.
    @Param int[][] matrix: the matrix of the board
    @Return bool: true if 2048 is included in the row, false otherwise.
    '''
    for row in matrix:
        if 2048 in row:
            return True
    return False