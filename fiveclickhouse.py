# Five-Click House
# Intro to Programming
# Author: Kaitlyn Stauder
# Date: 12 February, 2018

import graphics

def main():
    win = graphics.GraphWin()
    # Get the two points for the house frame
    corner1 = win.getMouse()
    corner2 = win.getMouse()
    # Draw the house frame
    house = Rectangle(corner1, corner2)
    house.draw(win)
    #Get the top of the door
    door = win.getMouse()
    houseWidth = corner2.getX() - corner1.getX()
    doorWidth = houseWidth / 5
    doorCorner1 = Point(door.getX() - doorWidth / 2, door.getY())
    doorCorner2 = Point(door.getX() + doorWidth / 2, corner1.getY())
    doorFrame = Rectangle(doorCorner1, doorCorner2)
    doorFrame.draw(win)
    windowCenter = win.getMouse()
    windowWidth = doorWidth / 2
    windowCorner1 = Point(windowCenter.getX() - windowWidth / 2, windowCenter.getY() - windowWidth / 2)
    windowCorner2 = Point(Center.getX() + windowWidth / 2, windowCenter.getY() + windowWidth / 2)
    window = Rectangle(windowCorner1, windowCorner2)
    window.draw(win)
    roofTip = win.getMouse()
    houseTip = Point(corner1.getX(), corner2.getY())
    roofLine1 = Line(houseTip, roofTip)
    roofLine2 = Line(roofTip2, corner2)
    roofLine2.draw(win)

main()
                     
    




