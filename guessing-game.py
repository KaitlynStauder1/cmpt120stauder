# Introduction to Programming
# Author: Kaitlyn Stauder
# Date: 5 March, 2018


def main():
    print("The program is thinking of an animal.")
    guess = input("Guess the name of the animal: ")
    animal = "elephant"
    no = False
    while not no:
        if guess != animal:
            print("That guess is incorrect, try again or if you want to quit type stop.")
            guess = input("Guess the name of the animal: ")
        else:
            print("Congratulations! You have correctly guessed the animal!")
            no = True
        
main()
        
    
