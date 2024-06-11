#Name: Nana Kwasi Owusu
#Drexel id: no329
#Purpose of file: This file defines the abstract Drawable class, which serves as the base class for all drawable objects in the game.
from abc import ABC, abstractmethod

'''
Methods in this class were authored by CS172 faculty
'''

class Drawable(ABC):
    def __init__(self, x=0, y=0):
        self.__visible = True
        self.__x = x
        self.__y = y
       
    @abstractmethod
    def draw(self,surface):
        pass
    
    @abstractmethod
    def get_rect(self):
        pass
    
    #this getter returns a tuple of Drawable's current position
    def getLoc(self):
        return (self.__x, self.__y)
    
    #these setters allow us to specify new x and y positions for the ball
    def setX(self,x):
        self.__x = x
    
    def setY(self,y):
        self.__y = y
        
    #both methods are used to support visibility
    def isVisible(self):
        return self.__visible
    
    def setVisible(self, visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False
            
    def setLoc(self, newLoc):
        (self.__x, self.__y) = newLoc
    
    #this method checks whether two drawable objects intersect each other
    def intersects(self, other):
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
          return True
        return False
