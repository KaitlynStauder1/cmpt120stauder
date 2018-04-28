# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 27, 2018
#Display Class

from graphics import *
from button import Button

class Display:
    def __init__(self, win, p1, p2):
        self.display = Rectangle(p1, p2)
        self.display.setFill('white')
        self.display.draw(win)
        tx = p1.getX() + (p2.getX() - p1.getX())/2
        ty = p1.getY() + (p2.getY() - p1.getY())/2
        self.text = Text(Point(tx, ty), '')
        self.text.draw(win)
        self.text.setFace('courier')
        self.text.setStyle('bold')
        self.text.setSize(16)

    def setText(self, text):
        self.text.setText(text)

    def getText(self):
        return self.text.getText()

    def memorysetText(self, text):
        self.text.setText(text)

    def memorygetText(self):
        return self.text.getText()
        
        
        
    
        
