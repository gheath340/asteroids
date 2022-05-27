import polygon
import bullet

class Ship(polygon.Polygon):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, 0, 0, 0.0, width, height)
        ship_shape = [(40, 0), (-20, 20), (-20, -20)]
        self.setPolygon(ship_shape)
        return

    def fire(self):
        x1, y1 = self.mOriginalPolygon[0]
        x, y = self.rotateAndTranslatePoint(x1, y1)
        bullet1 = bullet.Bullet(x , y, self.mDX, self.mDY, self.mRotation, self.mWorldWidth, self.mWorldHeight)
        return bullet1

    def evolve(self, dt):
        self.move(dt)

        return