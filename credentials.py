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
# Modified to generate the username in all lowercase 
def username(first, last):
    uname = first.lower() + '.' + last.lower()
    return uname

# Function for user to create a new password
def password():
    passwd = input("Create a new password: ")
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    return passwd

#Function to ensure the password has at least 8 characters
#Additional function to check password strength and requirements
def passwordcheck(passwd, uname):
    if passwd.lower() == passwd:
        print("Password must contain both upper and lower case characters")
        passwd = input("Create a new password: ")
    if passwd.upper()==passwd:
        print("Password must contain both upper and lower case characters")
        passwd = input("Create a new password: ")
    if passwd.isalpha():
        print("This password is weak")
    else:
        print("The force is strong in this one...")
    print("Account conifgured. Your new email address is", uname + "@marist.edu")

#Completed program
def main():
    first, last = names()
    username(first, last)
    uname = username(first, last)
    passwd = password()
    passwordcheck(passwd, uname)
    
main()




    
             
    


