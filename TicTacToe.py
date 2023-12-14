# game board array with "-" to represent lines in the TicTacToe board that will be printed in the while loop below

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# setting global variables to values that may or may not be changed throughout functions
currentPlayer = "X"
winner = None
gameRunning = True

# Welcome message. Also includes user input to either start the game or not.
print("Welcome to Tic Tac Toe!")
start_input = input("Please type Play to start the game:").lower()
if start_input == "play":
    t = True
else:
    t = False
    start_retry = input("Invalid Input. If it was a typo, please type play to start: ".lower()) # give user another chance to play game while in prgoram if it was a typo
    if start_retry == "play":
        t = True 
    else:
        t = False

while t is True:
    
# prints board using dashes from board variable 
    def printBoard(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

  






    # takes player input that will be used in game
    def playerInput(board):
        inp = input("Enter a number 1-9: ")
        inp_to_integer = int(inp) # user input is a string, not a integer, so I create this function to turn string in integer
        if inp_to_integer >= 1 and inp_to_integer <= 9 and board[inp_to_integer-1] == "-":
            board[inp_to_integer-1] = currentPlayer
        else:
            print("Oops player is already in that spot!")




    # check for win or tie
    def checkHorizontal(board): # determines if three user inputs are in a row in board
        global winner 
        if board[0] == board[1] == board[2] == board[0] and board[0] != "-" and board [2] != "-" and board [1] != "-":
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != "-" and board[4] != "-" and board [5] != "-":
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != "-" and board[7] != "-" and board[8] != "-":
            winner = board[6]
            return True
        

    def checkRow(board): # determines if three user inputs are in a row in board
        global winner
        if board[0] == board[3] == board[6] == board[0] and board[0] != "-" and board[3] != "-" and board[6] != "-":
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != "-":
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != "-":
            winner = board[0]
            return True

    def checkDiag(board): # determines if three user inputs are in a row in board
        global winner
        if board[0] == board[4] == board[8] and board[0] != "-" and board[4] != "-" and board[8] != "-":
            winner = board[0]
            return True
        
    def checkTie(board):
        if "-" not in board:
            printBoard(board)
            print("It is a tie!!")
            gameRunning = False
# function checks for win by checking three functions above, then printing a winner message and a restart option
    def checkWin():
        if checkDiag(board) or checkHorizontal(board) or checkRow(board):
            print(f"The winner is {winner}")
            restart = input("If you would like to play again, type play").lower()
            if restart == "play":
                resetGame()
            else:
                print("Thanks for playing!")
                t = False
# reset game function added to allow for restart option for players.
    def resetGame():
        global board, winner, gameRunning, currentPlayer
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        winner = None
        gameRunning = True
        currentPlayer = "X"

            






        










    # switch the player
    def switchPlayer():
        global currentPlayer
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"


    # check for win or tie again

    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()

    

