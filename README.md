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

# Plateau d'échecs

Le plateau serait un plateau sur mesure de 8x8 cases comme tout plateau de jeu d'échecs mais avec des cases de 5cmx5cm pour permettre une prise efficace par la pince du robot. Le plateau ferait 40cmx40cm au total. Les pièces seront des jetons de puissance 4 avec des images collées sur ces derniers, ce sont ces images qui seront reconnues.
