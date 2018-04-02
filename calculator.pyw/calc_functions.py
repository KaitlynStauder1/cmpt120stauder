#calc_functions.py
#Introduction to Programming
#Author: Kaitlyn Stauder
#Date: February 23, 2018

# JA: For functions that take a single operand, e.g. sin, they should perform
# the calculation without waiting for "="

from graphics import *
import math

win = GraphWin('Calc', 400, 580)
displayTextElement = Text(Point(0, 50), "green")
calcGrid = [[7, 8, 9, '+', 'MC'],
            [4, 5, 6, '-', 'M+'],
            [1, 2, 3, '*', 'M-'],
            ['', 0, '(', ')', 'MR'],
            ['Mode', 'sqrt', '/', '+/-', 'MS'],
            ['%', '^2', '.', 'Del', '=']]

sciGrid = [['x^y', 'sin', 'cos', 'tan', '10^x'],
           ['log', 'sin^-1', 'cos^-1', 'tan^-1', 'ln'],
           [7, 8, 9, '+', 'MC'],
           [4, 5, 6, '-', 'M+'],
           [1, 2, 3, '*', 'M-'],
           ['', 0, '(', ')', 'MR'],
           ['Mode', 'sqrt', '/', '+/-', 'MS'],
           ['%', '^2', '.', 'Del', '=']]
    
standardButtons = [['', '', '', '', ''],
                   ['', '', '', '', ''],
                   ['', '', '', '', ''],
                   ['', '', '', '', ''],
                   ['', '', '', '', ''],
                   ['', '', '', '', '']]

sciButtons = [['', '', '', '', ''],
              ['', '', '', '', ''],
              ['', '', '', '', ''],
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

def clickedButton(clicked, buttons):
    for i in range(len(buttons)):
        for j in range(len(buttons[0])):
            if clicked.getX() > buttons[i][j].p1.getX() and clicked.getX() < buttons[i][j].p2.getX():
                if clicked.getY() > buttons[i][j].p1.getY() and clicked.getY() < buttons[i][j].p2.getY():
                    return i, j
    return -1, -1

def createStandardCalculatorButtons(buttons):
    for i in range (6):
        for j in range(5):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, calcGrid[i][j])

def createSciCalculatorButtons(buttons):
    for i in range(8):
        for j in range(5):
            buttons[i][j] = calcButton(j * 80, i * 80 + 100, sciGrid[i][j])

def get_number(op):
    if type(op) == str:
        if op =='':
            return op
        if '.' in op:
            return float(op)
        else:
            return int(op)
    return op
    
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

def xRaisedy(op1, op2):
    return op1 ** op2

def sine(op):
    return math.sin(op)

def cosine(op):
    return math.cos(op)

def tangent(op):
    return math.tan(op)

def tenRaisedx(op):
    return 10 ** op

def log(op):
    return math.log10(op)

def inversesine(op):
    return math.asin(op)
    
def inversecosine(op):
    return math.acos(op)

def inversetangent(op):
    return math.atan(op)

def naturallog(op):
    return math.log(op)

def evaluateInputString(inputString):
    while '(' in inputString:
        for i in range(len(inputString) - 1, -1, -1):
            if inputString[i] == '(':
                break
        for j in range(i + 1, len(inputString)):
            if inputString[j] == ')':
                break
        expression = inputString[i + 1:j]
        if j < len(inputString):
            inputString = inputString[:i] + evaluateExpression(expression) + inputString[j + 1:]
        else:
            inputString = inputString[:i] + evaluateExpression(expression)
    if ',' in inputString:
        return evaluateExpression(inputString)
    return inputString

def evaluateExpression(expression):
    for i in range(len(expression)):
        if expression[i] == ',':
            break
    for j in range(i + 1, len(expression)):
        if expression[j] == ',':
            break
    expression = expression.replace(',', '')
    if j != len(expression) - 1:
        j = j - 2
    if i == 0:
        operator = expression[:j + 1]
        num1 = get_number(expression[j + 1:])
        return str(evaluateSingleOpExpression(num1, operator))
    else:
        num1 = get_number(expression[:i])
    if j < len(expression) - 1:
        operator = expression[i:j + 1]
        num2 = get_number(expression[j + 1:])
        return str(evaluateMultiOpExpression(num1, num2, operator))
    else:
        operator = expression[i:]
        return str(evaluateSingleOpExpression(num1, operator))

def evaluateSingleOpExpression(number, operator):
    if operator == '+/-':
        return changeSign(number)
    elif operator == '^2':
        return square(number)
    elif operator == 'sqrt':
        return sqrt(number)
    elif operator == '%':
        return percent(number)
    elif operator == 'sin':
        return sine(number)
    elif operator == 'cos':
        return cosine(number)
    elif operator == 'tan':
        return tangent(number)
    elif operator == '10^x':
        return tenRaisedx(number)
    elif operator == 'log':
        return log(number)
    elif operator == 'sin^-1':
        return inversesine(number)
    elif operator == 'cos^-1':
        return inversecosine(number)
    elif operator == 'tan^-1':
        return inversetangent(number)
    elif operator == 'ln':
        return naturallog(number)

def evaluateMultiOpExpression(number1, number2, operator):
    if operator == '+':
        return add(number1, number2)
    elif operator == '-':
        return subtract(number1, number2)
    elif operator == '*':
        return multiply(number1, number2)
    elif operator == '/':
        return divide(number1, number2)
    elif operator == 'x^y':
        return xRaisedy(number1, number2)

def main():
    global win, calcGrid, sciGrid, standardButtons, sciButtons
    grid = calcGrid
    buttons = standardButtons
    mode = 'standard'
    createStandardCalculatorButtons(buttons)
    inputString = ''
    displayString = ''
    displayTextElement = Text(Point(0, 50), "")
    displayTextElement.draw(win)
    operators = ['+', '-', '*', '/', '+/-', '^2', 'sqrt', '%', 'x^y', 'sin', 'cos', 'tan', '10^x', 'log', 'sin^-1', 'cos^-1', 'tan^-1', 'ln']
    memoryButtons = ['MC', 'M+', 'M-', 'MR', 'MS']
    memory = 0
    previousAnswer = ''
    clearWindow = False
    while True:
        clicked = win.getMouse()
        row, col = clickedButton(clicked, buttons)
        if clearWindow:
            inputString = ''
            displayString = ''
            displayTextElement.undraw()
            displayTextElement = Text(Point(0, 50), displayString)
            displayTextElement.draw(win)
            clearWindow = False
        if row >= 0:
            userInput = grid[row][col]
            if userInput not in ['Del', '=', 'Mode'] and userInput not in memoryButtons:
                if str(userInput) in operators:
                    inputString = inputString + ',' + str(userInput) + ','
                else:
                    inputString = inputString + str(userInput)
                displayString = (displayString + str(userInput)).rjust(150)
                displayTextElement.undraw()
                displayTextElement = Text(Point(0, 50), displayString)
                displayTextElement.draw(win)
            else:
                if userInput == 'Del':
                    inputString = ''
                    displayString = ''
                    previousAnswer = ''
                    displayTextElement.undraw()
                    displayTextElement = Text(Point(0, 50), displayString)
                    displayTextElement.draw(win)
                elif userInput == '=':
                    previousAnswer = evaluateInputString(inputString)
                    displayString = previousAnswer.rjust(150)
                    displayTextElement.undraw()
                    displayTextElement = Text(Point(0, 50), displayString)
                    displayTextElement.draw(win)
                    clearWindow = True
                elif userInput in memoryButtons:
                    if userInput == 'MC':
                        inputString = ''
                        displayString = ''
                        displayTextElement.undraw()
                        displayTextElement = Text(Point(0, 50), displayString)
                        displayTextElement.draw(win)
                        memory = 0
                    elif userInput == 'MR':
                        displayTextElement.undraw()
                        displayString = str(memory).rjust(150)
                        displayTextElement = Text(Point(0, 50), displayString)
                        displayTextElement.draw(win)
                        inputString = str(memory)
                    else:
                        if inputString == '':
                            if previousAnswer != '':
                                if userInput == 'M+':
                                    memory = memory + get_number(previousAnswer)
                                elif userInput == 'M-':
                                    memory = memory + get_number(previousAnswer)
                                elif userInput == 'MS':
                                    memory = memory + get_number(previousAnswer)
                        else:
                            if userInput == 'M+':
                                memory = memory + get_number(evaluateInputString(inputString))
                            elif userInput == 'M-':
                                memory = memory - get_number(evaluateInputString(inputString))
                            elif userInput == 'MS':
                                memory = get_number(evaluateInputString(inputString))
                            displayString = str(memory).rjust(150)
                            displayTextElement.undraw()
                            displayTextElement = Text(Point(0, 50), displayString)
                            displayTextElement.draw(win)
                        inputString = str(memory)
                elif userInput == 'Mode':
                    clearWindow = True
                    if mode == 'standard':
                        grid = sciGrid
                        buttons = sciButtons
                        win.close()
                        win = GraphWin('Calc', 400, 730)
                        createSciCalculatorButtons(buttons)
                        mode = 'scientific'
                    elif mode == 'scientific':
                        grid = calcGrid
                        buttons = standardButtons
                        win.close()
                        win = GraphWin('Calc', 400, 580)
                        createStandardCalculatorButtons(buttons)
                        mode = 'standard'                       

if __name__ == '__main__':
    main()
