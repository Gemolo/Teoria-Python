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

# triangoloSuperiore
def sommaTriangoloSuperioreMatrice(matr):
    sommaTS = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if j > i:
                sommaTS += matr[i][j]
    return sommaTS

# triangoloInferiore
def sommaTriangoloInferioreMatrice(matr):
    sommaIS = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if j < i:
                sommaIS += matr[i][j]
    return sommaIS

# m = [
#       [1,2,3],
#       [4,5,6]
#       [7,8,9]

# Output -> [2,3,6]

# Somma elementi della diagonaleDxSx
def sommaElementiDiagonaleDxSx(matr):
    somma = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i + j == len(matr) - 1:
                somma += matr[i][j]
    return matr

# Una matrice è bilanciata se la somma del traingolare sup meno la somma del triangolare superiore
# è pari a zero
def isBilanciata(matr):
    sommaSup = 0
    sommaInf = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i < j:
                sommaSup += matr[i][j]
            if i > j:
                sommaInf += matr[i][j]
    return sommaSup - sommaInf == 0

# Diagonale da SxDx meno DxSx
def differenzaDiagonali(matr):
    diff = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i == j:
                diff += matr[i][j]
            if i + j == len(matr) - 1:
                diff -= matr[i][j]
    return diff

# Controllare se un elemento elem è contenuto nella matrice matr
def isContains(elem, matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] == elem:
                return True
    return False






