# from unittest import TestCase
#
#
# class Test(TestCase):
#     def test_calculate_number(self):
#         self.fail()

import unittest

from equationgame import game_round



class TestCalculateNumber(unittest.TestCase):

    def test_calculate_number(self):
        # Test case 1: Check addition and subtraction
        nums_used = [1, 2, 3, 4]
        shuffled_operations = ['+', '-', '+']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual(game_round.calculate_number(nums_used, shuffled_operations, operation_options), 2)

        # Test case 2: Check multiplication and exponentiation
        nums_used = [2, 3, 4]
        shuffled_operations = ['*', '^']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual(game_round.calculate_number(nums_used, shuffled_operations, operation_options), 144)

        # Test case 3: Check all operations
        nums_used = [1, 2, 3, 4, 5]
        shuffled_operations = ['+', '-', '*', '^', '+']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual(game_round.calculate_number(nums_used, shuffled_operations, operation_options), -4)


if __name__ == '__main__':
    unittest.main()
