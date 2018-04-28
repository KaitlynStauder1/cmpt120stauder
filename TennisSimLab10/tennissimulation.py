# tennissimulation.py
# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 23, 2018

from simstats import SimStats
from tennismatch import Game
from tennisplayer import Player

def printIntro():
    print("This program simulates a tennis match.")

def getInputs():
    probA = float(input("Enter the probability of A: "))
    probB = float(input("Enter the probability of B: "))
    n = int(input("Number of matches to simulate: "))
    return probA, probB, n

def main():
    printIntro()
    probA, probB, n = getInputs()
    stats = SimStats()
    for i in range(n):
        theGame = Game(probA, probB)
        theGame.play()
        stats.update(theGame)
    stats.printReport()
main()
