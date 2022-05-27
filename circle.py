import rotatable
import pygame

class Circle(rotatable.Rotatable):

    def __init__(self, x, y, dx, dy, roatation, radius, world_width, world_height):
        super().__init__(x, y, dx, dy, roatation, world_width, world_height)
        self.mRadius = radius
        self.mColor = (255, 255, 255)

    def getRadius(self):
        return self.mRadius

    def getColor(self):
        return self.mColor

    def setRadius(self, radius):
        if radius >= 1:
            self.mRadius = radius
        return

    def setColor(self, color):
        self.mColor = color
        return

    def draw(self, surface):
        center = (int(self.mX), int(self.mY))
        pygame.draw.circle(surface, self.mColor, center, self.mRadius)
        return
