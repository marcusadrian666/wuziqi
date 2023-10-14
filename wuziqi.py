import numpy as np
def create_board():
    board = np.zeros((15, 15))
    return board
def place_stone(board, row, col, player):
    board[row][col] = player
def is_valid_move(board, row, col):
    return board[row][col] == 0
def get_winner(board):
    # 检查行
    for i in range(15):
        for j in range(11):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] != 0:
                return board[i][j]
    # 检查列
    for i in range(11):
        for j in range(15):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] != 0:
                return board[i][j]
    # 检查主对角线
    for i in range(11):
        for j in range(11):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4] != 0:
                return board[i][j]
    # 检查副对角线
    for i in range(11):
        for j in range(4, 15):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == board[i+4][j-4] != 0:
                return board[i][j]
    # 如果都没有赢家，返回0
    return 0
board = create_board()
player = 1
while True:
    print(board)
    print("It's player " + str(player) + "'s turn")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if not is_valid_move(board, row, col):
        print("Invalid move. Try again.")
        continue
    place_stone(board, row, col, player)
    winner = get_winner(board)
    if winner != 0:
        print(board)
        print("Player " + str(winner) + " wins!")
        break
    player = 2 if player == 1 else 1
