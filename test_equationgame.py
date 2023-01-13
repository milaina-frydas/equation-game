# import unittest
#
from equationgame import calculate_number
#
#
#
# class TestCalculateNumber(unittest.TestCase):
#
#     def test_calculate_number(self):
#         # Test case 1: Check addition and subtraction
#         nums_used = [1, 2, 3, 4]
#         shuffled_operations = ['+', '-', '+']
#         operation_options = ['+', '-', '*', '^']
#         self.assertEqual(calculate_number(nums_used, shuffled_operations, operation_options), 2)
#
#         # Test case 2: Check multiplication and exponentiation
#         nums_used = [2, 3, 4]
#         shuffled_operations = ['*', '^']
#         operation_options = ['+', '-', '*', '^']
#         self.assertEqual(calculate_number(nums_used, shuffled_operations, operation_options), 144)
#
#         # Test case 3: Check all operations
#         nums_used = [1, 2, 3, 4, 5]
#         shuffled_operations = ['+', '-', '*', '^', '+']
#         operation_options = ['+', '-', '*', '^']
#         self.assertEqual(calculate_number(nums_used, shuffled_operations, operation_options), -4)
#
# class TestCompileUserEquation(unittest.TestCase):
#
#         def test_compile_user_equation(self):
#             coordinates_clicked = [(50, 50), (150, 50), (250, 200), (350, 350)]
#             nums = [1, 2, 3, 4]
#             expected_output = [1, 2, 'x', '^2']
#
#             output = compile_user_equation(coordinates_clicked, nums)
#             self.assertEqual(output, expected_output)
#
#         def test_compile_user_equation_with_operations(self):
#             coordinates_clicked = [(50, 50), (150, 50), (820, 120), (350, 350)]
#             nums = [1, 2, 3, 4]
#             expected_output = [1, '+', 2, '^2']
#
#             output = compile_user_equation(coordinates_clicked, nums)
#             self.assertEqual(output, expected_output)
#
#         def test_compile_user_equation_with_no_operations(self):
#             coordinates_clicked = [(50, 50), (150, 50), (250, 50), (350, 50)]
#             nums = [1, 2, 3, 4]
#             expected_output = [1, 2, 3, 4]
#
#             output = compile_user_equation(coordinates_clicked, nums)
#             self.assertEqual(output, expected_output)
#
#
# if __name__ == '__main__':
#     unittest.main()
from unittest import TestCase


class Test(TestCase):


    def test_calculate_number(self):
        def test_calculate_number(self):

            nums_used = [1, 2, 3, 4]
            shuffled_operations = ['+', '-', '+']
            operation_options = ['+', '-', '*', '^']
            self.assertEqual(calculate_number(nums_used, shuffled_operations, operation_options), 2)

        self.fail()
