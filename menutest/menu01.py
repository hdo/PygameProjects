import pygame
import os
import SimpleMenu
    
def create_screen():
    if os.name == "nt":
        res1 = (800, 400)
        res2 = (1280, 800)
        return pygame.display.set_mode(res1)
    else:
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break
        #return pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
        return pygame.display.set_mode((800, 480))
    
pygame.init()
screen = create_screen()
clock = pygame.time.Clock()

done = False

menu = SimpleMenu.SimpleMenu(380, 400, 30)
for i in range(50):
    menu.add_item("MENU ENTRY %.3d" % i)
menu.index = 4
screen.blit(menu.get_menu(), (300,10))

dirty = True
while not done:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.dec_index()
                dirty = True
            if event.key == pygame.K_DOWN:
                menu.inc_index()
                dirty = True
            if event.key == pygame.K_ESCAPE:
                done = True
    
    
    if dirty:
        dirty = False
        screen.fill((0,0,0))
        screen.blit(menu.get_menu(), (400,50))
        pygame.display.flip()
        
    clock.tick(30)
