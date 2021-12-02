# 1. import pygame
import pygame
from sys import exit
from random import randint

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

player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_msg = my_font.render('Press space to run', False, (111, 196, 169))
game_msg_rect = game_msg.get_rect(center = (400, 325))

enemy_timer = pygame.USEREVENT
pygame.time.set_timer(enemy_timer, 1500)

# for game variables
gameActive = True
startTime = 0

# remove snail_rect & collision detection part
enemy_rect_list = []

def display_score():
    c_time = int((pygame.time.get_ticks() - startTime)/1000)
    score_surf = my_font.render(f'SCORE: {c_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    win.blit(score_surf, score_rect)
    return c_time

# define the obstacle movement function
def enemy_movement(enmy_rct_list):
    if enmy_rct_list:  # list is not null
        for enmy_rct in enmy_rct_list:
            enmy_rct.x -= 5
            win.blit(snail_surface, enmy_rct)
        enmy_rct_list = [enmy for enmy in enmy_rct_list if enmy.right > 0]

# 4. main loop
while True:
    # 5. event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #03. make event loop code for jump
        if gameActive:
            if event.type == pygame.KEYDOWN: #키를 눌렀을 때, 뗐을 때는 KEYUP
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -25 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and player_rect.bottom == 300:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -25  
                        
            if event.type == enemy_timer:
                enemy_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                snail_rect.left = 800
                startTime = pygame.time.get_ticks()            
                       
    if gameActive:
        win.blit(sky_surface, (0,0)) 
        win.blit(ground_surface, (0,300)) 
        # win.blit(text_surface, (330,50))
        score = display_score()
        
        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # win.blit(snail_surface, snail_rect)
        
        enemy_movement(enemy_rect_list)
        
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom > 300: 
            player_rect.bottom = 300 
                 
        win.blit(player_surf, player_rect)
        
        # collision
        if player_rect.colliderect(snail_rect):
            gameActive = False 
    else:
        win.fill((94, 129, 162))
        win.blit(player_stand, player_stand_rect)            
        score_msg = my_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_msg_rect = score_msg.get_rect(center = (400, 80))
        win.blit(score_msg, score_msg_rect)
        win.blit(game_msg, game_msg_rect)
                    
    pygame.display.update()
    clock.tick(60)