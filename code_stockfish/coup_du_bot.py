from tableau_resizer import tableau_resizer

from tableau_to_fen import tableau_to_fen

from stockfish_coup import stockfish_coup


def coup_du_bot(board, chemin, niveau, couleur):

    board = tableau_resizer(board)

    position = tableau_to_fen(board)
    
    meilleur_coup = stockfish_coup(chemin, niveau, position, couleur)
    
    return(meilleur_coup)






