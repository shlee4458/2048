"""
CS5001, Spring 2023
Final Project, 2048 Game
Seunghan, Lee

This file is the test program for the functions included in the utils file.
"""
import unittest
from utils import *

class TestUtils(unittest.TestCase):
    """
    This class contains test cases for the functions in utils file.
    """
    def test_num_rotate(self):
        '''
        Tests num_rotate function in the utils file.
        '''
        # Test if num_rotate returns correct value for each input
        dir_one = 'w'
        dir_two = 'a'
        dir_three = 's'
        dir_four = 'd'
        self.assertEqual(num_rotate(dir_one), 1)
        self.assertEqual(num_rotate(dir_two), 2)
        self.assertEqual(num_rotate(dir_three), 3)
        self.assertEqual(num_rotate(dir_four), 0)

    def test_generate_number(self):
        '''
        Tests generate number function in the utils file.
        '''
        num_one = generate_number()
        num_two = generate_number()
        self.assertTrue(num_one in [2, 4])
        self.assertTrue(num_two in [2, 4])

    def test_empty_grid(self):
        '''
        Tests empty_grid function in the utils file.
        '''
        # Test when matrix is not full
        matrix_one = [[1, 2, None], [2, None, 3], [None, 1, 2]]
        expected_one = [[0, 2], [1, 1], [2, 0]]
        actual_one = empty_grid(matrix_one)
        self.assertEqual(expected_one, actual_one)

        # Test when matrix is full
        matrix_two = [[1, 2, 3], [2, 5, 3], [1, 1, 2]]
        expected_two = []
        actual_two = empty_grid(matrix_two)
        self.assertEqual(expected_two, actual_two)
        
    def test_is_full(self):
        '''
        Tests is_full function in the utils file.
        '''
        # Test full matrix
        matrix_one = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
        expected_one = True
        actual_one = is_full(matrix_one)
        self.assertEqual(expected_one, actual_one)

        # Test matrix that is not full
        matrix_two = [[1, 2, None], [1, 2, 3], [1, 2, 3]]
        expected_two = False
        actual_two = is_full(matrix_two)
        self.assertEqual(expected_two, actual_two)

    def test_rotate(self):
        '''
        Tests rotate function in the utils file.
        '''
        # Tests full matrix
        matrix_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_one = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        rotate(matrix_one)
        actual_one = matrix_one
        self.assertEqual(expected_one, actual_one)

        # Tests matrix that is not full
        matrix_two = [[None, None, None], [1, 2, None], [None, None, None]]
        expected_two = [[None, 1, None], [None, 2, None], [None, None, None]]
        rotate(matrix_two)
        actual_two = matrix_two
        self.assertEqual(expected_two, actual_two)

    def test_slide(self):
        '''
        Tests slide function in the utils file.
        '''
        matrix_one = [[1, 2, None], [4, None, 6], [None, 8, 9]]
        expected_one = [[None, 1, 2], [None, 4, 6], [None, 8, 9]]
        slide(matrix_one)
        self.assertEqual(expected_one, matrix_one)

    def test_merge(self):
        '''
        Tests merge function in the utils file.
        '''
        matrix_one = [[4, 4, 4, 4], [None, None, 2, 2], [None, 2, 2, 2], [2, 4, 8, 16]]
        expected = [[None, 8, None, 8], [None, None, None, 4], [None, 2, None, 4], [2, 4, 8, 16]]
        expected_score = 24
        actual_score = merge(matrix_one)
        self.assertEqual(matrix_one, expected) # compare the mutated matrix with expected
        self.assertEqual(expected_score, actual_score) # compare the score

    def test_win(self):
        '''
        Tests win function in the utils file.        
        '''
        # Tests board that contains 2048
        matrix_one = [[2048, 2, 4], [4, 4, 4], [128, 128, 256]]
        actual_one = win(matrix_one)

        # Tests board that does not contain 2048()
        matrix_two = [[1, 2, 4], [4, 4, 4], [128, 128, 256]]
        actual_two = win(matrix_two)

        self.assertTrue(actual_one)
        self.assertFalse(actual_two)

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()