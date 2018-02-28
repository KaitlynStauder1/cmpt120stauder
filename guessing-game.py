# Introduction to Programming
# Author: Kaitlyn Stauder
# Date: 5 March, 2018


def main():
    print("The program is thinking of an animal.")
    guess = input("Guess the name of the animal: ")
    guess2 = guess.lower()
    animal = "elephant"
    stop = "q"
    y = "yes"
    n = "no"
    no = False
    while not no:
        if guess2[0] == stop:
            print("You have quit the game.")
            no = True
        elif guess2 != animal:
            print("That guess is incorrect, try again!")
            guess = input("Guess the name of the animal: ")
            guess2 = guess.lower()
        else:
            print("Congratulations! You have correctly guessed the animal!")
            no = True
            answer = input("Do you like this animal?: ")
            answer2 = answer.lower()
            if answer2 == y:
                print("That's awesome you like this animal, thanks for playing!")
            elif answer2 == n:
                print("Sorry you don't like this animal, but thanks for playing!")


main()
        
    
