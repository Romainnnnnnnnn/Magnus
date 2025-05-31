# Description du projet 

L'objectif est de pouvoir jouer aux échecs, en physique, contre une intelligence artificielle. Les coups de l'IA seraient réalisés par un UR3. 

Le projet est décomposé en 3 parties :

    -D'une part, il y a la reconnaissance d'image. Par l'intermédiaire d'une caméra (fixée sur le bras du robot, ou sur un support fixe), l'IA sera en mesure de reconnaître les différentes pieces sur les cases du plateau. Pour une question de simplicité, nous nous limiterons à un seul plateau, et à des pièces sur mesures.

    -D'autre part, il y a l'IA / l'algorithme qui sera en mesure de décider des coups. Etant donné que cela sort du projet, nous utiliserons une IA entrainée "toute faite" (à part si le temps nous le permet). 

    -Et enfin, il y a la partie robot qui recevra les mouvements à faire pour deplacer les bonnes pieces ou il faut.

## Reconnaissance d'image

L'IA de reconnaissance d'image servirait à reconnaitre les pieces et leur place, afin de traduire l'état du jeu en chaine de caractère et cette dernière serait alors donnée à l'algorithme qui décide du prochain coup. 

## IA joueuse d'échecs

Cette IA serait probablement un modèle tout fait qu'il faut implémenter/attacher à notre projet. Il recevrait alors l'état du jeu et il retournerait le prochain coup a faire.

## Bras robotisé

Ce bras robotisé sera à piori l'UR3. Celui ci recevrait le prochain coup à faire et degagerait la case arrivée s'il y a une pièce, puis deplacerait la piece de la case départ vers la case arrivée.
Les différentes actions possibles du robot, sachant qu'il doit connaitre les positions des cases, seraient :
    -prendre pièce
    -poser pièce
    -dégager pièce prise

## Ordre de réalisation

Afin de rester focus sur l'objetif premier qui est la reconnaissance d'image, la premiere étape du projet sera la reconnassance du jeu. Ensuite vient l'ajout de l'IA pour calculer les bons coups. Nous pourrons ainsi faire le déplacement des pièces manuellement à la place du robot en premier temps. Il est plus logique de faire le projet dans ce sens car il est moins intéressant d'implémenter le robot sans savoir les coups qu'il faut faire.

L'ordre est donc le suivant : 
    -Reconnaissance du jeu
    -IA pour caclculer le prochain coup suivant l'état du jeu
    -Bras robotisé qui realise le déplacement des pièces

## Plateau d'échecs

Le plateau serait un plateau sur mesure de 8x8 cases comme tout plateau de jeu d'échecs mais avec des cases de 5cmx5cm pour permettre une prise efficace par la pince du robot. Le plateau ferait 40cmx40cm au total. Les pièces seront des jetons de puissance 4 avec des images collées sur ces derniers, ce sont ces images qui seront reconnues.


## Les différents éléments

### Chess_Data

Dataset utilisé pour l'entrainement, sans augmentation "artificielle". 13 classes, 64 images par classe. Ce document est associé au csv Chess_Data.

### Test_Data

Dataset utilisé pour l'évaluation, sans augmentation "artificielle". 13 classes, 64 images par classe. Ce document est associé au csv Test_Data.

#### magnus_model

Modèle entrainé avec Chess_Data, et évalué avec Test_Data.



### Codes - image

Ces codes permettent le traitement de l'image de la Webcam. 

#### image_camera_calibration

Code utilisé lors de l'installation du système physique. Cela permet d'avoir un visuel de la caméra, divisé en 64 cases, afin d'ajuster le positionnement de la caméra et de l'echiquier.

#### image_acquisition

Code utilisé pour capturer l'image de la Webcam et en ajuster la résolution, la diviser en 64 cases d'une grille de 8x8, et enregistrer les images de chaque case. L'enregistrement est utilisé pour 2 choses. D'une part, il a permis initialement la création des datasets. D'autre part, il permet l'apport d'images pour l'IA.


### Codes - model

Ces codes permettent la création et l'entrainement du modèle.

#### model_class_Magnus

Code dans lequel on définit la structure du modèle.

#### model_building

Code dans lequel la data est augmentée, le modèle est entrainé, testé et enregistré

#### model_predictions

Code qui via les images renvoyées par le code image_acquisition, et le modèle entrainé via model_building, renvoie une matrice de la position actuelle


### Codes - user

Questions pour l'utilisateur

#### user_question_couleur

Demande à l'utilisateur s'il joue les noirs ou les blancs

#### user_question_elo

Demande à l'utilisateur l'elo de Stockfish

#### user_questions

Code mère qui fait appel aux 2 autres codes


### Stockfish

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

	- stockfish_tableau_resizer : fonction qui convertit le tableau 1x64 en 8x8

	- stockfish_tableau_to_fen : fonction qui convertit le tableau 8x8 em position FEN
	
	- stockfish_best_play : fonction qui sur base du FEN, renvoie le meilleur coup

	- stockfish_stockfish  : code mère qui renvoie le meilleur coup et affiche un visuel de la position



