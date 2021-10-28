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

# background
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# font
my_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = my_font.render('My game', False, 'Black')

# snail - enemy
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

# player
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(bottomleft = (80, 300))
player_gravity = 0

# for game variables
gameActive = True

# 4. main loop
while True:
    # 5. event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #03. make event loop code for jump
        if event.type == pygame.KEYDOWN: #키를 눌렀을 때, 뗐을 때는 KEYUP
            if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                player_gravity = -25 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and player_rect.bottom == 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -25  
                    
                       
    if gameActive:
        win.blit(sky_surface, (0,0)) 
        win.blit(ground_surface, (0,300)) 
        win.blit(text_surface, (330,50))
        
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        win.blit(snail_surface, snail_rect)
        
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom > 300: 
            player_rect.bottom = 300 
                 
        win.blit(player_surf, player_rect)
        
        # collision
        if snail_rect.colliderect(player_rect):
            gameActive = False 
    else:
        win.fill((94, 129, 162))
                    
    pygame.display.update()
    clock.tick(60)