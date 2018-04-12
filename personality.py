# personality.py
# Intro to Programming
# Author: Kaitlyn Stauder
# Date: April 9, 2018

#rows 0-5 and cols 0-3
grid = [[0, 0, 1, 1],
        [0, 0, 2, 0],
        [1, 0, 2, 5],
        [3, 4, 2, 3],
        [3, 4, 2, 3],
        [4, 0, 1, 5]]

def getInteraction():
    userAction = int(input("Enter an action:"))
    return userAction

def lookupEmotion(currEmotion, userAction):
    i = currEmotion
    j = userAction
    result = grid[i][j]
    if result == 0:
        print("You're making me angry!")
        return 0       
    elif result == 1:
        print("I am disgusted!")
        return 1       
    elif result == 2:
        print("You're scaring me!")
        return 2       
    elif result == 3:
        print("I am happy!")
        return 3       
    elif result == 4:
        print("I am upset!")
        return 4           
    elif result == 5:
        print("You suprised me!")
        return 5

def main():
    print("This is an Artificial Personlity Program!")
    print("Enter an emotion and the AI program with respond to you.")
    print("Enter the number that corresponds with the emotion you want to use: \n"
          "0. Reward,  1.Punish,  2. Threaten,  3. Joke.")
    currEmotion = 3
    while True:
        userAction = getInteraction()
        currEmotion = lookupEmotion(currEmotion, userAction)
main()

    
