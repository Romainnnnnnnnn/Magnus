import io

def tableau_resizer(board):
    board_8x8 = [[board[row * 8 + col][0] for col in range(8)] for row in range(8)]
    return board_8x8


    