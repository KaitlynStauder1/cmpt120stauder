# CMPT 120 Intro to Programming
# Lab 6 - Lists and Error Handling
# Author: Kaitlyn Stauder
# Created: 2018-03-24

symbol = ["   "," x ", " o "]
board = [["   ", "   ", "   "],
         ["   ", "   ", "   "],
         ["   ", "   ", "   "]]

def printBoard(board):
   for row in range(3):
          print("+-----------+")
          row_string = ""
          for col in range(3):
                row_string = row_string + "|  " + board[row][col]
          print(row_string + "| ")
   print("+-----------+")

def markBoard(board, row, col, player, symbol):
      board[row][col] = symbol[player]
      return board

def getPlayerMove(board):
   valid_move = False
   while not valid_move:
      row = int(input("Enter the row number that you'd like to place your marker.\n"))
      if row < 0 or row > 2:
         print("Invalid row!\nRow must be between 0 and 2.")
         continue
      col = int(input("Enter the column number that you'd like to place your marker.\n"))
      if col < 0 or col > 2:
         print("Invalid column!\nColumn must be between 0 and 2.")
         continue
      if board[row][col] == " ":
         valid_move = True
      else:
         print("Position " + str(row) +  ", " + str(col) + " is already occupied!\nPick a different spot.")
   return (row, col)

    
def hasBlanks(board):
   for row in range(3):
       for col in range(3):
               if board[row][col] == " ":
                        return True
   return False

def main():
        symbol = [" ","x", "o"]
        board =[[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
        print("Welcome to Tic Tac Toe!")
        print("Player 1 is X and Player 2 is O.")
        print("Player 1 will go first, please enter a row number (0-2) and then a column number (0-2)")
        player = 1
        while hasBlanks(board):
               printBoard(board)
               row, col = getPlayerMove(board)
               board = markBoard(board, row, col, player, symbol)
               player = player % 2 + 1
        printBoard(board)

main()

        
    
