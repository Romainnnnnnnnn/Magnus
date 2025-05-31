def question_couleur():
    color = None
    while color not in ['b', 'w']:
        color = input("Quelle couleur voulez-vous jouer ? (b pour blanc, n pour noir) : ").lower()
        if color == 'b':
            print("Vous jouez avec les blancs.")
            print("Le bot joue avec les noirs.")
            color = 'b'
        elif color == 'n':
            print("Vous jouez avec les noirs.")
            print("Le bot joue avec les blancs.")
            color = 'w'
        else:
            print("Couleur non reconnue.")
    return color