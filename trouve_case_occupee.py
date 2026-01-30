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
