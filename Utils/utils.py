####################   INPUT   ###########################################################################

# In Python, puoi ottenere input dall'utente utilizzando la funzione input().
# Ecco un semplice tutorial su come farlo:

# Prendere un input dall'utente e stamparlo
nome = input("Inserisci il tuo nome: ")
print("Ciao, " + nome + "!")

# L'input di default è una stringa, quindi se vuoi un numero, devi convertirlo
eta = input("Quanti anni hai? ")
eta = int(eta)  # Converti la stringa in un intero

# Puoi anche ottenere input in una sola riga
colore_preferito = input("Il tuo colore preferito: ")

print(nome + " ha " + str(eta) + " anni e il suo colore preferito è " + colore_preferito + ".")

# In questo esempio, la funzione input() viene utilizzata per ottenere l'input dell'utente.
# È importante notare che input() restituisce sempre una stringa, anche se l'utente inserisce un numero.
# Se hai bisogno di trattare l'input come un numero, devi convertirlo usando le funzioni int() o float().

# Ricorda che l'input dell'utente può essere sensibile alle maiuscole/minuscole,
# quindi se stai cercando di corrispondere a una stringa specifica,
# potrebbe essere utile convertire l'input in minuscolo o maiuscolo per uniformità:

risposta = input("Vuoi continuare? (sì/no): ").lower()

if risposta == "sì":
    print("Continuando...")
else:
    print("Interrompendo...")

# In questo modo, anche se l'utente inserisce "SÌ" o "sÌ",
# verrà comunque considerato come "sì".

##########################################################################################################


###################   RANDOM    ##########################################################################

#  In Python, puoi utilizzare il modulo random per generare numeri casuali.
# Ecco un tutorial su come generare numeri interi casuali:

import random

# Generare un numero intero casuale tra un intervallo specificato
numero_casuale = random.randint(1, 100)
print("Numero casuale tra 1 e 100:", numero_casuale)

# Puoi generare numeri casuali anche da un range
numero_casuale_range = random.randrange(1, 101, 2)  # Numeri dispari tra 1 e 100
print("Numero casuale tra 1 e 100 (solo dispari):", numero_casuale_range)

# Per generare numeri casuali float tra 0 e 1
numero_float_casuale = random.random()
print("Numero float casuale tra 0 e 1:", numero_float_casuale)

# Puoi anche mischiare una lista in modo casuale
lista_originale = [1, 2, 3, 4, 5]
random.shuffle(lista_originale)
print("Lista mischiata:", lista_originale)


# Spiegazioni:

# random.randint(a, b):                  Restituisce un numero intero casuale nell'intervallo tra a e b inclusi.
# random.randrange(start, stop, step):   Restituisce un numero casuale dall'intervallo di numeri generati da start a stop (escluso), con uno specificato passo.
# random.random():                       Restituisce un numero float casuale compreso tra 0 (incluso) e 1 (escluso).
# random.shuffle(sequence):              Mescola gli elementi di una sequenza (come una lista) in modo casuale.
# Questi sono solo alcuni esempi delle funzionalità offerte dal modulo random in Python per generare numeri casuali. Puoi adattare queste funzioni alle tue esigenze specifiche.