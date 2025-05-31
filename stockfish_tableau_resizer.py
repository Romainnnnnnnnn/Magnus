import io

#def tableau_resizer(board):
#    board_8x8 = [[board[row * 8 + col][0] for col in range(8)] for row in range(8)]
#    return board_8x8

def tableau_resizer(board, color):
    if color == "b":
        return [[board[row * 8 + col][0] for col in range(8)] for row in range(8)]
    elif color == "w":
        return [[board[(7 - row) * 8 + (7 - col)][0] for col in range(8)] for row in range(8)]



    