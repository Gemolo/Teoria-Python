# Somma tra matrici di pari dimensioni e quadrate
def sommaMatrici(matr1, matr2):
    matr3 = []
    for i in range(len(matr1)):
        for j in range(len(matr1[i])):
            matr3.append(matr1[i][j] + matr2[i][j])
    return matr3

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

# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# print(prodottoMatrici(A, B))
