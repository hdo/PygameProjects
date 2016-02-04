import pygame
import os

def create_screen():
    if os.name == "nt":
        res1 = (800, 400)
        res2 = (1280, 800)
        return pygame.display.set_mode(res2)
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
        return pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
    
pygame.init()
screen = create_screen()

done = False

font = pygame.font.Font(None, 30)
pygame.draw.circle(screen, (255,0,0), (20,20), 20, 0)
pygame.draw.circle(screen, (0,255,0), (20,50), 10, 0)
sensor0 = font.render("Haustuer", 1, (255, 255, 255))
screen.blit(sensor0, (40,12))

while not done:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    pygame.display.flip()