# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 27, 2018
# Calculator Class

from graphics import *
from button import Button
import math
from displayclass import Display

operators = ['+', '-', '*', '/', '%', 'sqrt',
             '+/-', 'x^y', 'sin', 'cos', 'tan', 'x^2',
             '10^x', 'sin^-1', 'cos^-1', 'tan^-1', 'log', 'ln']

class Calculator:
    def __init__(self):
        win = GraphWin("Calculator", 400, 600)
        win.setCoords(0,0,6,8)
        win.setBackground("slategrey")
        self.win = win
        self.createButtons()
        self.createDisplay()
        self.memory = 0
        self.mode = 'standard'

    def createButtons(self):
        standard = [(1, 1, 'Mode'), (2, 1, '0'), (3, 1, '.'),
                    (1, 2, '1'), (2, 2, '2'), (3, 2, '3'), (4, 2, '+'), (5, 2, '-'),
                    (1, 3, '4'), (2, 3, '5'), (3, 3, '6'), (4, 3, '*'), (5, 3, '/'),
                    (1, 4, '7'), (2, 4, '8'), (3, 4, '9'), (4, 4, '<-'), (5, 4, 'C'),
                    (1, 5, '('), (2, 5, ')'), (3, 5, '%'), (4, 5, 'sqrt'), (5, 5, '+/-'),
                    (1, 6, 'MC'), (2, 6, 'M+'), (3, 6, 'M-'), (4, 6, 'MR'), (5, 6, 'MS')]
        self.buttons = []
        for cx, cy, label in standard:
            self.buttons.append(Button(self.win, Point(cx,cy), .75, .75, label))
        self.buttons.append(Button(self.win, Point(4.5,1), 1.75, .75, "="))
        for b in self.buttons:
            b.activate()

    def createSciButtons(self):
        scientific = [(0.5, 1, 'Mode'), (1.5, 1, '0'), (2.5, 1, '.'), (3.5, 1, 'x^y'),
                      (0.5, 2, '1'), (1.5, 2, '2'), (2.5, 2, '3'), (3.5, 2, '+'), (4.5, 2, '-'),
                      (0.5, 3, '4'), (1.5, 3, '5'), (2.5, 3, '6'), (3.5, 3, '*'), (4.5, 3, '/'),
                      (0.5, 4, '7'), (1.5, 4, '8'), (2.5, 4, '9'), (3.5, 4, '<-'), (4.5, 4, 'C'),
                      (0.5, 5, 'sin'), (1.5, 5,'cos'), (2.5, 5, 'tan'), (3.5, 5, 'x^2'), (4.5, 5, '10^x'),
                      (0.5, 6, 'sin^-1'), (1.5, 6, 'cos^-1'), (2.5, 6, 'tan^-1'), (3.5, 6, 'log'), (4.5, 6, 'ln'),
                      (0.5, 7, '('), (1.5, 7, ')'), (2.5, 7, 'sqrt'), (3.5, 7, '%'), (4.5, 7, '+/-'),
                      (0.5, 8, 'MC'), (1.5, 8, 'M+'), (2.5, 8, 'M-'), (3.5, 8, 'MR'), (4.5, 8, 'MS')]
        self.buttons = []
        for cx, cy, label in scientific:
            self.buttons.append(Button(self.win, Point(cx,cy), .75, .75, label))
        self.buttons.append(Button(self.win, Point(4.5,1), .75, .75, "="))
        for b in self.buttons:
            b.activate()

    def createDisplay(self):
        self.display = Display(self.win, Point(.5, 7.5), Point(5.5, 6.5))
 
    def createDisplay2(self):
        self.display = Display(self.win, Point(0.5, 8.5), Point(4.5, 10))

    def getButton(self):
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()

    def processButton(self, key):
        text = self.display.getText()
        clearWindow = False
        if key == 'C':
            self.display.setText('')
        elif key == '<-':
            self.display.setText(text[:-1])
        elif key == '=':
            result = evaluateInputString(text)
            self.display.setText(result)              
        elif key == 'MR':
            self.display.setText(str(self.memory))
        elif key == 'MC':
            self.memory = 0
            self.display.setText('')
        elif key == 'M+':
            if text == '':
                return
            self.memory = self.memory + eval(evaluateInputString(text))
            self.display.setText(str(self.memory))
        elif key == 'M-':
            if text == '':
                return
            self.memory = self.memory - eval(evaluateInputString(text))
            self.display.setText(str(self.memory))
        elif key == 'MS':
            if text == '':
                return
            self.memory = eval(evaluateInputString(text))
            self.display.setText(str(self.memory))
        elif key == 'Mode':
            clearWindow = True
            if self.mode == 'standard':
                self.win.close()
                win = GraphWin("Calculator", 400, 600)
                win.setCoords(0,0,5,10)
                win.setBackground("slategrey")
                self.win = win
                self.createSciButtons()
                self.createDisplay2()
                self.mode = 'scientific'
                if key == 'M+':
                    if text == '':
                        return
                    self.memory = self.memory + eval(evaluateInputString(text))
                    self.display.setText(str(self.memory))
                elif key == 'M-':
                    if text == '':
                        return
                    self.memory = self.memory - eval(evaluateInputString(text))
                    self.display.setText(str(self.memory))
                elif key == 'MS':
                    if text == '':
                        return
                    self.memory = eval(evaluateInputString(text))
                    self.display.setText(str(self.memory))
            elif self.mode == 'scientific':
                self.win.close()
                win = GraphWin("Calculator", 400, 600)
                win.setCoords(0,0,6,8)
                win.setBackground("slategrey")
                self.win = win
                self.createButtons()
                self.createDisplay()
                self.mode = 'standard'
                if key == 'M+':
                    if text == '':
                        return
                    self.memory = self.memory + eval(evaluateInputString(text))
                    self.display.setText(str(self.memory))
                elif key == 'M-':
                    if text == '':
                        return
                    self.memory = self.memory - eval(evaluateInputString(text))
                    self.display.setText(str(self.memory))
                elif key == 'MS':
                    if text == '':
                        return
                    self.memory = eval(evaluateInputString(text))
                    self.display.setText(str(self.memory))
        else:
            self.display.setText(text + key)

    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

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
    if any(operator in inputString for operator in operators):
        return evaluateExpression(inputString)
    return inputString


def evaluateExpression(expression):
    for operator in operators:
        if operator in expression:
            if operator in ('+', '-', '/'):
                if '+/-' in expression:
                    continue
            for i in range(len(expression)):
                if expression[i:i + len(operator)] == operator:
                    break
            if i == 0:
                num1 = get_number(expression[len(operator):])
                return str(evaluateSingleOpExpression(num1, operator))
            elif i == (len(expression) - len(operator)):
                num1 = get_number(expression[:i])
                return str(evaluateSingleOpExpression(num1, operator))
            else:
                num1 = get_number(expression[:i])
                num2 = get_number(expression[i + len(operator):])
                return str(evaluateMultiOpExpression(num1, num2, operator))

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




    
