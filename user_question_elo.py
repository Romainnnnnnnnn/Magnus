def question_elo():
    elo = None
    while True:
        try:
            elo = int(input("Choisissez l'elo de Stockfish ? (entre 1350 et 2850) : "))
            if 1350 <= elo <= 2850:
                print(f"L'elo de Stockfish est fixé à {elo}.")
                return elo
            else:
                print("Veuillez entrer un ELO compris entre 1350 et 2850.")
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'ELO.")