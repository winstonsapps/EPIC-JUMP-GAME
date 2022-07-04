
import pygame, sys as sus # AMOGUS
import os # useful for paths


"""pygame setup"""
pygame.init() # initliazes pygame
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.SCALED) # creates window
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

"""colours"""
white = (255,255,255) # or pygame.Color("white")
black = (0,0,0)
"""loading assets"""
big_font = pygame.font.Font(os.path.join('assets','PressStart2P-Regular.ttf'), 40)
start_img = pygame.image.load(os.path.join('assets', 'start.png')).convert_alpha()
start_img = pygame.transform.scale(start_img, (80,80))
settings_img = pygame.image.load(os.path.join('assets', 'settings.png')).convert_alpha()
settings_img = pygame.transform.scale(settings_img, (80,80))
"""misc setup"""
menu = 'start' # start, settings, or game
clock = pygame.time.Clock()
"""title screen"""
start = pygame.Rect((width/4, height/2), (80,80))
settings = pygame.Rect((width - width/4 - 80, height/2), (80,80))
"""main loop"""
while True:
    for event in pygame.event.get(): # event handler
        if event.type == pygame.QUIT:
            pygame.quit()
            sus.exit() # fixes a error
        if event.type == pygame.MOUSEBUTTONDOWN and menu == 'start':
            if start.collidepoint(event.pos): # checks if the click is in the start button
                menu = 'playing'
    # graphchis # it's intentional
    screen.fill(black)
    if menu == 'start': # start menu
        screen.blit(big_font.render("EPIC JUMP GAME", False,  white), (40, 40))
        screen.blit(start_img, start)
        screen.blit(settings_img, settings)
        
    

    pygame.display.update() # does exactly what u think it does: updates the display you dum dum
    clock.tick(30)