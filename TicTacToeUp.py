import random

def printBoard(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i != 6:
            print("---------")

def playerInput(board):
    while True:
        inp = int(input("Type a number from 1-9:"))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = "X"
            break
        else:
            print("Invalid move")

def checkWin(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)             # diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "-":
            return board[condition[0]]
    if "-" not in board:
        return "Tie"
    return None

def computer(board):
    while True:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            break

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
current_player = "X"

while True:
    printBoard(board)
    playerInput(board)
    winner = checkWin(board)
    if winner:
        print(f"The winner is {winner}!")
        break
    computer(board)
    winner = checkWin(board)
    if winner:
        print(f"The winner is {winner}!")
        break
