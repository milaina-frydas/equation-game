import unittest
from equationgame import game_round
from pynput.mouse import Button, Controller


class TestCalculateNumber(unittest.TestCase):

    def test_calculate_number(self):
        image = 'chalkboard.jpg'
        level = 1
        selected_nums = []
        # Test case 1: Check addition and subtraction
        nums_used = [1, 2, 3, 4]
        shuffled_operations = ['+', '-', '+']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual((game_round(image, level, selected_nums)).calculate_number(nums_used, shuffled_operations,
                                                                                    operation_options), 2)

        # Test case 2: Check multiplication and exponentiation
        nums_used = [2, 3, 4]
        shuffled_operations = ['*', '^']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual((game_round(image, level, selected_nums)).calculate_number(nums_used, shuffled_operations,
                                                                                    operation_options), 144)

        # Test case 3: Check all operations
        nums_used = [1, 2, 3, 4, 5]
        shuffled_operations = ['+', '-', '*', '^', '+']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual((game_round(image, level, selected_nums)).calculate_number(nums_used, shuffled_operations,
                                                                                    operation_options), -4)


class TestSelectedNums(unittest.TestCase):

    def test_selected_nums(self):
        game_round(image='chalkboard.jpg', level=1, selected_nums=[])

        mouse = Controller()

        mouse.position = (100, 400)
        mouse.click(Button.left, 1)

        self.assertEqual(game_round().nums[0] in game_round().selected_nums)
