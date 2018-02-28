# Intro to Programming
# Author: Kaitlyn Stauder
# Date: 19 February, 2018

from graphics import *
win = GraphWin('Calc', 300, 500)

def calcbutton(x, y, value):
    button = Rectangle(Point(100, 0), Point(x + 100, y + 100))
    button.setFill('lightblue')
    button.draw(win)
    text = Text(Point(x + 50, y + 50), value)
    text.draw(win)
    return button

def inside(clicked, button):
    if clicked.getX() < button.p1.getX() and clicked.getX() < button.p2.getX():
            if clicked.getY() < button.p1.getY() and clicked.getY() < button.p2.getY():
                return true
            return false

    
def main():
    display = Rectangle(Point(0,0), Point(300, 100))
    display.setFill('green')
    display.draw(win)
    button1 = calcbutton(0, 100, 5)
    button2 = calcbutton(200, 100, 6)
    button3 = calcbutton(200, 100, 7)
    displayString = ''
    text = Text(Point(300 - len(displayString) * 10, 50), displayString)
    while 1==1:
        clicked = win.getMouse()
        if inside(clicked, button1):
                displayString = displayString + '5';
                text = Text(Point(300 -  len(displayString) + 10, 50), displayString)
                text.draw(win)
                button1.setFill('navy')
                button2.setFill('lightblue')
                button3.setFill('lightblue')
        if inside(clicked, button2):
                button1.setFill('ligtblue')
                button2.setFill('navy')
                button3.setFill('lightblue')
        if inside(clicked, button3):
                button1.setFill('lightblue')
                button2.setFill('lightblue')
                button3.setFill('navy')
                print(clicked.getX(), clicked.getY())

main()
