#calc_functions.py
#Introduction to Programming
#Author: Kaitlyn Stauder
#Date: February 23, 2018

from graphics import *
import math

win = GraphWin('Calc', 400, 580)
displayTextElement = Text(Point(0, 50), "green")
calcGrid = [
    [7, 8, 9, '+', 'MC'],
    [4, 5, 6, '-', 'M+'],
    [1, 2, 3, '*', 'M-'],
    ['', 0, '', '/', 'MR'],
    ['', 'sqrt', '', '+/-', 'MS'],
    ['%', '^2', '.', 'Del', '=']
]
buttons = [['', '', '', '', ''],
           ['', '', '', '', ''],
           ['', '', '', '', ''],
           ['', '', '', '', ''],
           ['', '', '', '', ''],
           ['', '', '', '', '']]

def calcButton(x, y, value):
    button = Rectangle(Point(x, y), Point(x + 80, y + 80)) 
    button.setFill('blue')
    button.setOutline('lightblue')
    button.draw(win)
    text = Text(Point(x + 40, y + 40), value) 
    text.setTextColor('white')
    text.setSize(30)
    text.draw(win)
    return button

def inside(clicked, button):
    if clicked.getX() > button.p1.getX() and clicked.getX() < button.p2.getX():
        if clicked.getY() > button.p1.getY() and clicked.getY() < button.p2.getY():
            return True
    return False

def clickedButton(clicked):
    for i in range(6):
        for j in range(5):
            if clicked.getX() > buttons[i][j].p1.getX() and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY() and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createCalculatorButtons():
    for i in range (6):
        for j in range(5):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def get_number(op):
    if op =='':
        return op
    if '.' in op:
        return float(op)
    else:
        return int(op)
    
def add(op1, op2):
    return op1 + op2

def subtract(op1, op2):
    return op1 - op2

def multiply(op1, op2):
    return op1 * op2

def divide(op1, op2):
    return op1 / op2

def changeSign(op):
    return -1 * op

def square(op):
    return op ** 2

def sqrt(op):
    return math.sqrt(op)

def percent(op):
    return op / 100

def main():
    createCalculatorButtons()
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)
    op1 = ''
    op1Entered = False
    op2 = ''
    op2Entered = False
    opr = ''
    oprEntered = False
    operators = ['+', '-', '*', '/', '+/-', '^2', 'sqrt', '%']
    memoryButtons = ['MC', 'M+', 'M-', 'MR', 'MS']
    answer = ''
    memory = 0
    while True:
        clicked = win.getMouse()
        row, col = clickedButton(clicked)

        if row >= 0:
            userInput = calcGrid[row][col]
            if userInput == 'Del':
                displayTextElement.undraw()
                displayString = ''
                displayTextElement = Text(Point(0, 50), "")
                displayTextElement.draw(win)
                op1Entered = False
                op1 = ''
                op2Entered = False
                op2 = ''
                oprEntered = False
                answer = ''
            else:
                if userInput == '=':
                    previousInput = '='
                    op1 = get_number(op1)
                    op2 = get_number(op2)
                    if opr == '+':
                        answer = add(op1, op2)
                    elif opr == '-':
                        answer = subtract(op1, op2)
                    elif opr == '*':
                        answer = multiply(op1, op2)
                    elif opr == '/':
                        answer = divide(op1, op2)
                    elif opr == '+/-':
                        if op1Entered:
                            answer = changeSign(op1)
                        else:
                            answer = changeSign(op2)
                    elif opr == '^2':
                        if op1Entered:
                            answer = square(op1)
                        else:
                            answer = square(op2)
                    elif opr == 'sqrt':
                        if op1Entered:
                            answer = sqrt(op1)
                        else:
                            answer = sqrt(op2)
                    elif opr == '%':
                        if op1Entered:
                            answer = percent(op1)
                        else:
                            answer = percent(op2)
                    else:
                        answer = ''
                    displayTextElement.undraw()
                    displayString = str(answer).rjust(150)
                    displayTextElement = Text(Point(0, 50), displayString)
                    displayTextElement.draw(win)
                    op1 = ''
                    op1Entered = False
                    op2 = ''
                    op2Entered = False
                    opr = ''
                    oprEntered = False
                elif userInput in memoryButtons:
                    op1 = get_number(op1)
                    op2 = get_number(op2)
                    if userInput == 'MC':
                        memory = 0
                        displayTextElement.undraw()
                    elif userInput == 'MR':
                        displayTextElement.undraw()
                        displayString = str(memory).rjust(150)
                        displayTextElement = Text(Point(0, 50), displayString)
                        displayTextElement.draw(win)
                    else:
                        if userInput == 'M+':
                            if answer != '':
                                memory = add(memory, answer)
                            else:
                                if op1Entered:
                                    memory = add(memory, op1)
                                elif op2Entered:
                                    memory = add(memory, op2)
                        elif userInput == 'M-':
                            if answer != '':
                                memory = subtract(memory, answer)
                            else:
                                if op1Entered:
                                    memory = subtract(memory, op1)
                                elif op2Entered:
                                    memory = subtract(memory, op2)
                        elif userInput == 'MS':
                            if answer != '':
                                memory = answer
                            else:
                                if op1Entered:
                                    memory = op1
                                elif op2Entered:
                                    memory = op2
                        if op1Entered or op2Entered:
                            displayTextElement.undraw()
                            displayString = str(memory).rjust(150)
                            displayTextElement = Text(Point(0, 50), displayString)
                            displayTextElement.draw(win)
                    op1 = ''
                    op1Entered = False
                    op2 = ''
                    op2Entered = False
                    opr = ''
                    oprEntered = False
                else:
                    if not op1Entered and not op2Entered and not oprEntered:
                        displayTextElement.undraw()
                        displayString = ''
                        displayTextElement = Text(Point(0, 50), "")
                        displayTextElement.draw(win)
                    if userInput in operators:
                        oprEntered = True
                        opr = userInput
                    else:
                        if not oprEntered:
                            op1Entered = True
                            op1 = op1 + str(userInput)
                        else:
                            op2Entered = True
                            op2 = op2 + str(userInput)
                    buttons[row][col].setFill('lightblue')
                    displayString = (displayString + str(userInput)).rjust(150)
                    displayTextElement.undraw()
                    displayTextElement = Text(Point(0, 50), displayString)
                    displayTextElement.draw(win)

        for i in range(6):
            for j in range(5):
                if (i == row and j == col):
                    buttons[i][j].setFill('blue')        
main()
