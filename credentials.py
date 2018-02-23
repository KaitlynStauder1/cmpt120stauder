# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Kaitlyn Stauder
# Created: 2018-02-23

# Function for user to input names
def names():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last

# Function to generate a Marist-style username
def username(first, last):
    uname = first + '.' + last
    return uname

# Function for user to create a new password
def password(uname):
    passwd = input("Create a new password: ")

#Function to ensure the password has at least 8 characters
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account conifgured. Your new email address is", uname + "@marist.edu")

#Completed program
def main():
    first, last = names()
    username(first, last)
    uname = username(first, last)
    password(uname)
    
main()




    
             
    


