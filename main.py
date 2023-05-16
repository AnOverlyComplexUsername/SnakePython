import pygame
import random
import os  

os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 0'
pygame.init()

green = (0, 255, 0)
blue = (50, 153, 213)
red = (153, 30, 30)

dis_width = 1920
dis_height = 1080

dis = pygame.display.set_mode((dis_width, dis_height), pygame.NOFRAME)

clock = pygame.time.Clock()
my_font = pygame.font.SysFont('arial', 30)


def run():
    x1 = dis_width // 2
    y1 = dis_height // 2
    dir = [0, 0]
    snake_list = []
    snake_len = 5
    foodx = 40
    foody = 40
    rspwnTimer = 2000
    score = 0
    sqr_size = 20

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    dir = [-sqr_size, 0]
                elif event.key == pygame.K_g:
                    dir = [sqr_size, 0]
                elif event.key == pygame.K_r:
                    dir = [0, -sqr_size]
                elif event.key == pygame.K_f:
                    dir = [0, sqr_size]
                elif event.key == pygame.K_q:
                    pygame.QUIT()
        x1 += dir[0]
        y1 += dir[1]
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, sqr_size, sqr_size])
        score_surface = my_font.render("Score: " + str(score), True, (0, 0, 0))
        dis.blit(score_surface, (30, 0))

        snake_list.append([x1, y1])
        if len(snake_list) > snake_len:
            del snake_list[0]

        if ([x1, y1] in snake_list[:-1]):
            dis.fill(red)
            pygame.time.delay(rspwnTimer)
            run()

        if (x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0):
            pygame.time.delay(rspwnTimer)
            run()

        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], sqr_size, sqr_size])

        if x1 == foodx and y1 == foody:
            foodx = round(
                random.randrange(0, dis_width - sqr_size) /
                float(sqr_size)) * float(sqr_size)
            foody = round(
                random.randrange(0, dis_height - sqr_size) /
                float(sqr_size)) * float(sqr_size)
            score += 1
            snake_len += 1

        pygame.display.update()
        clock.tick(10)


run()
