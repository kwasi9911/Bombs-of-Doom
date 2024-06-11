#Name: Nana Kwasi Owusu
#Drexel id: no329
#Purpose of file: This file defines the Paddle class, a subclass of Drawable and is used to represent the paddle in the game
from drawable import Drawable
import pygame
'''
Methods in this class were authored by CS172 faculty
'''
class Paddle(Drawable):
    def __init__(self,width,height,color):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth / 2, screenHeight / 2)
        self.__color = color
        self.__width = width
        self.__height = height
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.get_rect())
        
        
    def get_rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - self.__width/2, screenHeight - 20 - (self.__height), self.__width, self.__height)
