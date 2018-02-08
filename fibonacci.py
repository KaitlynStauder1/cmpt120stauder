# Introduction to Programming
# Author: Kaitlyn Stauder
# Date: February 5, 2018

def main():
    print ("This program computes the nth Fibonacci number.")
    n = int(input("Enter a number for n:"))
    if n <= 0:
        print("Error")
    else:
        previous = 1
        current = 1
        for i in range(1, n):
            new = previous + current
            previous = current
            current = new
        print (previous)
main()



                  
    
    
