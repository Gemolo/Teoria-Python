

# Somma matrice
def sommaMatrice(matr):
    somma = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            somma += matr[i][j]
    return somma

# Lunghezza matrice
def lenMatrice(matr):
    lun = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            lun += 1
    return lun

# Lunghezza matrice ottimizzato
def lenMatriceMigliore(matr):
    lun  = 0
    for i in range(len(matr)):
        lun += len(matr[i])
    return lun

# Media di una matrice
def mediaMatrice(matr):
    somma = sommaMatrice(matr)
    lun = lenMatrice(matr)
    return somma / lun

