#yahtzee.py
#A game of yahtzee for 1-4 players
#By: Josh Currier

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Yahtzee")
    #title()
background_image = pygame.image.load("background.jpg").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background_image,(0,0))
    #player_number = player_count()
    #yahtzee()
    #winner_name, winner_score = score_finalizer()
#hi-score_checker()
    


    
    
