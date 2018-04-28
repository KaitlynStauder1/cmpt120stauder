# tennismatch.py
# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 23, 2018

from random import *
from tennisplayer import Player

class Game:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA
        self.receiver = self.playerB

    def changeServer(self): 
        if self.server == self.playerA:
            self.server = self.playerB
            self.receiver = self.playerA
        else:
            self.server = self.playerA
            self.receiver = self.playerB

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()

    def play (self):
        if self.server.winsPoint():
            if self.server.getScore() == 40 and self.receiver.getScore() == 40:
                if self.server.checkadvantage():
                    self.server.winGame() or self.receiver.winGame()
                    if self.server.game >= 6 and self.server.game - self.receiever.game >= 2:
                        self.server.winSet()
                        self.server.resetScore()
                        self.receiver.resetScore()
                        self.changeServer()
                    elif self.receiver.checkadvantage():
                        self.receiver.unsetadvantage()
                    else:
                        self.server.advantage()
            elif self.server.getScore() == 40 and self.receiver.getScore() < 40:
                self.server.winGame()
                if self.server.game >= 6 and self.server.game - self.receiver.game >= 2:
                    self.server.winSet()
                    self.server.resetScore()
                    self.receiver.resetScore()
                    self.changeServer()
            else:
                self.server.incScore()
        else:
            self.receiver.incScore()
            if self.receiver.getScore() == 40 and self.server.getScore() < 40:
                self.receiver.winGame()
                if self.receiver.game >= 6 and self.receiver.game - self.server.game >= 2:
                    self.receiver.winSet()
                    self.server.resetScore()
                    self.receiver.resetScore()
                    self.changeServer()

