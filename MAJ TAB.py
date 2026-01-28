def maj_tableau(grille, x, y, orientation):
    """
    met des 1 dans les trois cases du triminos
    Entrée : 
    - grille (liste de liste)
    - x, y (coordonnées de la case (2x2) où le trimino est placé)
    - orientation (str) -> HD HG BD BG
    """
    match orientation:
        case "HG":
            grille[x][y],grille[x+1][y],grille[x][y+1] = [1,1,1]
        case "HD":
            grille[x][y+1],grille[x][y],grille[x+1][y+1] = [1,1,1]
        case "BD":
            grille[x+1][y+1],grille[x][y+1],grille[x+1][y] = [1,1,1]
        case _:
            grille[x+1][y],grille[x][y],grille[x+1][y+1] = [1,1,1]
            