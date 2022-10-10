import sys
import pygame
import random
from playsound import playsound

from tkinter import messagebox
from sys import exit
import time
def default_sound():
    playsound('Sounds/default_music.mp3')
    time.after(30, default_sound)
class Player:
    def __init__(self):
        self.jumpingsound = pygame.mixer.Sound("Sounds/Lost_Life.mp3")
        self.movingside = pygame.mixer.Sound("Sounds/default_music.mp3")

class Bird:
    x_position = int()
    y_position = int()
    def __init__(self):
        self.Birdtouchsound = pygame.mixer.Sound("Sounds/Lost_Life.mp3")



    def checking_collision(self, x1, y1, x_position, y_position,score):
        if x_position - 20 < x1 < x_position + 20 and y_position - 20 < y1 < y_position + 20:
            self.Birdtouchsound.play()
            writing_scores(score)
            return True
        else:
            return False


def writing_scores(scores):
    f = open("Scores.txt", "a")
    f.write(f"{str(scores)}\n")
    f.close()


def showing_score():
    f = open("Scores.txt", "r")
    reading = f.readlines()
    lists = list()
    for i in reading:
        lists.append(int(i))
    lists.sort(reverse=True)
    f.close()
    return lists


initial_xposition = 200
initial_yposition = 150
pygame.init()
game_window = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Sky Walker")
surface1 = pygame.image.load("Images/images.xcf").convert_alpha()
danger_bird = pygame.image.load("Images/Danger_bird.xcf").convert_alpha()
left_pointed_danger_bird = pygame.image.load("Images/Pointing_Left_danger_Bird.xcf")
danger_bird = pygame.transform.scale(danger_bird, (50, 50))
left_pointed_danger_bird = pygame.transform.scale(left_pointed_danger_bird, (50, 50))

surface1 = pygame.transform.scale(surface1, (600, 400))
copy_right_surface = pygame.Surface((800, 50))
copy_right_surface.fill("white")
score_text = pygame.font.Font("Fonts/FiraCode-VariableFont_wght.ttf", 20)
lives_text = pygame.font.Font("Fonts/FiraCode-VariableFont_wght.ttf", 20)
High_scores_text = pygame.font.Font("Fonts/FiraCode-VariableFont_wght.ttf", 15)
score = 0
lives = 3

copy_right_text = pygame.font.Font("Fonts/FiraCode-VariableFont_wght.ttf", 35)
copy_right_final = copy_right_text.render("Pygame ||  Sky Walker || Rohit", False, "Red")

score_surface = pygame.Surface((200, 400))
score_surface.fill("cyan")
high_score_final = High_scores_text.render(f"Top 3 High Scores", False, "Violet")

frame_rate = pygame.time.Clock()
lister = showing_score()
velocity = 0
velocity_x = 0
acceleration = 0.1
real_high_score_text = pygame.font.Font("Fonts/FiraCode-VariableFont_wght.ttf", 20)
high_score_final_scores = real_high_score_text.render(f"{lister[0:3]}", False, "violet")

y_axis_bird = [0, 25, 50, 75, 100, 125, 150]

x1 = 550
x2 = 0
y1 = random.choice(y_axis_bird)

y2 = random.choice(y_axis_bird)
jump_sound = pygame.mixer.Sound("Sounds/Jump_sound.mp3")
side_moving = pygame.mixer.Sound("Sounds/yeah-boy-114748.mp3")

while lives > 0:

    right_pointed_bird = Bird()
    left_pointed_bird = Bird()


    main_figure = pygame.image.load("Images/main_figure_jumping.xcf").convert_alpha()
    main_figure = pygame.transform.scale(main_figure, (50, 50))
    keys = pygame.key.get_pressed()

    for everything in pygame.event.get():
        if everything.type == pygame.QUIT:
            sys.exit()

        if keys[pygame.K_w]:
            jump_sound.play()
            velocity = -3
            score += 1

        if keys[pygame.K_s]:
            velocity += 1

        if keys[pygame.K_d]:
            initial_xposition += 20
            velocity_x += 0.5
            initial_yposition += 5
            side_moving.play()

        if keys[pygame.K_a]:
            initial_xposition -= 20
            velocity_x -= 0.5
            initial_yposition += 5
            side_moving.play()

        if initial_yposition >= 348:
            lives -= 1

        if initial_xposition >= 550:
            initial_xposition = 520
            velocity_x = 0

        if initial_xposition <= 0:
            initial_xposition = 50
            velocity_x = 0

    if left_pointed_bird.checking_collision(x1, y1, initial_xposition,initial_yposition,score) is True or right_pointed_bird.checking_collision(x2, y2, initial_xposition, initial_yposition,score) is True:
        messagebox.showinfo("Game over", f"Score: {score}")


        sys.exit()

    game_window.blit(surface1, (0, 0))
    game_window.blit(main_figure, (initial_xposition, initial_yposition))
    game_window.blit(danger_bird, (x1, y1))
    game_window.blit(left_pointed_danger_bird, (x2, y2))
    game_window.blit(score_surface, (600, 0))
    game_window.blit(copy_right_surface, (0, 400))

    score_final = score_text.render(f"score: {score}", False, "red")
    lives_final = lives_text.render(f"lives: {lives}", False, "Red")

    game_window.blit(copy_right_final, (85, 400))
    game_window.blit(score_final, (610, 75))
    game_window.blit(lives_final, (610, 150))
    game_window.blit(high_score_final, (610, 225))
    game_window.blit(high_score_final_scores, (610, 260))

    initial_yposition += velocity
    initial_xposition += velocity_x
    velocity += acceleration
    x1 -= 1
    x2 += 1
    pygame.display.update()
    frame_rate.tick(60)

writing_scores(score)
