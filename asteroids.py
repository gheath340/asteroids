import ship
import pygame
import rock
import random
import star
import bullet
import text

class Asteroids:

    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height
        x = width / 2
        y = height / 2
        self.mShip = ship.Ship(x, y, self.mWidth, self.mHeight)
        self.mRocks = []
        self.mBullets = []
        self.mStars = []
        self.mObjects = []
        self.mScore = 0
        for i in range(10):
            x = random.randrange(width)
            y = random.randrange(height)
            rock1 = rock.Rock(x, y,self.mWidth, self.mHeight)
            self.mRocks.append(rock1)
        for obj in self.mRocks:
            self.mObjects.append(obj)
        for i in range(20):
            x = random.randrange(width)
            y = random.randrange(height)
            star1 = star.Star(x , y, width, height)
            self.mStars.append(star1)
        for obj in self.mStars:
            self.mObjects.append(obj)
        self.mObjects.append(self.mShip)
        return

    def getShip(self):
        return self.mShip

    def getStars(self):
        return self.mStars

    def getBullets(self):
        return self.mBullets

    def getRocks(self):
        return self.mRocks

    def getObjects(self):
        return self.mObjects

    def getWorldWidth(self):
        return self.mWidth

    def getWorldHeight(self):
        return self.mHeight

    def addScore(self):
        self.mScore += 100
        return

    def addRock(self):
        if len(self.mRocks) < 10:
            x = random.randrange(self.mWidth)
            y = random.randrange(self.mHeight)
            rock1 = rock.Rock(x, y,self.mWidth, self.mHeight)
            self.mRocks.append(rock1)
            self.mObjects.append(rock1)

    def fire(self):
        if len(self.mBullets) < 3:
            bullet1 = self.mShip.fire()
            self.mBullets.append(bullet1)
            self.mObjects.append(bullet1)
        return

    def evolveAllObjects(self, dt):
        for obj in self.mObjects:
            obj.evolve(dt)
        return

    def collideShipAndBullets(self):
        for bullet in self.mBullets:
            if bullet.hits(self.mShip) == True:
                bullet.setActive(False)
                self.mShip.setActive(False)
                return True
        return False

    def collideShipAndRocks(self):
        for rock in self.mRocks:
            if rock.hits(self.mShip) == True:
                rock.setActive(False)
                self.mShip.setActive(False)
                return True
        return False

    def collideRocksAndBullets(self):
        for rock in self.mRocks:
            for bullet in self.mBullets:
                if bullet.hits(rock) == True:
                    bullet.setActive(False)
                    rock.setActive(False)
                    self.addScore()
                    return True
        return False

    def removeInactiveObjects(self):
        for obj in self.mObjects:
            if obj.getActive() == False:
                if type(obj) is rock.Rock:
                    self.mRocks.remove(obj)
                    self.mObjects.remove(obj)
                if type(obj) is bullet.Bullet:
                    self.mBullets.remove(obj)
                    self.mObjects.remove(obj)
                if type(obj) is ship.Ship:
                    self.mObjects.remove(obj)
        return

    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(-delta_rotation)
        return

    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)
        return

    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)
        return

    def evolve(self, dt):
        for obj in self.mObjects:
            if obj.getActive() == True:
                obj.evolve(dt)
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.collideRocksAndBullets()
        self.removeInactiveObjects()
        if self.mShip.getActive() == True:
            self.addRock()
        return

    def draw(self, surface):
        rect = pygame.Rect(0, 0, self.mWidth, self.mHeight)
        pygame.draw.rect(surface, (0,0,0), rect)
        for obj in self.mObjects:
            if obj.getActive() == True:
                obj.draw(surface)
        x = self.mWidth - 50
        y = 50
        score = text.Text(str(self.mScore), x, y)
        if self.mShip.getActive():
            text.Text.draw(score, surface)
        if self.mShip.getActive() == False:
            for obj in self.mObjects:
                if type(obj) is rock.Rock:
                    self.mRocks.remove(obj)
                    self.mObjects.remove(obj)
                if type(obj) is bullet.Bullet:
                    self.mBullets.remove(obj)
                    self.mObjects.remove(obj)
                if type(obj) is ship.Ship:
                    self.mObjects.remove(obj)
            endText = "Game over"
            score = "Score:  " + str(self.mScore)
            x = self.mWidth / 2
            y = self.mHeight / 2
            endGame = text.Text(endText, x , y)
            endScore = text.Text(score, x, y + 50)
            text.Text.draw(endGame, surface)
            text.Text.draw(endScore, surface)
        return