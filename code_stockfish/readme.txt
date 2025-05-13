Prérequis :
	- Avoir Stockfish d'installé sur son pc
	- Connaitre le chemin du stockfish-windows-x86-64-avx2.exe
	- Faire pip install stockfish dans l'environnement virtuel
    - Faire pip install chess dans l'environnement virtuel

Paramètres d'entrée :

	- board : tableau de Strings de 1x64 avec la position de la partie
		- Le remplir par rangée puis par colonne : A1, B1, C1, D1, E1, F1, G1, H1, A2 ...
		- Informations sur chaque case :
    		- 'xy' 
        	- 'x' = couleur de la pièce : 'w' pour blanc, 'b' pour noir
        	- 'y' = type de la pièce : 'p' pour pion, 'r' pour tour, 'n' pour cavalier, 'b' pour fou, 'q' pour dame, 'k' pour roi

	- chemin : chemin vers l'exécutable de Stockfish

	- niveau : niveau de jeu du bot (entre 1350 et 2850)

	- couleur : couleur que joue le bot

Paramètre de sortie :

	- meilleur_coup : coup que renvoie le programme

Fonctions :

	- principal.py : code principal où on appelle la fonction mère

	- coup_du_bot.py : fonction mère qui sur base de la position, renvoie le meilleur coup de Stockfish selon sa configuration

	- tableau_resizer : fonction qui convertit le tableau 1x64 en 8x8

	- tableau_to_fen : fonction qui convertit le tableau 8x8 en fen
	
	- stockfish_coup : fonction qui sur base du fen, renvoie le meilleur coup


