# Intro to Programming
# Author: Kaitlyn Stauder
# Date: February 6, 2018

import math

def main():
    n = int(input("Enter the number of terms to sum:"))
    series = 0
    for i in range (n):
        series = series+4*(-1)**i/(2*i+1)
        accuracy = abs(math.pi-series)
    print ("The approximate value of pi:",series)
    print ("The error in the approximation of pi:", accuracy)
main()
