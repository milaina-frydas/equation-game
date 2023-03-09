import unittest
from equationgame import calculate_number



class TestCalculateNumber(unittest.TestCase):

    def test_calculate_number(self):
        # Test case 1: Check addition and subtraction
        nums_used = [1, 2, 3, 4]
        shuffled_operations = ['+', '-', '+']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual(calculate_number(nums_used, shuffled_operations, operation_options), 2)

        # Test case 2: Check multiplication and exponentiation
        nums_used = [2, 3, 4]
        shuffled_operations = ['*', '^']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual(calculate_number(nums_used, shuffled_operations, operation_options), 144)

        # Test case 3: Check all operations
        nums_used = [1, 2, 3, 4, 5]
        shuffled_operations = ['+', '-', '*', '^', '+']
        operation_options = ['+', '-', '*', '^']
        self.assertEqual(calculate_number(nums_used, shuffled_operations, operation_options), -4)

class TestCompileUserEquation(unittest.TestCase):

        def test_compile_user_equation(self):
            coordinates_clicked = [(50, 50), (150, 50), (250, 200), (350, 350)]
            nums = [1, 2, 3, 4]
            expected_output = [1, 2, 'x', '^2']

            output = compile_user_equation(coordinates_clicked, nums)
            self.assertEqual(output, expected_output)

        def test_compile_user_equation_with_operations(self):
            coordinates_clicked = [(50, 50), (150, 50), (820, 120), (350, 350)]
            nums = [1, 2, 3, 4]
            expected_output = [1, '+', 2, '^2']

            output = compile_user_equation(coordinates_clicked, nums)
            self.assertEqual(output, expected_output)

        def test_compile_user_equation_with_no_operations(self):
            coordinates_clicked = [(50, 50), (150, 50), (250, 50), (350, 50)]
            nums = [1, 2, 3, 4]
            expected_output = [1, 2, 3, 4]

            output = compile_user_equation(coordinates_clicked, nums)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()

BEGIN
running <- True
WHILE running DO
FOR event IN pygame.event.get() DO
IF event.type == pygame.QUIT THEN
running <- False
END IF
END FOR

scss
Copy code
    background <- pygame.image.load(default_image)

    screen.blit(background, (0, 0))

    # Title
    title_font <- pygame.font.Font('EraserDust.ttf', 100)
    title <- title_font.render('Equation Game', True, 'white')
    screen.blit(title, (100, 50))

    # Select Level
    level_font <- pygame.font.Font('EraserDust.ttf', 75)
    level_select_text <- level_font.render('Select Level:', True, 'white')
    screen.blit(level_select_text, (200, 200))

    button_font <- pygame.font.Font('EraserDust.ttf', 40)
    level_1_button <- button_font.render('Level 1', True, 'white')
    screen.blit(level_1_button, (350, 300))
    level_2_button <- button_font.render('Level 2', True, 'white')
    screen.blit(level_2_button, (350, 350))
    level_3_button <- button_font.render('Level 3', True, 'white')
    screen.blit(level_3_button, (350, 400))

    mouse <- pygame.mouse.get_pos()
    click <- pygame.mouse.get_pressed()

    IF 520 + 10 > mouse[0] > 520 - 10 and 322 + 10 > mouse[1] > 322 - 10 THEN
        pygame.draw.circle(screen, (191, 255, 128), (520, 322), 10.0, 0)
        IF click[0] == 1 THEN
            image <- 'chalkboard.jpg'
            level <- 1
            selected_nums <- []
            game_round(image, level, selected_nums)
            running <- False
        END IF
    ELSE
        pygame.draw.circle(screen, (255, 153, 153) , (520, 322), 10.0, 0)
    END IF

    IF 520 + 10 > mouse[0] > 520 - 10 and 372 + 10 > mouse[1] > 372 - 10 THEN
        pygame.draw.circle(screen, (191, 255, 128), (520, 372), 10.0, 0)
        IF click[0] == 1 THEN
            image <- 'chalkboard.jpg'
            level <- 2
            selected_nums <- []
            game_round(image, level, selected_nums)
            running <- False
        END IF
    ELSE
        pygame.draw.circle(screen, (255, 153, 153) , (520, 372), 10.0, 0)
    END IF

    IF 520 + 10 > mouse[0] > 520 - 10 and 422 + 10 > mouse[1] > 422 - 10 THEN
        pygame.draw.circle(screen, (191, 255, 128), (520, 422), 10.0, 0)
        IF click[0] == 1 THEN
            image <- 'chalkboard.jpg'
            level <- 3
            selected_nums <- []
            game_round(image, level, selected_nums)
            running <- False
        END IF
    ELSE
        pygame.draw.circle(screen, (255, 153, 153) , (520, 422), 10.0, 0)
    END IF

    pygame.display.update()
END WHILE
END