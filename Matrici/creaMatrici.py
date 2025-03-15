import random

# Crea una matrice mxn di valore
def creaMatriceValore(m, n, valore):
    matr = []
    for i in range(m):
        riga = []
        for j in range(n):
            riga.append(valore)
        matr.append(riga)
    return matr

# Crea una matrice mxn di zeri
def creaMatriceZeri(m, n):
    matr = []
    for i in range(m):
        riga = []
        for j in range(n):
            riga.append(0)
        matr.append(riga)
    return matr

# oppure, siccome nelle righe superiori è definito un metodo creaMatriceValore usiamo quello passando 0
def creaMatriceZeri2(m, n):
    return creaMatriceValore(m, n, 0)

# Crea una matrice mxn di numeri random da min a max
def creaMatriceRandom(m, n, min, max):
    matr = []
    for i in range(m):
        riga = []
        for j in range(n):
            numRandom  = random.randint(min, max)
            riga.append(numRandom)
        matr.append(riga)
    return matr

# Crea una matrice quadrata nxn di zeri
def creaMatriceQuadrata(n):
    matr = []
    for i in range(n):
        riga = []
        for j in range(n):
            riga.append(0)
        matr.append(riga)
    return matr