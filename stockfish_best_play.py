import chess
import io
import random



def stockfish_coup(chemin, niveau, position):

    from stockfish import Stockfish
    stockfish = Stockfish(
    path=chemin,
    parameters={
        "Threads": 4,
        "Skill Level": 20,
        "Hash": 1024,
        "MultiPV": 1,
        "UCI_LimitStrength": True,
        "UCI_Elo": niveau, #variable d'entrée entre 1350 et 2850
    }
)

    position
    stockfish.set_fen_position(position)

    coup_final = stockfish.get_best_move()
    if coup_final is None:
        print("No legal moves: checkmate or stalemate.")
        return None
    visu = stockfish.get_board_visual()
    print(visu)
    
    return(coup_final)