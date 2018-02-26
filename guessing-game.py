# Introduction to Programming
# Author: Kaitlyn Stauder
# Date: 5 March, 2018


def main():
    print("The program is thinking of an animal.")
    guess = input("Guess the name of the animal: ")
    guess2 = guess.lower()
    animal = "elephant"
    stop = "quit"
    no = False
    while not no:
        if guess2 == stop:
            print("You have quit the game.")
            no = True
        elif guess2 != animal:
            print("That guess is incorrect, try again.")
            guess = input("Guess the name of the animal: ")
            guess2 = guess.lower()
        else:
            print("Congratulations! You have correctly guessed the animal!")
            no = True
        
main()
        
    
