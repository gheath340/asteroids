import pygame
import math
import rotatable

class Polygon(rotatable.Rotatable):

    def __init__(self, x, y, dx, dy, roatation, world_width, world_height):
        super().__init__(x, y, dx, dy, roatation, world_width, world_height)
        self.mOriginalPolygon = []
        self.mColor = (255, 255, 255)
        return
    
    def getPolygon(self):
        return self.mOriginalPolygon

    def getColor(self):
        return self.mColor

    def getRadius(self):
        numPoints = len(self.mOriginalPolygon)
        if numPoints == 0:
            return 0
        total = 0
        for point in self.mOriginalPolygon:
            x , y = point
            distance = math.sqrt((x * x) + (y * y))
            total += distance
        average = total / numPoints
        return average

    def setPolygon(self, point_list):
        self.mOriginalPolygon = point_list
        return

    def setColor(self, color):
        self.mColor = color
        return

    def draw(self, surface):
        tempList = self.rotateAndTranslatePointList(self.mOriginalPolygon)
        pygame.draw.polygon(surface, self.mColor, tempList)
        return