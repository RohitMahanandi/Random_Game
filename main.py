import sys

import pygame
from tkinter import messagebox
from sys import exit
import time
initial_xposition = 200
initial_yposition = 150
pygame.init()
game_window = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Sky Walker")
surface1 = pygame.image.load("Images/images.xcf")
surface1 = pygame.transform.scale(surface1, (600, 400))
copy_right_surface = pygame.Surface((800, 50))
copy_right_surface.fill("white")
copy_right_text = pygame.font.Font("Fonts/FiraCode-VariableFont_wght.ttf", 35)
copy_right_final = copy_right_text.render("Pygame ||  Sky Walker || Rohit", False, "Red")

score_surface = pygame.Surface((200, 400))
score_surface.fill("cyan")


frame_rate = pygame.time.Clock()

velocity = 0
velocity_x = 0
acceleration = 0.1

while True:
    main_figure = pygame.image.load("Images/main_figure_jumping.xcf")
    main_figure = pygame.transform.scale(main_figure, (50, 50))
    keys = pygame.key.get_pressed()
    for everything in pygame.event.get():
        if everything.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_w]:
            velocity = -3


        if keys[pygame.K_s]:
            velocity += 1
        if keys[pygame.K_d]:
            initial_xposition += 20
            velocity_x += 0.5
        if keys[pygame.K_a]:
            initial_xposition -= 20
            velocity_x -= 0.5

        if initial_yposition >= 348:
            messagebox.showinfo("lost", "you lost, try again")
            sys.exit()
        if initial_xposition >= 550:
            initial_xposition = 520
            velocity_x = 0
        if initial_xposition <= 0:
            initial_xposition = 50
            velocity_x = 0

    game_window.blit(surface1, (0, 0))
    game_window.blit(main_figure, (initial_xposition, initial_yposition))
    game_window.blit(score_surface, (600, 0))
    game_window.blit(copy_right_surface, (0, 400))
    game_window.blit((copy_right_final), (85, 400))


    initial_yposition += velocity
    initial_xposition += velocity_x
    velocity += acceleration

    pygame.display.update()
    frame_rate.tick(60)

