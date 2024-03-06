# README: ⚙️ Utils 🎨

## 📚 Cambio colore terminale di Python

Con la classe bcolors potete cambiare il colore della chat del vostro terminale

**Esempio:**
```python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKGREEN} Colore in verde! {bcolors.ENDC}")
```

## Random 🎰

Random vi permette di generare numeri casuali e scelte casuali per i vostri esercizi

**Esempio:**
```python
import random

# Generare un numero intero casuale tra un intervallo specificato
numero_casuale = random.randint(1, 100)
print("Numero casuale tra 1 e 100:", numero_casuale)
```

## Input 🤖

Input vi permette di chiedere all'utente delle informazioni

**Esempio:**
```python
# In Python, puoi ottenere input dall'utente utilizzando la funzione input().
# Ecco un semplice tutorial su come farlo:

# Prendere un input dall'utente e stamparlo
nome = input("Inserisci il tuo nome: ")
print("Ciao, " + nome + "!")
```


