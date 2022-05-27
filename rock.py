import polygon
import random
import math

class Rock(polygon.Polygon):

    def __init__(self, x, y, world_width, world_height):
        rotation = random.uniform(0, 359.9)
        super().__init__(x, y, 0, 0, rotation, world_width, world_height)
        points = [(40, -20), (-40, 0), (20, 20), (40, 40)]
        self.setPolygon(points)
        self.mSpinRate = random.uniform(-90, 90)
        dv = random.uniform(10, 20)
        self.accelerate(dv)
        return

    def createRandomPolygon(self, radius, number_of_points):
        pointsList = []
        firstTheta = math.radians(360 / number_of_points)
        min_rad = radius * .7
        max_rad = radius * 1.3
        for i in range(number_of_points):
            theta = firstTheta * i
            radius = random.uniform(min_rad, max_rad)
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            pointsList.append((x, y))
        return pointsList

    def getSpinRate(self):
        return self.mSpinRate

    def setSpinRate(self, spin_rate):
        self.mSpinRate = spin_rate
        return

    def evolve(self, dt):
        self.rotate(self.mSpinRate * dt)
        self.move(dt)
        return


