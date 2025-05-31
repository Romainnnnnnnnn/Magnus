from stockfish_tableau_resizer import tableau_resizer

from stockfish_tableau_to_fen import tableau_to_fen

from stockfish_best_play import stockfish_coup


def coup_du_bot(board, chemin, niveau, couleur):

    board = [[piece] for piece in board]

    board = board[::-1]
    
    board = [row[::-1] for row in board]

    board = tableau_resizer(board, couleur)

    position = tableau_to_fen(board, couleur)
    
    meilleur_coup = stockfish_coup(chemin, niveau, position)
    
    return(meilleur_coup)






