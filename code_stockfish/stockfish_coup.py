import chess
import io
import random



def stockfish_coup(chemin, niveau, position, couleur):

    from stockfish import Stockfish
    stockfish = Stockfish(
    path=chemin,
    parameters={
        "Threads": 4,
        "Skill Level": 20,
        "Hash": 1024,
        "MultiPV": 5,
        "UCI_LimitStrength": True,
        "UCI_Elo": niveau, #variable d'entrée entre 1350 et 2850
    }
)

    #Mode auto depuis matrice
    stockfish.set_fen_position(position)
    #stockfish.set_fen_position(position.fen())

    #Mode manuel depuis position fen
    #stockfish.set_fen_position('r1bkkk1r/p1p2ppp/1pnp1n2/2b1p1N1/2B1P3/B1N4P/P1PP1PP1/R2Q1K1R w - - 1 1')

    cinq_meilleurs_coups = stockfish.get_top_moves()
    coup_aleatoire = random.choice(cinq_meilleurs_coups)
    coup_final = coup_aleatoire['Move']
    return(coup_final)