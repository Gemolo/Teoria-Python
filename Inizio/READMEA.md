# 🐍 Introduzione a Python

Questo repository contiene esempi di base sul linguaggio di programmazione **Python**, illustrando concetti fondamentali come variabili, tipi di dati, metodi e operazioni.

## 📂 Contenuto del Repository

### 🔹 Linguaggio di Programmazione
- Python è un linguaggio **non tipizzato**.
- Permette di scrivere codice che viene eseguito come **algoritmi**.
- Usato per risolvere problemi di vario tipo.

### 🏗️ Variabili e Tipi di Dati
- **Variabili**: contenitori di informazioni che possono variare nel tempo.
- **Tipi di variabili**:
    - `int`: numeri interi.
    - `double` (float in Python): numeri con la virgola.
    - `string`: parole o testo, es. "Ciao".
    - `char`: singoli caratteri.
    - `boolean`: `True` o `False` (vero o falso).

### ✍️ Commenti in Python
- Tutto ciò che è scritto dopo `#` è un **commento**, quindi non viene eseguito dal programma.

### 🔢 Operazioni
- **Cast di variabili**: trasformare una variabile in un altro tipo.
  ```python
  num = 5
  parola = "casa"
  print(str(num) + parola)  # Concatena numero e stringa
  ```
- **Modulo** `%`: restituisce il resto della divisione.
  ```python
  print(5 % 2)  # Output: 1
  print(6 % 2)  # Output: 0
  ```

### ⚙️ Metodi (Funzioni)
- I **metodi** sono blocchi di codice che possono essere richiamati per eseguire operazioni.
  ```python
  def somma(num1, num2):
      return num1 + num2
  ```
- Esempio di utilizzo:
  ```python
  risultato = somma(5, 6)
  print(risultato)  # Output: 11
  ```

### ⌨️ Scorciatoie da Tastiera
- **CTRL + ù** → Commentare/Decommentare il codice.
- **CTRL + S** → Salvare il file.

## 📝 Esempio di Programma
```python
def init():
    print("Sono fuori dal metodo")
    dimmiCiao(1, 0, 6)
    risultato = somma(8, 7)
    print(risultato)

def dimmiCiao(num1, num2, num3):
    print("Ciao")
    print(num1)

def somma(num1, num2):
    return num1 + num2

init()
```

## 🤝 Contributi
Se vuoi contribuire, fai un fork del repository, crea un nuovo branch, apporta le modifiche e invia una pull request! 🚀

## ⚖️ Licenza
Questo progetto è distribuito sotto la licenza MIT.
