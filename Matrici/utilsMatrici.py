######## LEN ################

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





########## STAMPE #############

# Stampa matrice
def stampaMatrice(matr):
    for i in range(len(matr)):
        print("")
        for j in range(len(matr[i])):
            print(f"\t{matr[i][j]}", end = " ")
        print("")





########## SOMME ##############

# Somma matrice
def sommaMatrice(matr):
    somma = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            somma += matr[i][j]
    return somma

# Somma per Riga
def sommaRigheMatrice(matr):
    somme = []
    for i in range(len(matr)):
        somma = 0
        for j in range(len(matr[i])):
            somma += matr[i][j]
        somme.append(somma)
    return somme

# Somma per Colonna
def sommaColonneMatrice(matr):
    somme = []
    for j in range(len(matr)):
        somma = 0
        for i in range(len(matr[j])):
            somma += matr[i][j]
        somme.append(somma)
    return somme

# Somma elementi della diagonaleDxSx
def sommaElementiDiagonaleDxSx(matr):
    somma = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i + j == len(matr) - 1:
                somma += matr[i][j]
    return matr

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

# Somma tra matrici di pari dimensioni e quadrate
def sommaMatrici(matr1, matr2):
    matr3 = []
    for i in range(len(matr1)):
        riga = []
        for j in range(len(matr1[i])):
            riga.append(matr1[i][j] + matr2[i][j])
        matr3.append(riga)
    return matr3

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




########## PRODOTTI ##############

# Prodotto scalare
def moltiplica_scalare(matrice, k):
    nuova_matrice = []
    for riga in matrice:
        nuova_riga = []
        for elemento in riga:
            nuova_riga.append(elemento * k)
        nuova_matrice.append(nuova_riga)
    return nuova_matrice

# Prodotto tra due matrici di pari dimensioni e quadrate
def prodottoMatrici(matr1, matr2):
    matr3 = []
    for i in range(len(matr1)):
        riga = []
        for j in range(len(matr2[i])):
            c = 0
            for k in range(len(matr2)):
                c += matr1[i][k] * matr2[k][j]
            riga.append(c)
        matr3.append(riga)
    return matr3

########## MEDIE ##################

# Media di una matrice
def mediaMatrice(matr):
    somma = sommaMatrice(matr)
    lun = lenMatrice(matr)
    return somma / lun

# m = [
#       [1,2,3],
#       [4,5,6]
#       [7,8,9]

# Output -> [2,3,6]

######### FUNZIONI  BOOLEANE ##############

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

# Controllare se un elemento elem è contenuto nella matrice matr
def isContains(elem, matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] == elem:
                return True
    return False

# Una matrice è diagonale se tutti gli elementi fuori dalla diagonale principale sono zero.
def isDiagonale(matr):
    isDiag = True
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i != j:
                if matr[i][j] != 0:
                    isDiag = False
    return isDiag






########## FUNZIONI CONTA ##############

# Conta numeri pari in una matrice
def contaPari(matr):
    count = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] % 2 == 0:
                count += 1
    return count



########## FUNZIONI RETURN MATRICE #######

# Trasposta
def trasponi_matrice(matrice):
    trasposta = []
    for j in range(len(matrice)):
        trasposta_riga = []
        for i in range(len(matrice[0])):
            trasposta_riga.append(matrice[i][j])
        trasposta.append(trasposta_riga)
    return trasposta

# Rotazione della matrice di 90 gradi in senso orario
def ruota_90(A):
    ruotata = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ruotata[j][2-i] = A[i][j]  # Ruota di 90° in senso orario
    return ruotata