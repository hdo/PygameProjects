import pygame
import os


def create_screen():
    if os.name == "nt":
        return pygame.display.set_mode((800, 480))
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
gameDisplay = create_screen()

pygame.display.flip()
pygame.display.update()

clock = pygame.time.Clock()

gameExit = False

myimage = pygame.image.load('cover/0a33ca50e8c75959db94308d0240250f.png')
imagerect = myimage.get_rect()


cover_list = []
for item in sorted(os.listdir('cover')):
    fullname = os.path.join('cover',item)
    current_cover = pygame.image.load(fullname)
    cover_list.append(current_cover)


current_index = 0
while not gameExit:
    gameDisplay.blit(cover_list[current_index], cover_list[current_index].get_rect())

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_1:
                gameDisplay.fill((255,0,0))
            if event.key == pygame.K_2:
                gameDisplay.fill((0,255,0))
            if event.key == pygame.K_3:
                gameDisplay.fill((0,0,255))
            if event.key == pygame.K_UP:
                if current_index < len(cover_list)-1:
                    current_index = current_index + 1
            if event.key == pygame.K_DOWN:
                if current_index > 0:
                    current_index = current_index -1 

    pygame.display.update()
    clock.tick(30)
    


pygame.quit()
quit()
