#Name: Nana Kwasi Owusu
#Drexel id: no329
#Purpose of file: This file defines the Text class, a subclass of Drawable, used to display text in the game.
from drawable import Drawable
import pygame

'''
Methods in this class were authored by CS172 faculty
'''

class Text(Drawable):
    def __init__(self, message="Pygame", x=0, y=0, color=(0,0,0), size=24):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)
        
    #Draws the text on the given surface if it is visible. 
    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, True, self.__color)
        surface.blit(self.__surface, self.getLoc())
        
    #Returns the rectangle representing the text's position and size.
    def get_rect(self):
        return self.__surface.get_rect()
    
    #Sets a new message for the text object.
    def setMessage(self, message):
        self.__message = message
