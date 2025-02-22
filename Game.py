import pygame
pygame.init()

screen = pygame.display.set_mode((500,600))

GREEN = (44, 196, 5)

running=True

while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.flip()

pygame.quit()    