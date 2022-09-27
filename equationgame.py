import random
from random import randint
import pygame

# initialising pygame
pygame.init()

default_image = 'chalkboard.jpg'
# creating the screen
screen = pygame.display.set_mode((900, 600))

# title and icon
pygame.display.set_caption('Equation Game')
icon = pygame.image.load('calculator.png')
pygame.display.set_icon(icon)

# operation options
operation_options = ['+', '-', 'x', '^2']

given_level = 0


def game_round(image, level, selected_nums):
    # background
    background = pygame.image.load(image)

    # choosing the operations for the round

    quantity = randint(1, 4)
    operations = random.sample(operation_options, k=quantity)

    # choosing the numbers that will be displayed

    nums = []
    while len(nums) != 8:
        num_to_add = randint(1, 10)
        if num_to_add not in nums:
            nums.append(num_to_add)
        else:
            pass

    # shuffling the operations because im going to iterate through the list of them
    shuffled_operations = random.sample(operations, k=len(operations))

    # choosing which numbers from the displayed ones, that are going to be the ones to use, and shuffling them
    nums_used = []
    if '^2' in operations:
        nums_used = random.sample(nums, k=quantity)
    else:
        nums_used = random.sample(nums, k=(quantity + 1))

    # displaying the numbers

    font = pygame.font.Font('EraserDust.ttf', 60)
    y_pos = 100
    nums_colour = (255, 0, 0)

    def display_numbers(y):
        X = 30
        for num in nums:
            if num in selected_nums:
                num_to_display = font.render(str(num), True, 'yellow')
            else:
                num_to_display = font.render(str(num), True, nums_colour)
            screen.blit(num_to_display, (X, y))
            X += 100

    # calculator which takes an equation in the form of the list

    def calculator(list):

        print(list)

        num = list[0]

        i = 1

        for item in list:

            if item == '+':
                num += list[i]
                i += 1
            elif item == '-':
                num = num - list[i]
                i += 1
            elif item == 'x':
                num *= list[i]
                i += 1
            elif item == '^2':
                num = num ** 2
                i += 1
            else:
                i += 1

        return num

    # constructing official equation

    def construct_official_equation():
        official_equation = []

        official_equation.append(nums_used[0])
        i = 1
        for op in shuffled_operations:
            if op == '+':
                official_equation.append('+')
                official_equation.append(nums_used[i])
                i += 1
            elif op == '-':
                official_equation.append('-')
                official_equation.append(nums_used[i])
                i += 1
            elif op == 'x':
                official_equation.append('x')
                official_equation.append(nums_used[i])
                i += 1
            elif op == '^2':
                official_equation.append('^2')
            else:
                pass

        return official_equation

    def display_equation():
        string = ('')
        for item in construct_official_equation():
            string += str(item)
        thing_to_display = font.render(string, True, 'pink')
        screen.blit(thing_to_display, (100, 250))

    # shuffle icon

    def show_shuffle_icon():
        screen.blit(pygame.image.load('shuffle.png'), (820, 0))

    # calculating the aim and constructing the equation, alongside

    def calculate_number():

        aim = nums_used[0]

        i = 1

        for op in shuffled_operations:
            if operation_options.index(op) == 0:
                aim = aim + nums_used[i]
                i += 1
            elif operation_options.index(op) == 1:
                aim = aim - nums_used[i]
                i += 1
            elif operation_options.index(op) == 2:
                aim = aim * nums_used[i]
                i += 1
            elif operation_options.index(op) == 3:
                aim = aim ** 2
            else:
                pass

        return aim

    # displaying aim at the top

    textX = 380
    textY = 0

    def show_aim(x, y):
        aim_to_display = font.render(str(calculate_number()), True, 'white')
        screen.blit(aim_to_display, (x, y))

    # displaying the operations on the side

    def display_operations():
        if '+' in operations:
            screen.blit(pygame.image.load('add.png'), (820, 100))
        else:
            pass
        if '-' in operations:
            screen.blit(pygame.image.load('subtract.png'), (820, 170))
        else:
            pass
        if 'x' in operations:
            screen.blit(pygame.image.load('multiply.png'), (820, 240))
        else:
            pass
        if '^2' in operations:
            screen.blit(pygame.image.load('squared.png'), (820, 310))
        else:
            pass

    # win or loss function

    def win_or_loss(inputlist):
        if calculator(inputlist) == calculate_number():
            return True
        else:
            return False

    # function that compiles user's equation

    coordinates_clicked = []

    def compile_user_equation():
        users_equation = []
        for coordinate in coordinates_clicked:
            if coordinate[0] < 820:
                if 9 < coordinate[0] < 109:
                    users_equation.append(nums[0])
                elif 109 < coordinate[0] < 209:
                    users_equation.append(nums[1])
                elif 209 < coordinate[0] < 309:
                    users_equation.append(nums[2])
                elif 309 < coordinate[0] < 409:
                    users_equation.append(nums[3])
                elif 409 < coordinate[0] < 509:
                    users_equation.append(nums[4])
                elif 509 < coordinate[0] < 609:
                    users_equation.append(nums[5])
                elif 609 < coordinate[0] < 709:
                    users_equation.append(nums[6])
                elif 709 < coordinate[0] < 809:
                    users_equation.append(nums[7])
                else:
                    pass
            else:
                if 99 < coordinate[1] < 170:
                    users_equation.append('+')
                elif 170 < coordinate[1] < 240:
                    users_equation.append('-')
                elif 240 < coordinate[1] < 310:
                    users_equation.append('x')
                elif 310 < coordinate[1] < 380:
                    users_equation.append('^2')
                else:
                    pass

        return users_equation

    # levels
    def display_level(level):
        level_to_display = font.render(f'Level: {str(level)}', True, 'white')
        screen.blit(level_to_display, (30, 0))

    # setting boundaries

    def set_boundaries():
        if level == 0:
            boundary = 600
        elif level == 1:
            boundary = 493
        elif level == 2:
            boundary = 428
        else:
            pass
        return boundary

    # game loop
    running = True

    while running:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        y_pos += 0.03

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if (my < 100) and (mx > 800):
                    level -= 1
                    if image == 'garbage1.jpg':
                        game_round('garbage1.jpg', level, [])
                    elif image == 'chalkboard.jpg':
                        game_round('chalkboard.jpg', level, [])
                    elif image == 'garbage2.jpg':
                        game_round('garbage2.jpg', level, [])
                    else:
                        pass
                else:
                    coordinates_clicked.append([mx, my])
                    if mx < 820:
                        if 9 < mx < 109:
                            selected_nums.append(nums[0])
                        elif 109 < mx < 209:
                            selected_nums.append(nums[1])
                        elif 209 < mx < 309:
                            selected_nums.append(nums[2])
                        elif 309 < mx < 409:
                            selected_nums.append(nums[3])
                        elif 409 < mx < 509:
                            selected_nums.append(nums[4])
                        elif 509 < mx < 609:
                            selected_nums.append(nums[5])
                        elif 609 < mx < 709:
                            selected_nums.append(nums[6])
                        elif 709 < mx < 809:
                            selected_nums.append(nums[7])
                        else:
                            pass
                    else:
                        if 35 < my < 150:
                            operations.remove('+')
                        elif 150 < my < 220:
                            operations.remove('-')
                        elif 220 < my < 300:
                            operations.remove('x')
                        elif 275 < my < 400:
                            operations.remove('^2')
                        else:
                            pass

                    if len(coordinates_clicked) == len(construct_official_equation()):
                        if win_or_loss(compile_user_equation()):
                            level += 1
                            if image == 'chalkboard.jpg':
                                game_round('chalkboard.jpg', level, [])
                            elif image == 'garbage1.jpg':
                                game_round('garbage1.jpg', level, [])
                            else:
                                game_round('garbage2.jpg', level, [])
                        else:
                            if image == 'garbage1.jpg':
                                display_equation()
                                game_round('garbage2.jpg', level, [])
                            elif image == 'chalkboard.jpg':
                                display_equation()
                                game_round('garbage1.jpg', level, [])
                            else:
                                pass
            else:
                pass

        display_level(level)
        show_shuffle_icon()
        display_numbers(y_pos)
        show_aim(textX, textY)
        display_operations()
        pygame.display.update()


game_round('chalkboard.jpg', given_level, [])
