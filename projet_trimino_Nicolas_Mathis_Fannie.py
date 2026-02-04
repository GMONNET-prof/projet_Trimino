from turtle import *
from random import *

speed(10) # 1 - 10 du plus lent au plus rapide, 0 étant le plus rapide
colormode(255) # définition du mode de couleur en RBG
#hideturtle() # cacher la tortue
width(2) # épaisseur du crayon
#tracer(0,0) # sans les animations


def aller(x,y):
    """ deplace le stylo """ 
    
    up()
    goto(x,y)
    down()

def convertit_pixel(x,y,longeur,dimension):
    X = -longeur//2 + y*dimension
    Y = longeur//2 - x*dimension
    return X,Y

def dessiner_case_noire(x,y,dimension, longueur):
    """remplit en noir une case de la grille choisie aléatoirement 
       entrée: coordonne de la case noire 
       sortie: Nada 
    """
    X,Y = convertit_pixel(x, y, longueur, dimension)
    aller(X,Y)
    color(0,0,0)
    setheading(0)
    begin_fill()
    for i in range(2):
        forward(dimension)
        right(90)
        forward(dimension)
        right(90)
    end_fill()

def dessiner_grille(n, longueur):
    dimension_case=longueur//n
    x=-256
    y=256
    aller(x,y)
    for i in range(n+1):
        forward(dimension_case*n)
        aller(x, y-dimension_case)
        y -=dimension_case
        
    x=-256
    y=256
    aller(x,y)
    right(90)
    for j in range(n+1):
        forward(dimension_case*n)
        aller(x+dimension_case, y)
        x+=dimension_case


def dessin_du_trimino(dimension):
    """Dessine le trimino"""
    color(randint(1, 255), randint(1, 255), randint(1, 255)) # couleur aléatoire
    begin_fill()
    pencolor(0,0,0)
    forward(2*dimension)
    right(90)
    forward(2*dimension)
    right(90)
    forward(dimension)
    right(90)
    forward(dimension)
    left(90)
    forward(dimension)
    right(90)
    forward(dimension)
    end_fill()


def dessiner_trimino(x,y,orientation,dimension):
    """Va au bon emplacement et bonne orientation et appelle la fonction dessin
        entrée: coordonées (int), orientation (str), dimension (int)
        sortie: aucune """
    
    X,Y = convertit_pixel(x, y, longueur, dimension)
    aller(X,Y)
    
    if orientation == "BD":
        aller(X + 2*dimension, Y)
        setheading(-90)
        dessin_du_trimino(dimension)
    
    
    elif orientation == "BG":
        aller(X + 2*dimension ,Y- 2*dimension)
        setheading(180)
        dessin_du_trimino(dimension)
        
    
    elif orientation == "HD":
        aller(X ,Y)
        setheading(0)
        dessin_du_trimino(dimension)
    
    elif orientation == "HG":
        aller(X ,Y- 2*dimension)
        setheading(90)
        dessin_du_trimino(dimension)



def trouve_case_occupee(grille, x, y, delta):
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
    dessiner_trimino(x,y,orientation, dimension)
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
    tab = []
   
    
    for i in range (taille):
        tab_tmp=[0]*taille
        tab.append(tab_tmp)
        
    return tab   
                


def case_noire(tab):
    x = randint(0, len(tab)-1)
    y = randint(0, len(tab)-1)
    tab[x][y] = -1
    return  (x,y)      
          

def resoudre_tableau(grille,x,y,delta):
    orientation=trouve_case_occupee(grille, x, y, delta)
    print(orientation, x, x+delta, y,y+delta)
    #for ligne in grille:
    #    print(ligne)
    #print()
    if delta ==2:
        
        maj_tableau(grille,x,y,orientation)
        
    else:
        delta=delta//2
        maj_tableau(grille,x+delta-1,y+delta-1,orientation)
        resoudre_tableau(grille,x,y,delta)
        resoudre_tableau(grille,x+delta,y,delta)
        resoudre_tableau(grille,x,y+delta,delta)
        resoudre_tableau(grille,x+delta,y+delta,delta)        



nb_case = 8    
longueur= 512
dimension = longueur // nb_case    
ma_grille=creation_tableau(nb_case) 
dessiner_grille(nb_case, longueur) 
coord_case_noire = case_noire(ma_grille)
dessiner_case_noire(coord_case_noire[0], coord_case_noire[1],dimension, longueur) 
resoudre_tableau(ma_grille, 0, 0, nb_case)
for ligne in ma_grille:
    print(ligne)
# print(trouve_case_occupee(ma_grille, 0, 0, 8))