def trouve_case_occupee(grille, x, y, delta):
    for i in range(x,x+delta):
        for j in range(y,y+delta):
            if grille[i][j]!=0:
                if i < delta//2 and j < delta//2:
                    return "BD"
                elif i >= delta//2 and j >= delta//2:
                    return"HG"
                elif i < delta//2 and j >= delta//2: 
                    return"BG"
                else:
                    return"HD"
