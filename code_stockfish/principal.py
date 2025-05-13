from coup_du_bot import coup_du_bot



board = [
    ['wr'], ['wn'], ['wb'], ['wq'], ['wk'], ['wb'], ['wn'], ['wr'],  # 0–7
    ['wp'], ['wp'], ['wp'], ['wp'], ['wp'], ['wp'], ['wp'], ['wp'],  # 8–15
    ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'],  # 16–23
    ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'],  # 24–31
    ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'],  # 32–39
    ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'], ['--'],  # 40–47
    ['bp'], ['bp'], ['bp'], ['bp'], ['bp'], ['bp'], ['bp'], ['bp'],  # 48–55
    ['br'], ['bn'], ['bb'], ['bq'], ['bk'], ['bb'], ['bn'], ['br'],  # 56–63
]
#Tableau de 1x64 avec la position de la partie
#Remplir par rangée puis par colonne : A1, B1, C1, D1, E1, F1, G1, H1, A2 ...
#Informations sur chaque case :
    # 'xy' 
        # 'x' = couleur de la pièce : 'w' pour blanc, 'b' pour noir
        # 'y' = type de la pièce : 'p' pour pion, 'r' pour tour, 'n' pour cavalier, 'b' pour fou, 'q' pour dame, 'k' pour roi


chemin = 'C:/Projets/Projet_Magnus/stockfish_app/stockfish-windows-x86-64-avx2.exe'

#Chemin vers l'exécutable de Stockfish

niveau = 2000
#Niveau de jeu du bot (entre 1350 et 2850)

couleur = 'blanc'
#Couleur du bot : 'blanc' ou 'noir'

meilleur_coup = coup_du_bot(board, chemin, niveau, couleur)
#Appel de la fonction pour obtenir le meilleur coup

print(meilleur_coup)