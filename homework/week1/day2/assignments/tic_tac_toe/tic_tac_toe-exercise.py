# -*- coding: utf-8 -*-
"""
Exercise. Tic-tac-toe

We are going to build a program that allows us to play tic-tac-toe on the terminal


In a nutshell, the tic-tac-toe board can be thought of 3 lists inside another one

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

for example, if we want to see what is the state of the box above to the
Left, we can access doing board [[0,0]]

We have 2 players, and each player will alternate in choosing a different slot on the board,
and placing either an "X"  (player 1) or "O" (player 2)

The game will have to validate that the new coordinates chosen by the current player 
are valid, i.e., they need to be empty and be inside the board.


Hint: You can use a deque (in the module collections) to rotate between player 1 and 2
"""
"""
Tried my best to finish this tic tac toe game but was unable to fully finish,
need to take a day
to study up on the fundamentals and practice up
"""
board = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"]]
    

turns = 1
row = 3
col = 3
rowX = 0
rowO = 0
colX = 0
colO = 0


while turns <= 9:
    print(board)
    if turns % 2 ==1:
        row = input("Player 1 : Row")
        row = int(row)
        col = input("Player 1 : Col")
        col = int(col)
    if turn_number % 2 == 0:
        row = input("Player 2 : Row")
        row = int(row)
        col = input("Player 2 : Col")
        col = int(col)
    if board(row)(col) ==" ":
        if turn % 2 == 1:
            baord(row)(col) = "X"
        if turn % 2 == 0:
            baord(row)(col) = "O"
        turns += 1
        
        
    for x in range (0,3):
        for y in range(0, 3):
            if board[x][y] == "X":
                rowX += 1
            elif board[x][y] == "O":
                rowO += 1
            if isWinner("X"):
                print("WINNER! : PLAYER 1") 
                exit()
            if isWinner("O"):
                print("WINNER : PLAYER 2")
                exit()

                
        


def isWinner(board): ##getting lost on how to check if the player has won

    if  (board[0][0] == board[1][0] == board[2][0] | 
        board[0][1] == board[1][1] == board[2][1] | 
        board[0][2] == board[1][2] == board[2][2] | 
        board[0][0] == board[0][1] == board[0][2] | 
        board[1][0] == board[1][1] == board[1][2] | 
        board[2][0] == board[2][1] == board[2][2] | 
        board[0][2] == board[1][1] == board[2][0] | 
        board[0][0] == board[1][1] == board[2][2]) :
        return True
    else :
        return False
        
            


