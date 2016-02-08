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


menu = SimpleMenu.SimpleMenu(380, 300, 30)
for i in range(50):
    menu.add_item("MENU ENTRY %.3d" % i)
menu.index = 4

submenu = SimpleMenu.SimpleMenu(380, 300, 30)
for i in range(50):
    submenu.add_item("SUBMENU ENTRY %.3d" % i)
submenu.index = 4

screen.blit(menu.get_menu(), (300,10))

done = False
dirty = True
show_menu = 1
animate_state = False
animate_dir = 1
start = 0;

print "go"
while not done:

    if animate_state:
        # ignore input on anmiation
        pygame.event.clear()
        dirty = True
        if animate_dir == 1:
            start = start + 75
            if start >= 380:
                start = 380
                animate_state = False
        if animate_dir == -1:
            start = start - 75
            if start <= 0:
                start = 0
                animate_state = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_RIGHT or event.key == pygame.K_RETURN:
                animate_dir = 1
                animate_state = True
                dirty = True
            if event.key == pygame.K_LEFT:
                animate_dir = -1
                animate_state = True
                dirty = True
            if event.key == pygame.K_ESCAPE:
                done = True
    
        
        
    if dirty or animate_state:
        dirty = False
        screen.fill((0,0,0))
        menu1 =  menu.get_menu()   
        rect_m1 = menu1.get_rect()
        menu2 = submenu.get_menu()
        rect_m2 = menu2.get_rect()   
        #screen.blit(menu1, rect_m1, (100,0,120,400))
        screen.blit(menu1, (0,0), rect_m1.clip(0+start,0,380-start,400))
        screen.blit(menu2, (380-start,0), rect_m2.clip(0,0,start,400))
        #print "updat"    
        pygame.display.flip()
        
    clock.tick(30)
