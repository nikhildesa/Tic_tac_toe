import random
global board
board = ["_","_","_",
        "_","_","_",
        "_","_","_"]

global count
count = 0

def check_game(turn):
    count+=1;
    if board['7'] == board['8'] == board['9'] != ' ': # across the top
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")                
        break
    
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break 
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        print(board)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")
        break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
        print("\nGame Over.\n")                
        print("It's a Tie!!")


def board_display():
    print(board[0] +"|" + board[1] +"|" + board[2])
    print(board[3] +"|" + board[4] +"|" + board[5])
    print(board[6] + "|" + board[7] +"|" + board[8])
    
    
    
 

board_display()

def human():
    a = input("Enter location")
    board[int(a)] = "x"
    board_display()
    turn = "Human"
    check_game(turn)
    

i = input("Press 1. Heads  Press 2. tails")


board = human()


