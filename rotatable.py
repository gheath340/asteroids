import movable
import math

class Rotatable(movable.Movable):

    def __init__(self, x, y, dx, dy, roatation, world_width, world_height):
        self.mRotation = roatation
        super().__init__(x, y, dx, dy, world_width, world_height)
        return

    def getRotation(self):
        return self.mRotation

    def rotate(self, delta_rotation):
        self.mRotation += delta_rotation
        if self.mRotation == 360:
            self.mRotation = 0
        elif self.mRotation < 0:
            while self.mRotation < 0:
                self.mRotation += 360
        elif self.mRotation > 360:
            while self.mRotation > 360:
                self.mRotation -= 360
        return self.mRotation

    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        radRotation = math.radians(rotation)
        horizontal = math.cos(radRotation) * delta_velocity
        verticle = math.sin(radRotation) * delta_velocity
        return horizontal, verticle

    def accelerate(self, delta_velocity):
        vertHorz = self.splitDeltaVIntoXAndY(self.mRotation ,delta_velocity)
        horizontal = vertHorz[0]
        verticle = vertHorz[1]
        self.mDX += horizontal
        self.mDY += verticle
        return
        
    def rotatePoint(self, x1, y1):
        theta1 = math.atan2(y1, x1)
        r1 = math.sqrt(x1 * x1 + y1 * y1)
        theta2 = theta1 + math.radians(self.mRotation)
        r2 = r1
        x2 = r2 * math.cos(theta2)
        y2 = r2 * math.sin(theta2)
        return x2, y2

    def translatePoint(self, x1, y1):
        x2 = x1 + self.mX
        y2 = y1 + self.mY
        return (x2, y2)

    def rotateAndTranslatePoint(self, x1, y1):
        x2,y2 = self.rotatePoint(x1,y1)
        return self.translatePoint(x2, y2)

    def rotateAndTranslatePointList(self, points):
        tempList = []
        for point in points:
            x1,y1 = point
            tempList.append(self.rotateAndTranslatePoint(x1, y1))
        return tempList