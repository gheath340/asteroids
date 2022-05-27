import circle
import random

class Star(circle.Circle):

    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0, 0, 0, 2, world_width, world_height)
        self.mBrightness = random.randrange(0, 255)

    def getBrightness(self):
        return self.mBrightness

    def setBrightness(self, brightness):
        if brightness <= 255 and brightness >= 0:
            self.mBrightness = brightness
            self.mColor = (brightness, brightness, brightness)
        return

    def evolve(self, dt):
        list = [10, -10, 0]
        value = random.choice(list)
        newVal = self.mBrightness + value
        self.setBrightness(newVal)
        return