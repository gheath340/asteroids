import math
import pygame

class Movable:

    def __init__(self, x, y, dx, dy, world_width, world_height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mActive = True
        return

    def getActive(self):
        return self.mActive

    def setActive(self, value):
        self.mActive = value
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY
    
    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def move(self, dt):
        self.mX = self.mX + (self.mDX * dt)
        self.mY = self.mY + (self.mDY * dt)

        if self.mX >= self.mWorldWidth:
            self.mX -= self.mWorldWidth
        elif self.mX < 0.0:
            self.mX += self.mWorldWidth

        if self.mY >= self.mWorldHeight:
            self.mY -= self.mWorldHeight
        elif self.mY < 0.0:
            self.mY += self.mWorldHeight

        return

    def hits(self, other):
        center1 = pygame.math.Vector2(other.mX, other.mY)
        center2 = pygame.math.Vector2(self.mX, self.mY)
        collide = center1.distance_to(center2) <= (self.getRadius() + other.getRadius())
        if collide == True:
            return True
        return False

    def getRadius(self):
        raise NotImplementedError

    def accelerate(self, dt):
        raise NotImplementedError

    def evolve(self, dt):
        raise NotImplementedError

    def draw(self, surface):
        raise NotImplementedError