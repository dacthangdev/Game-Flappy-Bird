
from random import randint
from shutil import move
from tkinter import font
import pygame

pygame.init()
screens = pygame.display.set_mode((400,600))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()
WHITE = (255,255,255)
RED = (255,0,0)
x_bird = 50 
y_bird = 350
x_pipe1 = 400 
x_pipe2 = 600
x_pipe3 = 800
pipe_with = 50
pipe1_height = randint(100,400)
pipe2_height = randint(100,400)
pipe3_height = randint(100,400)

pipe1_pass = False
pipe2_pass = False
pipe3_pass = False

d2_pipe = 150
bird_drop_velocity = 0
gravity = 0.5
pipe_velocity = 2
score = 0
font = pygame.font.SysFont('san',20)
font1 = pygame.font.SysFont('san',30)

pausing = False

background_img = pygame.image.load('images/background.png')
background_img = pygame.transform.scale(background_img,(400,600))
bird_img = pygame.image.load('images/bird.png')
bird_img = pygame.transform.scale(bird_img,(35,35))
pipe_img = pygame.image.load('images/tube.png')
pipe_op_img = pygame.image.load('images/tube_op.png')

sand_img = pygame.image.load('images/sand.png')
sand_img = pygame.transform.scale(sand_img,(400,30))
running = True

start = False

while running:
    clock.tick(60)
    screens.fill(WHITE)
    screens.blit(background_img,(0,0))
    sand = screens.blit(sand_img,(0,570))

    pipe1_img = pygame.transform.scale(pipe_img,(pipe_with,pipe1_height))
    pipe1 = screens.blit(pipe1_img,(x_pipe1,0))
    pipe2_img = pygame.transform.scale(pipe_img,(pipe_with,pipe2_height))
    pipe2 = screens.blit(pipe2_img,(x_pipe2,0))
    pipe3_img = pygame.transform.scale(pipe_img,(pipe_with,pipe3_height))
    pipe3 = screens.blit(pipe3_img,(x_pipe3,0))


    pipe1_op_img = pygame.transform.scale(pipe_op_img,(pipe_with, 600-(pipe1_height + d2_pipe)))
    pipe1op = screens.blit(pipe1_op_img,(x_pipe1,pipe1_height+d2_pipe))
    pipe2_op_img = pygame.transform.scale(pipe_op_img,(pipe_with, 600-(pipe2_height + d2_pipe)))
    pipe2op = screens.blit(pipe2_op_img,(x_pipe2, pipe2_height+d2_pipe))
    pipe3_op_img = pygame.transform.scale(pipe_op_img,(pipe_with, 600-(pipe3_height + d2_pipe)))
    pipe3op = screens.blit(pipe3_op_img,(x_pipe3,pipe3_height+d2_pipe))

    bird = screens.blit(bird_img,(x_bird,y_bird))

    score_txt = font.render("Score:" + str(score), True, RED)
    screens.blit(score_txt,(5,5))

    if start == False:
        start_txt = font.render("Press Space to start the game!", True, RED)
        screens.blit(start_txt,(85,260))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True
    if start == True:
        # move bird
        y_bird += bird_drop_velocity
        bird_drop_velocity += gravity
        # move pipe :
        x_pipe1 -= pipe_velocity
        x_pipe2 -= pipe_velocity
        x_pipe3 -= pipe_velocity

    # new
    if x_pipe1 < -pipe_with:
        x_pipe1 = 550
        pipe1_height = randint(100,400)
        pipe1_pass = False
    if x_pipe2 < -pipe_with:
        x_pipe2 = 550
        pipe2_height = randint(100,400)
        pipe2_pass = False
    if x_pipe3 < -pipe_with:
        x_pipe3 = 550
        pipe3_height = randint(100,400)
        pipe3_pass = False

    if x_pipe1 + pipe_with <= x_bird and pipe1_pass ==False:
        pipe1_pass = True
        score += 1
    if x_pipe2 + pipe_with <= x_bird and pipe2_pass ==False:
        pipe2_pass = True
        score += 1
    if x_pipe3 + pipe_with <= x_bird and pipe3_pass ==False:
        pipe3_pass = True
        score += 1

    pipes = [pipe1, pipe2, pipe3, pipe1op,pipe2op,pipe3op,sand]
    for pipe in pipes:
        if bird.colliderect(pipe):
            pipe_velocity = 0
            bird_drop_velocity = 0
            game_txt = font1.render("Game Over, Score: "+ str(score),True,RED)
            screens.blit(game_txt,(85,260))
            space_txt = font.render("Press Space to continue!", True, RED)
            screens.blit(space_txt,(120,300))
            pausing = True
       
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
                if pausing == True:
                    x_bird = 50 
                    y_bird = 350
                    x_pipe1 = 400 
                    x_pipe2 = 600
                    x_pipe3 = 800
                    pipe_velocity = 2
                    score = 0
                    pausing = False
                    
    pygame.display.flip()
pygame.quit()    
    