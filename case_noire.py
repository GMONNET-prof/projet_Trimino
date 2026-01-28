from random import *
def case_noires(tab):
    x = randint(0, len(tab)-1)
    y = randint(0, len(tab)-1)
    tab[x][y] = -1
    return  (x,y)
