import pygame
import time
from pygame import QUIT

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Christmas Card")

img = pygame.image.load("christmas.png")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))

while(True):
    #font = pygame.font.SysFont("Times New Roman", 72)
    #text = font.render("Merry", True, (0,0,0))
    #text2 = font.render("Christmas", True, (0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    #display_surface.blit(text,(210,180))
    #display_surface.blit(text2,(180,64))
    pygame.display.update()
    time.sleep(2)

    image2 = pygame.image.load("christmas2.png")
    #font2 = pygame.font.SysFont("Arial", 36)
    #text3 = font2.render("Wisihing you a jolly christmas", True, (0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image2,(0,0))
    #display_surface.blit(text3,(30,30))
    pygame.display.update()
    time.sleep(2)

    image3 = pygame.image.load("christmas3.png")
    display_surface.fill((255,255,255))
    display_surface.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(2)

    #for event in pygame.event.get():
        #if event.type == QUIT:
            #pygame.quit()