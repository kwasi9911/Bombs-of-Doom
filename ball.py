#Name: Nana Kwasi Owusu
#Drexel id: no329
#Purpose of file: This file contains the ball class, a subclass of Drawable, used to represent the ball in the game
import math
import random

from drawable import Drawable
import pygame

'''
Methods in this class were authored by CS172 faculty
'''

class Ball(Drawable):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 1
        self.__ySpeed = 1

    #Draws the ball on the given surface if it is visible.
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)

    #Moves the ball according to its current speed.
    def move(self):
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed
        self.setX(newX)
        self.setY(newY)

        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1

        if newY <= self.__radius:
            self.__ySpeed *= -1

        return newY + self.__radius >= height
    
    #Returns the rectangle representing the ball's position and size.
    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius)

    #returns color of ball
    def getColor(self):
        return self.__color
    
    #sets color of ball
    def setColor(self, color):
        self.__color = color
    
    #gets radius of ball
    def getRadius(self):
        return self.__radius
    
    #sets radius of ball
    def setRadius(self, radius):
        self.__radius = radius
        
    #checks if the ball is touching another object
    def isTouchingBall(self, other):
        if isinstance(other, Ball):
            distance = math.hypot(self.getLoc()[0] - other.getLoc()[0], self.getLoc()[1] - other.getLoc()[1])
            return distance <= self.__radius + other.__radius
        elif isinstance(other, pygame.Rect):
            ball_rect = self.get_rect()
            return ball_rect.colliderect(other)
        return False

    #sets horizontal speed of the ball
    def setXSpeed(self, speed):
        self.__xSpeed = speed
    #gets horizontal speed of the ball
    def getXSpeed(self):
        return self.__xSpeed
    
    #sets vertical speed of the ball
    def setYSpeed(self, speed):
        self.__ySpeed = speed
    
    #gets vertical speed of the ball
    def getYSpeed(self):
        return self.__ySpeed
    
    #this method was authored by Nana Kwasi Owusu. Randomizes the ball's x and y speed.
    def randomize_speed(self):
        self.__xSpeed = random.randint(-3, 3)
        self.__ySpeed = random.randint(-3, 3)
        if self.__xSpeed == 0:
            self.__xSpeed = 1
        if self.__ySpeed == 0:
            self.__ySpeed = 1