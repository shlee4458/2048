"""
CS5001, Spring 2023
Final Project, 2048 Game
Seunghan, Lee

This file is the main entry to the game.
"""
from game import *

def main():
    '''
    Ask for user input for the size of the board.
    Size of the board has to be within 4 and 8, inclusive.
    '''
    size = int(input("Input the size of the board: "))
    while True: # ask user until the input is between 4 and 8, inclusive
        if size >= 4 and size <= 8:
            break
        else:
            size = int(input("Input number between 4 and 8, inclusive: "))

    game = Game(size) # intialize Game class with input size
    game.start() # starts the game

if __name__ == "__main__":
    main()