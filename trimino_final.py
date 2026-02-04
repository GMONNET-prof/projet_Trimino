from random import *
from turtle import *


speed(10) # 1 - 10 du plus lent au plus rapide, 0 étant le plus rapide
colormode(255) # définition du mode de couleur en RBG
hideturtle() # cacher la tortue
width(2) # épaisseur du crayon

tracer(0, 0)  # Désactive l'animation automatique pour un contrôle manuel du rendu
def aller(x,y):
    """
    Déplace la tortue aux coordonnées spécifiées (x, y) sans dessiner.
    Entrée :
        - x (int) : position x de destination.
        - y (int) : position y de destination.
    Sortie : aucune (déplace la tortue à la position donnée).
    """
    up()
    goto(x,y)
    down()
    
    
def trouve_case_occupee(grille, x, y, delta):
    """
    Cherche si une case d'une sous-grille delta x delta est occupée.
    Détermine la zone où la case occupée se trouve parmi les 4 quadrants de la sous-grille.
    Entrée :
        - grille (list) : la grille de jeu.
        - x (int) : coordonnée x du coin supérieur gauche de la sous-grille.
        - y (int) : coordonnée y du coin supérieur gauche de la sous-grille.
        - delta (int) : taille de la sous-grille (doit être une puissance de 2).
    Sortie :
        - (str) : une des valeurs suivantes : "BD", "HG", "BG", "HD" 
          qui représente la zone dans laquelle la case est occupée.
    """
    for i in range(x,x+delta):
        for j in range(y,y+delta):
            if grille[i][j]!=0:
                if i < x+delta//2 and j < y+delta//2:
                    return "BD"
                elif i >= x+delta//2 and j >=y+ delta//2:
                    return"HG"
                elif i < x+delta//2 and j >= y+delta//2: 
                    return"BG"
                else:
                    return"HD"
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

def creation_tableau(taille):
    """
    Crée un tableau (grille) de taille 'taille' x 'taille' initialisé à zéro.
    Entrée :
        - taille (int) : taille de la grille (dimensions de la grille carrée).
    Sortie :
        - tab (list) : grille de taille 'taille' x 'taille' remplie de 0.
    """
    tab = []
   
    
    for i in range (taille):
        tab_tmp=[0]*taille
        tab.append(tab_tmp)
        
    return tab   
                

def case_noire(tab):
    """
   Génère une case noire aléatoire dans la grille et la marque avec -1.
   Entrée :
       - grille (list) : la grille de jeu.
   Sortie :
       - (tuple) : coordonnées (x, y) de la case noire générée.
   """
    x = randint(0, len(tab)-1)
    y = randint(0, len(tab)-1)
    tab[x][y] = -1
    return  (x,y)                



def resoudre_tableau(grille,x,y,delta):
    """
    Résout le placement des triminos dans la grille à partir de la case (x, y).
    Utilise la récursion pour diviser la grille en sous-grilles.
    Entrée :
        - grille (list) : la grille de jeu.
        - x (int) : coordonnée x de la case de départ.
        - y (int) : coordonnée y de la case de départ.
        - delta (int) : taille de la sous-grille (doit être une puissance de 2).
    Sortie : aucune (modifie la grille directement).
    """
    orientation=trouve_case_occupee(grille, x, y, delta)
    if delta ==2:
        dessiner_trimino(grille, x, y, orientation)
        maj_tableau(grille,x,y,orientation)
        
    else:
        delta=delta//2
        maj_tableau(grille,x+delta-1,y+delta-1,orientation)
        dessiner_trimino(grille, x+delta-1, y+delta-1, orientation)
        resoudre_tableau(grille,x,y,delta)
        resoudre_tableau(grille,x+delta,y,delta)
        resoudre_tableau(grille,x,y+delta,delta)
        resoudre_tableau(grille,x+delta,y+delta,delta)        
        
        
def dessiner_grille(taille):
    """Dessine les segments de la grille en noir
    Entrée : 𝑛 pour dessiner 2𝑛 + 1 segments verticaux et horizontaux
    Sortie : aucune """  
    penup()   
    cote = 512 // taille
    # Dessiner les segments verticaux
    for i in range(taille +1):
        goto(-256 + i* cote, 256)
        pendown()
        setheading(270)  
        forward(512)
        penup()
    # Dessiner les segments horizontaux
    for j in range(taille +1):
        goto(256, 256 - j *cote)
        pendown()
        setheading(180)  
        forward(512)
        penup()
        

def dessiner_case_noire(x,y): 
    """dessine une case noir l'endroit souhaité
    entree: cordonnées souhaités (x,y)
    sortie: aucune"""
    begin_fill()
    color(0,0,0) # couleur noire
    X = -256 + 512//taille * y
    Y = 256 - 512//taille * x
    aller(X,Y)
    setheading(0)  
    for i in range(0, 2):
        forward(512//taille)
        right(90)
        forward(512//taille)
        right(90)
    end_fill()
    
    
    
def coordonnées_vers_px(x, y):
    """
    Convertit les coordonnées de la grille (x, y) en pixels pour afficher sur l'écran.
    Entrée :
        - x (int) : coordonnée x de la grille.
        - y (int) : coordonnée y de la grille.
    Sortie :
        - [px_x, px_y] (list) : liste contenant les coordonnées en pixels.
    """
    X = -256 + (512//(taille)) * y
    Y = 256 - (512//(taille)) * x
    return [X, Y]


def dessiner_trimino(grille, x, y, orientation):
    """
    Dessine un triminos de forme en L à l'endroit spécifié avec une orientation donnée.
    Entrée :
        - grille (list) : la grille de jeu.
        - x (int) : coordonnée x du coin supérieur gauche du triminos.
        - y (int) : coordonnée y du coin supérieur gauche du triminos.
        - orientation (str) : orientation du triminos ("HG", "HD", "BD", "BG").
    Sortie : aucune (dessine un triminos sur l'écran).
    """
    
    penup()
    color(randint(0, 255), randint(0, 255), randint(0, 255)) # couleur aléatoire
    X, Y = coordonnées_vers_px(x,y)
    aller(X,Y)
    if orientation == "HG":
        setheading(0)
        pendown() 
        begin_fill()
        forward(512//taille*2)
        right(90)
        forward(512//taille)
        right(90)
        forward(512//taille)
        left(90)
        forward(512//taille)
        right(90)
        forward(512//taille)
        right(90)
        forward(512//taille*2)
        end_fill()
        penup()
        
    if orientation == "HD":
        setheading(0)    
        pendown()
        begin_fill()
        forward(512//taille*2)
        right(90)
        forward(512//taille*2)
        right(90)
        forward(512//taille)
        right(90)
        forward(512//taille)
        left(90)
        forward(512//taille)
        right(90)
        forward(512//taille)
        
        end_fill()  
        penup()
        
    if orientation == "BG":
        setheading(0)    
        pendown()
        begin_fill()
        forward(512//taille)
        right(90)
        
        forward(512//taille)
        left(90)
        
        forward(512//taille)
        right(90)
        
        forward(512//taille)
        right(90)
        
        forward(512//taille*2)
        right(90)
        
        forward(512//taille*2)
        
        end_fill()  
        penup()
        
    if orientation == "BD":
        setheading(0)    
        penup()
        forward(512//taille)
        pendown()
        begin_fill()
        forward(512//taille)
        right(90)
        
        forward(512//taille*2)
        right(90)
        
        forward(512//taille*2)
        right(90)
        
        forward(512//taille)
        right(90)
        
        forward(512//taille)
        left(90)
        
        forward(512//taille)
        end_fill()  
        penup()
        



        
taille = 16
   
dessiner_grille(taille)
grille = creation_tableau(taille) 
x,y = case_noire(grille)
dessiner_case_noire(x,y)
resoudre_tableau(grille,0,0, taille)
exitonclick()