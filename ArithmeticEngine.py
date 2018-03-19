# CMPT 120 - Lab 6
# Kaitlyn Stauder
# 03-19-2018
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Artihmetic Engine...")
    print("\nPlease come back again soon!")

def operands():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmdlower = cmd.lower()
        if cmdlower == "add":
            num1, num2 = operands()
            result = num1 + num2
        elif cmdlower == "sub":
            num1, num2 = operands()
            result = num1 - num2
        elif cmdlower == "mult":
            num1, num2 = operands()
            result = num1 * num2
        elif cmdlower == "div":
            num1, num2 = operands()
            result = num1 // num2
        elif cmdlower == "quit":
            break
        else:
            print(cmdlower, "is an invalid command.")
            break
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()
main()
