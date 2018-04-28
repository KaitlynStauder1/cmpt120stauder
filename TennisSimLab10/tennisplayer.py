# tennisplayer.py
# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 23, 2018

from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        self.sets = 0
        self.game = 0
        advantage = True

    def winsPoint(self): 
        return random() <= self.prob

    def resetScore(self):
        self.resetScore = 0
        self.score = self.resetScore
        return self.score

    def incScore(self): 
        if self.score == 0:
            self.score = 15
        if self.score == 15:
            self.score = 30
        if self.score == 30:
            self.score = 40

    def advantage(self):
        return self.advantage

    def unsetadvantage(self):
        self.advantage = True

    def checkadvantage(self):
        self.advantage = False
        
    def getScore(self): 
        return self.score

    def winSet(self): 
        self.sets = self.sets + 1
        return self.sets

    def getSet(self): 
        return self.sets
    
    def winGame(self): 
        self.game = self.game + 1

