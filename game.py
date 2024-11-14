import pygame
import time
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Design Challenge")
screen.fill((255,255,255))
img = pygame.image.load("glasses.jpg")
img = pygame.transform.scale(img, (1000,700))
screen.blit(img, (0,0))

pygame.font.init() 
my_font = pygame.font.SysFont('Times New Roman MS', 20)


pygame.display.flip()
while(True):
    clock.tick(60)
    
    one_surface = my_font.render('1. How are you?', False, (0, 0, 0))
    screen.blit(one_surface, (175,250))
    one_surface = my_font.render('2. Whats up?', False, (0, 0, 0))
    screen.blit(one_surface, (175,270))
    one_surface = my_font.render('3. Im doing good, how about you?', False, (0, 0, 0))
    screen.blit(one_surface, (175, 290))

    for event in pygame.event.get():

        # quit on exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()