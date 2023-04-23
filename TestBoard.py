"""
CS5001, Spring 2023
Final Project, 2048 Game
Seunghan, Lee

This program includes TestBoard class which implement PyUnit.
"""
import unittest
from board import *

class TestBoard(unittest.TestCase):
    """
    This class contains test cases for the features of the
    Board class.
    """
    board_one = Board(4)

    def test_create_matrix(self):
        '''
        Test create_matrix method in the Board class.
        '''
        new_board = Board(4)
        expected_matrix = [[None, None, None, None], [None, None, None, None],\
                          [None, None, None, None], [None, None, None, None]]
        actual_matrix = new_board.get_matrix()
        self.assertEqual(expected_matrix, actual_matrix)

    def test_generate(self):
        '''
        TODO: how should I test randomly generated ones
        Test generate method in the Board class.
        '''
        self.board_one.set_matrix([[1, 1, 1, 1], [1, 1, 1, None],\
                                   [1, 1, 1, 1], [1, 1, 1, 1]])
        self.board_one.generate()
        expected = [2, 4]
        actual = self.board_one.get_matrix()[1][3]
        self.assertTrue(actual in expected)

    def test_rotate_n(self):
        '''
        Test rotate_n method in the Board class.
        '''
        before_rotate = [[1, 2, 3, 4], [5, 6, 7, 8],\
                         [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board_one.set_matrix(before_rotate)
        self.board_one.rotate_n(2)
        expected_matrix = [[16, 15, 14, 13], [12, 11, 10, 9],\
                           [8, 7, 6, 5], [4, 3, 2, 1]]
        actual_matrix = self.board_one.get_matrix()
        self.assertEqual(expected_matrix, actual_matrix)

    def test_swipe(self):
        '''
        Test swipe method in the Board class.
        '''

        # Expected and Actual values
        matrix_before = [[4, 4, 4, 4], [None, None, 2, 2],\
                         [None, 2, 2, 2], [2, 4, 8, 16]]
        expected_matrix = [[None, None, 8, 8], [None, None, None, 4],\
                    [None, None, 2, 4], [2, 4, 8, 16]]
        expected_score = 24
        
        # Set board
        board = self.board_one
        board.set_matrix(matrix_before)
        curr_score = board.get_score()
        
        # Call swipe function to the board
        board.swipe() 

        # Get Actual values
        actual_matrix = board.get_matrix()
        actual_score = board.get_score() - curr_score

        # Test whether expected and actual are equal
        self.assertEqual(expected_score, actual_score)
        self.assertEqual(expected_matrix, actual_matrix)        

    def test_update(self):
        '''
        Test update method in the Board class.
        '''
        # Test swiping up - input for the rotation is 1
        matrix_before = [[4, 4, 8, None], [None, None, 4, 4],\
                         [4, 4, 4, 16], [8, 8, 8, 16]]
        expected_matrix = [[8, 8, 8, 4], [8, 8, 8, 32],\
                           [None, None, 8, None], [None, None, None, None]]
        expected_score = 56
        
        # Set board
        board = self.board_one
        board.set_matrix(matrix_before)
        curr_score = board.get_score()
        
        # Call update function to the board
        board.update(1) # for up swipe, initial rotatation is 1 

        # Get the actual values
        actual_matrix = board.get_matrix()
        actual_score = board.get_score() - curr_score

        # Compare expected and actual
        self.assertEqual(expected_matrix, actual_matrix)
        self.assertEqual(expected_score, actual_score)

    def test_can_generate(self):
        '''
        Test can_generate method in the Board class.
        '''

        # Test full matrix
        matrix_one = [[1, 2, 3, 4], [5, 6, 7, 8],\
                  [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board_one.set_matrix(matrix_one)
        self.assertFalse(self.board_one.can_generate())

        # Text matrix that is not full
        matrix_two = [[1, 2, 3, None], [5, 6, 7, 8],\
                  [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board_one.set_matrix(matrix_two)
        self.assertTrue(self.board_one.can_generate())
            
    def test_can_swipe(self):
        '''
        Test can_swipe method in the Board class.
        '''
        # Test when the player can swipe
        matrix_can = [[4, 4, 8, None], [None, None, 4, 4],\
                         [4, 4, 4, 16], [8, 8, 8, 16]]

        board = self.board_one
        board.set_matrix(matrix_can)
        self.assertTrue(board.can_swipe())
        
        # Test when the player cannot swipe
        matrix_cannot = [[1, 2, 3, 4], [5, 6, 7, 8],\
                    [9, 10, 11, 12], [13, 14, 15, 16]]
        
        board.set_matrix(matrix_cannot)
        self.assertFalse(board.can_swipe())
    
    def reset(self):
        '''
        Test reset method in the Board class.
        '''

        # Resets the Board class
        board = self.board_one
        board.reset()
        
        # Expected values
        expected_score = 0
        expected_matrix = [[None, None, None, None], [None, None, None, None],\
                           [None, None, None, None], [None, None, None, None]]
        
        # Actual values
        actual_score = board.get_score()
        actual_matrix = board.get_matrix() 

        # Compare expected and the actual value
        self.assertEqual(expected_matrix, actual_matrix)
        self.assertEqual(expected_score, actual_score)
    
    def test_set_matrix(self):
        '''
        Test set_matrix method in the Board class.
        '''
        new_matrix = [[1, 2, 3, 4], [5, 6, 7, 8],\
                      [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board_one.set_matrix(new_matrix)
        actual = self.board_one.get_matrix()
        self.assertEqual(new_matrix, actual)
    
    def test_set_status(self):
        '''
        Test set_status method in the Board class.
        '''
        new_status = "Lets get an internship this summer"
        self.board_one.set_status(new_status)
        actual = self.board_one.get_status()
        self.assertEqual(new_status, actual)
    
    def test_add_score(self):
        '''
        Test add_score method in the Board class.
        '''
        curr_score = self.board_one.get_score()
        self.board_one.add_score(4)
        expected_score = curr_score + 4
        actual_score = self.board_one.get_score()
        self.assertEqual(expected_score, actual_score)

    def test_get_size(self):
        '''
        Test get_size method in the Board class.
        '''
        expected = 4
        actual = self.board_one.get_size()
        self.assertEqual(expected, actual)
    
    def test_get_matrix(self):
        '''
        Test get_matrix method in the Board class.
        '''
        new_matrix = [[1, 2, 3, 4], [5, 6, 7, 8],\
                [9, 10, 11, 12], [13, 14, 15, 16]]
        self.board_one.set_matrix(new_matrix)
        expected = new_matrix
        actual = self.board_one.get_matrix()
        self.assertEqual(expected, actual)
    
    def test_get_score(self):
        '''
        Test get_score method in the Board class.
        '''
        curr_score = self.board_one.get_score()
        self.board_one.add_score(1)
        new_score = self.board_one.get_score()
        self.assertEqual(1, new_score - curr_score)
    
    def test_get_status(self):
        '''
        Test get_status method in the Board class.
        '''
        expected = "Boring"
        self.board_one.set_status(expected)
        actual = self.board_one.get_status()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()