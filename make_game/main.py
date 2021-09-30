# 1. import pygame
import pygame
from sys import exit

# 2. initialize pygame
pygame.init()

# 3. creating a window
win = pygame.display.set_mode((800, 400))

# 7. change caption
pygame.display.set_caption("YES의 게임")

clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

my_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = my_font.render('My game', False, 'Black')

# 4. main loop
while True:
    # 5. event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    win.blit(sky_surface, (0,0)) 
    win.blit(ground_surface, (0,300)) 
    win.blit(text_surface, (330,50))
                 
    pygame.display.update()
    clock.tick(60)