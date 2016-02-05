import pygame
import os
import SimpleMenu

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
        #return pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
        return pygame.display.set_mode((800, 480))



def get_title(title):
    textfont = pygame.font.Font(None, 40)    
    text = textfont.render(title, 1, (200,200,200))
    return text
    
    
    
    
    
pygame.init()
screen = create_screen()

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
    current_cover = pygame.transform.scale(current_cover, (360, 360))
    cover_list.append(current_cover)
for item in sorted(os.listdir('cover')):
    fullname = os.path.join('cover',item)
    current_cover = pygame.image.load(fullname)
    current_cover = pygame.transform.scale(current_cover, (360, 360))
    cover_list.append(current_cover)

menu = SimpleMenu.SimpleMenu(380, 400, 30)
for i in range(50):
    menu.add_item("MENU ENTRY %.3d" % i)
menu.textcolor = (200,200,200)    
    


current_index = 0
dirty = True
while not gameExit:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_1:
                screen.fill((255,0,0))
            if event.key == pygame.K_2:
                screen.fill((0,255,0))
            if event.key == pygame.K_3:
                screen.fill((0,0,255))
            if event.key == pygame.K_DOWN:
                if current_index < len(cover_list)-1:
                    current_index = current_index + 1
                    menu.inc_index()
                    dirty = True
            if event.key == pygame.K_UP:
                if current_index > 0:
                    current_index = current_index -1 
                    menu.dec_index()
                    dirty = True
    if dirty:
        dirty = False
        screen.blit(menu.get_menu(), (400,60))
        new_pos = cover_list[current_index].get_rect()
        new_pos.centerx = 200
        new_pos.centery = 240
        screen.blit(cover_list[current_index], new_pos)
        screen.blit(get_title(menu.menuitems[menu.index]), (50,10))
        

    pygame.display.update()
    clock.tick(30)
    


pygame.quit()
quit()
