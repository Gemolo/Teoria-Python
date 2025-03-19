import os

def creaMatrice(m, n):
    matrice = []
    for i  in range (m):
        riga = []
        for j in range(n):
            riga.append("-")
        matrice.append(riga)
    return matrice

def stampaMatrice(matrice):
    print("[")
    for i in range (len(matrice)):
        print("\t[", end=" ")
        for j in range(len(matrice[i])):
            print(f"{matrice[i][j]}", end=" ")
        print("]")
    print("]")


def inserisciMossa(i, j, turno):
    if matr[i][j] != "-":
        return False
    if turno:
        matr[i][j] = "X"
    else:
        matr[i][j] = "O"
    return True

def simboli(vettore):
    count = 0
    for i in range(len(vettore)):
        if vettore[i] == "X":
            count += 1

        if vettore[i] == "O":
            count += -1

        if vettore[i] == "-":
            count += 0
    return count

# Data una matrice e un indice di riga ritornare la riga
def getRiga(i):
    return matr[i]

def getColonna(col):
    colonna = []
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if j == col:
                colonna.append(matr[i][j])
    return colonna

def getDiagonaleSxDx():
    diagonalesdx = []
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i == j:
                diagonalesdx.append(matr[i][j])
    return diagonalesdx

def getDiagonaleDxSx():
    diagonaledsx = []
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if i + j == len(matr)-1:
                diagonaledsx.append(matr[i][j])
    return diagonaledsx

# TODO
# def controlla(numero):
#     match numero:
#             case 3:
#                 # Ha vinto X
#                 return 2
#             case -3:
#                 # Ha vinto O
#                 return 1
#             case _:
#                 # Nessuno vince
#                 print("Nessuna riga vincente")

def vittoria():
    vinto = -1

    diagSxDx = getDiagonaleSxDx()
    simboliDiagonaleSxDx = simboli(diagSxDx)

    match simboliDiagonaleSxDx:
        case 3:
            # Ha vinto X
            return 2
        case -3:
            # Ha vinto O
            return 1

    diagDxSx = getDiagonaleDxSx()
    simboliDiagonaleDxSx = simboli(diagDxSx)
    match simboliDiagonaleDxSx:
        case 3:
            # Ha vinto X
            return 2
        case -3:
            # Ha vinto O
            return 1

    for i in range(3):
        riga = getRiga(i)
        simboliRiga = simboli(riga)

        match simboliRiga:
            case 3:
                # Ha vinto X
                return 2
            case -3:
                # Ha vinto O
                return 1

        colonna = getColonna(i)
        simboliColonna = simboli(colonna)

        match simboliColonna:
            case 3:
                # Ha vinto X
                return 2
            case -3:
                # Ha vinto O
                return 1



turno = True
matr = creaMatrice(3,3)
mosse = 0
vinto = 0
# Gioco
while mosse < 9 and vinto != 2 and vinto != 1:
    # Per windows
    # os.system('cls')

    stampaMatrice(matr)
    if turno:
        print("Tocca a X")
    else:
        print("Tocca a O")
    i = int(input("Dimmi la coordinata x: "))
    j = int(input("Dimmi la coordinata y: "))
    if inserisciMossa(i, j, turno):
        mosse += 1
        turno = not turno
        vinto = vittoria()

if vinto == 2:
    print("VINCE X")
if vinto == 1:
    print("VINCE 0")
if mosse == 9:
    print("PAREGGIO")