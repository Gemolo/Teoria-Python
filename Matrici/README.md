# 📌 Matrici in Python

Questo repository contiene una raccolta di funzioni per la manipolazione di matrici in Python. Le funzioni sono implementate senza l'uso di metodi integrati avanzati, rendendole didattiche e adatte per l'apprendimento dei concetti base sulla gestione delle matrici. 🧑‍💻

## 📂 Contenuto del Repository

### 🔢 Funzioni di Base
- **`lenMatrice(matr)`**: 📏 Calcola la lunghezza totale di una matrice.
- **`lenMatriceMigliore(matr)`**: 🚀 Versione ottimizzata per il calcolo della lunghezza.

### ➕ Operazioni sulle Matrici
- **Somma degli elementi**:
    - `sommaMatrice(matr)`: ➗ Restituisce la somma di tutti gli elementi.
    - `somma_colonne(matrice)`: 📊 Restituisce la somma degli elementi per colonna.
    - `somma_matrice(matrice)`: 📊 Restituisce la somma degli elementi per riga.
    - `sommaElementiDiagonaleDxSx(matr)`: 🔀 Somma degli elementi sulla diagonale principale.
    - `differenzaDiagonali(matr)`: 🔄 Differenza tra le due diagonali.

- **Operazioni sui triangoli della matrice**:
    - `sommaTriangoloSuperioreMatrice(matr)`: 🔼 Somma degli elementi sopra la diagonale principale.
    - `sommaTriangoloInferioreMatrice(matr)`: 🔽 Somma degli elementi sotto la diagonale principale.
    - `isBilanciata(matr)`: ⚖️ Verifica se la matrice è bilanciata.

- **Operazioni tra matrici**:
    - `sommaMatrici(matr1, matr2)`: 🔄 Somma tra due matrici di pari dimensioni.
    - `prodottoMatrici(matr1, matr2)`: ✖️ Prodotto tra due matrici quadrate.

### 🛠️ Funzioni Aggiuntive
- **Media della matrice**: `mediaMatrice(matr)` 🎯
- **Moltiplicazione per scalare**: `moltiplica_scalare(matrice, k)` 🏗️
- **Ricerca**:
    - `isContains(elem, matr)`: 🔍 Verifica se un elemento è contenuto nella matrice.
    - `contaPari(matr)`: 🔢 Conta il numero di elementi pari.
- **Trasposizione**: `trasponi_matrice(matrice)` 🔄

## 📝 Esempio di Utilizzo

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sommaMatrice(matrice))  # Output: 45
print(somma_colonne(matrice))  # Output: [12, 15, 18]
```

