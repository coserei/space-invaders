
#from microbit import *
import time
import random

class SI:

    def __init__(self):

        self.gameStart: bool = True
        self.timeControl: int = 5
        self.score: int = 0

        self.vijandenPos: list[int] = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
        
        self.bulletPos: list[int] = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
        
        self.playerPos: list[int] = [0,0,1,0,0] 
        
        self.main()
    
    def startScherm(self):
        #if button_a.was_pressed and button_b.was_pressed:
        #    self.gameStart = True
        pass

    def playerMovement(self):
            for x in range(len(self.playerPos)):
                if False and self.playerPos[x] == 1 and not x == 0:
                    self.playerPos[x] = 0
                    self.playerPos[x-1] = 1
                elif False and self.playerPos[x] == 1 and not x == 4:
                    self.playerPos[x] = 0
                    self.playerPos[x+1] = 1
    """
    def vijandMovement(self):
        for y in range(0,5):
            for x in range(0,5):
                if self.vijandenPos[y][x] == 1:
                    self.vijandenPos[y][x] = 0
                    self.vijandenPos[y-1][x] = 1
    """

    """
    def vijandSpawn(self):
        self.enemySpawnPos: int = random.randint(0,4)
        if self.vijandenPos[self.enemySpawnPos] == 1:
            self.vijandSpawn()
        else:
            self.enemyPos[self.enemySpawnPos] = 1
    """

    """
    def spelerSchiet(self):
        for y in range(1,5):
            for x in range(0,5):
                if 1 in self.bulletPos[0]:
                    self.bulletPos[0][x] = 0
                elif self.bulletPos[y][x] == 1:
                    self.bulletPos[y][x] = 0
                    self.bulletPos[y-6][x] = 1
        print(self.bulletPos)
    """

    def addScore(self):
        self.score += 1

    def checkCollision(self):
        for y in range(0,5):
            for x in range(0,5):
                if self.bulletPos[y][x] == self.vijandenPos[y][x]:
                    print('raak')
        pass

    def checkGameOver(self):
        if 1 in self.vijandenPos[0]:
            print("Game Over")
            return True
        return False

    def gameOver(self):
        print('klaar')
        pass

    def main(self):
        while self.gameStart == True:
            print('i')
            time.sleep(3)       
            self.playerMovement()
            self.vijandMovement()
            self.spelerSchiet()
            self.checkCollision()
            if self.checkGameOver():
                self.gameOver()
                break        

spaceInvaders = SI()