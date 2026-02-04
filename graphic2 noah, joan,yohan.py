import turtle
from random import randint

turtle.colormode(255)

def aller(x, y):
    """
    Déplace la tortue à la position (x, y) sans dessiner.

    Paramètres :
        x (int) : Coordonnée x de la position cible.
        y (int) : Coordonnée y de la position cible.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def dessiner_grille(taille):
    """
    Dessine une grille carrée de taille spécifiée. La grille est composée de carrés.

    Paramètres :
        taille (int) : Nombre de cases par côté de la grille.
    """
    cpt1 = 0
    cpt2 = 0
    x = -256
    y = 256
    grid_size = 512 // taille

    # Dessiner les lignes horizontales
    while cpt1 < taille + 1:
        aller(x, y)
        turtle.forward(512)
        y = y - grid_size
        aller(x, y)
        cpt1 += 1

    x = -256
    y = 256
    turtle.right(90)  # Réorientation pour dessiner les lignes verticales
    # Dessiner les lignes verticales
    while cpt2 < taille + 1:
        aller(x, y)
        turtle.forward(512)
        x = x + grid_size
        aller(x, y)
        cpt2 += 1

def dessiner_case_noire(x, y, taille):
    """
    Dessine une case noire à la position (x, y) dans la grille.

    Paramètres :
        x (int) : Coordonnée x de la case.
        y (int) : Coordonnée y de la case.
        taille (int) : Nombre de cases par côté de la grille.
    """
    grid_size = 512 // taille
    X = -256 + y * grid_size
    Y = 256 - x * grid_size
    aller(X, Y)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(grid_size)
        turtle.left(90)
    turtle.end_fill()

def dessiner_trimino(taille, x, y, orientation):
    """
    Dessine un trimino en forme de "L" à la position (x, y) selon l'orientation spécifiée.

    Paramètres :
        taille (int) : Nombre de cases par côté de la grille.
        x (int) : Coordonnée x de la case de départ du trimino.
        y (int) : Coordonnée y de la case de départ du trimino.
        orientation (str) : Orientation du trimino parmi les options suivantes : 
                             "HG", "HD", "BG", "BD" (Haut-Gauche, Haut-Droite, Bas-Gauche, Bas-Droite).
    """
    cote = 512 // taille
    X = -512 // 2 + y * cote
    Y = 512 // 2 - x * cote

    # Affichage de "Trimino" en haut de la fenêtre
    turtle.penup()
    turtle.goto(0, 250)  # Positionner le texte en haut de la page
    turtle.pendown()
    turtle.write("Trimino", align="center", font=("Arial", 24, "bold"))
    
    # Si l'orientation est invalide, afficher l'erreur et ne pas dessiner le trimino
    if orientation not in ["HG", "HD", "BG", "BD"]:
        print("Orientation invalide")
        return

    # Si l'orientation est valide, dessiner le trimino
    turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))  # Remplissage aléatoire
    turtle.pensize(2)  # Contour de la forme

    # Dessiner le trimino en fonction de l'orientation
    if orientation == "HG":
        aller(X, Y)
        turtle.setheading(0)
        turtle.begin_fill()
        turtle.forward(cote)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.left(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.forward(cote)
        turtle.end_fill()

    elif orientation == "HD":
        aller(X, Y)
        turtle.setheading(0)
        turtle.begin_fill()
        turtle.forward(cote)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.left(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.end_fill()

    elif orientation == "BG":
        aller(X, Y)
        turtle.setheading(0)
        turtle.begin_fill()
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.left(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.forward(cote)
        turtle.end_fill()

    elif orientation == "BD":
        aller(X, Y)
        turtle.setheading(270)
        turtle.penup()
        turtle.forward(cote)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(cote)
        turtle.left(90)
        turtle.forward(cote*2)
        turtle.left(90)
        turtle.forward(cote*2)
        turtle.left(90)
        turtle.forward(cote)
        turtle.left(90)
        turtle.forward(cote)
        turtle.right(90)
        turtle.forward(cote)
        turtle.end_fill()

def case_noire(tab, taille):
    """
    Placer une case noire aléatoire dans la grille.

    Paramètres :
        tab (list) : La grille sous forme de liste de listes.
        taille (int) : Nombre de cases par côté de la grille.

    Retour :
        tuple : Les coordonnées (x, y) de la case noire ajoutée.
    """
    x = randint(0, taille - 1)
    y = randint(0, taille - 1)
    tab[x][y] = -1
    dessiner_case_noire(x, y, taille)
    return (x, y)

def creation_tableau(taille):
    """
    Crée un tableau vide représentant la grille de taille `taille`.

    Paramètres :
        taille (int) : Nombre de cases par côté de la grille.

    Retour :
        list : Une liste de listes représentant la grille vide.
    """
    tab = []
    for i in range(taille):
        tab.append([0] * taille)
    dessiner_grille(taille)
    return tab

def trouve_case_occupee(grille, x, y, delta):
    """
    Trouve l'orientation d'une case occupée pour la découpe du trimino.

    Paramètres :
        grille (list) : La grille sous forme de liste de listes.
        x (int) : Coordonnée x de la case.
        y (int) : Coordonnée y de la case.
        delta (int) : Taille de la sous-grille dans laquelle rechercher.

    Retour :
        str : L'orientation du trimino ("HG", "HD", "BG", "BD").
    """
    for i in range(x, x + delta):
        for j in range(y, y + delta):
            if grille[i][j] != 0:
                if i < x + delta // 2 and j < y + delta // 2:
                    return "BD"
                elif i >= x + delta // 2 and j >= y + delta // 2:
                    return "HG"
                elif i < x + delta // 2 and j >= y + delta // 2:
                    return "BG"
                else:
                    return "HD"

def maj_tableau(grille, x, y, orientation):
    """
    Met à jour la grille en insérant un trimino à la position (x, y) avec l'orientation donnée.

    Paramètres :
        grille (list) : La grille sous forme de liste de listes.
        x (int) : Coordonnée x de la case où le trimino est placé.
        y (int) : Coordonnée y de la case où le trimino est placé.
        orientation (str) : Orientation du trimino ("HG", "HD", "BG", "BD").
    """
    dessiner_trimino(taille, x, y, orientation)
    match orientation:
        case "HG":
            grille[x][y], grille[x + 1][y], grille[x][y + 1] = [1, 1, 1]
        case "HD":
            grille[x][y + 1], grille[x][y], grille[x + 1][y + 1] = [1, 1, 1]
        case "BD":
            grille[x + 1][y + 1], grille[x][y + 1], grille[x + 1][y] = [1, 1, 1]
        case _:
            grille[x + 1][y], grille[x][y], grille[x + 1][y + 1] = [1, 1, 1]

def resoudre_tableau(grille, x, y, delta):
    """
    Résout le problème de placement des triminos pour remplir la grille.

    Paramètres :
        grille (list) : La grille sous forme de liste de listes.
        x (int) : Coordonnée x de la case à traiter.
        y (int) : Coordonnée y de la case à traiter.
        delta (int) : Taille de la sous-grille à traiter (initialement la taille complète).
    """
    orientation = trouve_case_occupee(grille, x, y, delta)
    if delta == 2:
        maj_tableau(grille, x, y, orientation)
    else:
        delta = delta // 2
        maj_tableau(grille, x + delta - 1, y + delta - 1, orientation)
        resoudre_tableau(grille, x, y, delta)
        resoudre_tableau(grille, x + delta, y, delta)
        resoudre_tableau(grille, x, y + delta, delta)
        resoudre_tableau(grille, x + delta, y + delta, delta)

# Code principal pour initialiser et dessiner
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")
turtle.setup(600, 600)

# Paramètres de la grille
taille = 16
ma_grille = creation_tableau(taille)
case_noire(ma_grille, taille)
resoudre_tableau(ma_grille, 0, 0, taille)

turtle.update()  # Mise à jour manuelle de l'écran

# Attente d'un clic pour fermer
turtle.exitonclick()

