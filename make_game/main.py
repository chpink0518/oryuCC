# 1. import pygame
import pygame
from sys import exit

# 2. initialize pygame
pygame.init()

# 3. creating a window
win = pygame.display.set_mode((800, 400))

# 7. change caption
pygame.display.set_caption("YES의 게임")

# 01. change icon
icon = pygame.image.load('graphics/snail_icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

my_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = my_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80, 200))

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
    
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 800
    win.blit(snail_surface, (snail_x_pos,250))
    
    win.blit(player_surf, player_rect)
                 
    pygame.display.update()
    clock.tick(60)