import pygame

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
        self.show_max = self.height / self.item_height
        #self.show_max = 5
        self.show_scope = (0, self.show_max-1)
        
    def add_item(self, title):
        self.menuitems.append(title)

    def update_scope(self):
        if self.index < self.show_scope[0]:
            # TODO add sanity check
            self.show_scope = (self.show_scope[0]-1, self.show_scope[1]-1)
        if self.index > self.show_scope[1]:
            # TODO add sanity check
            self.show_scope = (self.show_scope[0]+1, self.show_scope[1]+1)
            print self.show_scope
                

    def inc_index(self):
        if self.index < len(self.menuitems) - 1:
            self.index = self.index + 1
            self.update_scope()
            
    def dec_index(self):
        if self.index > 0:
            self.index = self.index - 1
            self.update_scope()

    def get_menu(self):
        self.canvas.fill(self.background)
        counter = 0
        for i in range(self.show_scope[0], self.show_scope[1]+1):
            title = self.menuitems[i]
        #for title in self.menuitems:
            sf = pygame.Surface((self.width, self.item_height))
            text = self.textfont.render(title, 1, self.textcolor)
            textpos = text.get_rect()
            textpos.centery = sf.get_rect().centery+2
            textpos.x = 5
            if self.index == i:
                pygame.draw.rect(sf, self.selectedborder, (1,1,self.width-2, self.item_height-2), 2)
            sf.blit(text, textpos)
            self.canvas.blit(sf, (0, 1 + counter*(self.item_height)))
            counter = counter + 1
        pygame.draw.rect(self.canvas, (255,0,0), (0, 0, self.width, self.height), 2)
        return self.canvas
