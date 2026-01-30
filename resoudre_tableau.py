def resoudre_tableau(grille,x,y,delta):
    orientation=trouve_case_occupee(grille, x, y, delta)
    print(orientation, x, x+delta, y,y+delta)
   
    if delta ==2:
        
        maj_tableau(grille,x,y,orientation)
        
    else:
        delta=delta//2
        maj_tableau(grille,x+delta-1,y+delta-1,orientation)
        resoudre_tableau(grille,x,y,delta)
        resoudre_tableau(grille,x+delta,y,delta)
        resoudre_tableau(grille,x,y+delta,delta)
        resoudre_tableau(grille,x+delta,y+delta,delta)        
