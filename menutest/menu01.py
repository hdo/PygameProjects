import pygame
import os

class SimpleMenu:
    
    def __init__(self, width, height, item_height):
        self.menuitems = []
        self.index = 0
        self.width = width
        self.height = height
        self.item_height = item_height
        self.text_height = self.item_height
        self.background = (0,0,0) # black
        self.textcolor = (235, 235, 235) # white
        #self.selectedborder = (255, 255, 0) # yellow
        self.selectedborder = (0, 255, 0) # green
        self.selectedtextcolor = self.textcolor
        self.canvas = pygame.Surface((self.width, self.height))
        self.textfont = pygame.font.Font(None, self.text_height)
        
    def add_item(self, title):
        self.menuitems.append(title)

    def inc_index(self):
        if self.index < len(self.menuitems) - 1:
            self.index = self.index + 1
            
    def dec_index(self):
        if self.index > 0:
            self.index = self.index - 1
            

    def get_menu(self):
        self.canvas.fill(self.background)
        counter = 0
        for title in self.menuitems:
            sf = pygame.Surface((self.width, self.item_height))
            text = self.textfont.render(title, 1, self.textcolor)
            textpos = text.get_rect()
            textpos.centery = sf.get_rect().centery+2
            textpos.x = 5
            if self.index == counter:
                pygame.draw.rect(sf, self.selectedborder, (1,1,self.width-2, self.item_height-2), 2)
            sf.blit(text, textpos)
            self.canvas.blit(sf, (0, 10 + counter*(self.item_height)))
            counter = counter + 1
        return self.canvas
    
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
        return pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
    
pygame.init()
screen = create_screen()

done = False

def get_item(title):
    item_dim = (300, 30)
    font = pygame.font.Font(None, 30)
    text = font.render(title, 1, (255, 255, 255))
    textpos = text.get_rect()
    sf = pygame.Surface(item_dim)
    print textpos
    textpos.centery = sf.get_rect().centery+2
    textpos.x = 5
    pygame.draw.rect(sf, (255,255,0), (1,1,item_dim[0]-2, item_dim[1]-2), 2)
    sf.blit(text, textpos)
    return sf


#screen.blit(get_item("MENU ENTRY 01"), (40,10))
#screen.blit(get_item("MENU ENTRY 02"), (40,50))
#screen.blit(get_item("MENU ENTRY 03"), (40,90))
#screen.blit(get_item("MENU ENTRY 04"), (40,130))

menu = SimpleMenu(380, 400, 30)
for i in range(10):
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