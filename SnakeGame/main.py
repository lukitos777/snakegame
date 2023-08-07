import pygame
import random

# create the game field
pygame.init()
# colors
black = (0, 0, 0)
red = (255, 0, 0)
cyan = (0, 100, 100)
food_color = (1, 155, 1)
field_color = (102, 255, 178)
yellow = (255, 255, 102)

field_width = 600
field_height = 400

field = pygame.display.set_mode((field_width, field_height))

pygame.display.set_caption('Snake_game_🐍')

clock = pygame.time.Clock()

game_over = False

# size of snake and food
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    val = score_font.render('Your score: ' + str(score), True, yellow)
    field.blit(val, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(field, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msg = font_style.render(msg, True, color)
    field.blit(msg, [field_width / 6, field_height / 3])


def gameLoop():
    game_over, game_close = False, False

    x1, y1 = field_width / 2, field_height / 2

    x1_change, y1_change = 0, 0

    # snake body
    snake_list = []
    lenght_of_snake = 1

    # food coordinates
    foodx = round(random.randrange(0, field_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, field_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            field.fill(field_color)
            message('you lost! Press Q-quit or C-play again', red)
            your_score(lenght_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        # condition when snake go out the barrier
        if x1 > field_width or x1 < 0 or y1 >= field_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        field.fill(field_color)
        pygame.draw.rect(field, food_color, [foodx, foody, snake_block, snake_block])
        # snake drawing
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(lenght_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, field_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, field_height - snake_block) / 10.0) * 10.0
            lenght_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == '__main__':
    gameLoop()