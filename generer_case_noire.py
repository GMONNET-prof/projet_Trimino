from random import*


def generer_case_noire(grille):
    """ renvoie les coordonnées de la case noire (tuple de deux valeurs)
    et modifie la grille
    Entrée : La grille 
    Sortie : Coordonnées de la case noire"""
    
    n = len(grille)
    x = randint(0, n-1)
    y = randint(0, n-1)
    
    grille[y][x] = -1 # Case noire créée
    
    return x, y
    





    
