# In Python, i cicli sono strutture di controllo che consentono di eseguire un blocco di istruzioni ripetutamente. Ci sono due tipi principali di cicli in Python: il ciclo for e il ciclo while. Vediamo come usarli.

# Ciclo for:
# Il ciclo for è comunemente utilizzato per iterare su una sequenza (come una lista, una tupla, una stringa o un range). Ecco un esempio di come utilizzarlo:

# Esempio di ciclo for con una lista

frutta = ["mela", "banana", "kiwi"]

for frutto in frutta:
    print(frutto)
    
# Output:
# mela
# banana
# kiwi

# In questo esempio, il ciclo for itera su ogni elemento della lista frutta e stampa ogni elemento.

# Puoi anche utilizzare la funzione range per generare una sequenza di numeri e iterare attraverso di essa:

# Esempio di ciclo for con range
for numero in range(1, 5):  # Genera una sequenza da 1 a 4
    print(numero)
    
# Output:

# 1
# 2
# 3
# 4


# Ciclo while:
# Il ciclo while esegue un blocco di istruzioni fintanto che una condizione specificata è vera. Ecco un esempio:

# Esempio di ciclo while
contatore = 0

while contatore < 5:
    print(contatore)
    contatore += 1
    
# Output:
    
# 0
# 1
# 2
# 3
# 4

# In questo esempio, il ciclo while continua ad eseguire il blocco di istruzioni finché la condizione contatore < 5 è vera. È importante assicurarsi che la condizione alla fine diventi falsa per evitare un ciclo infinito.

# Istruzioni break e continue:
# break: Termina prematuramente il ciclo.
# continue: Salta il resto del blocco e passa alla successiva iterazione del ciclo.

# Esempio di break e continue
for numero in range(1, 10):
    if numero == 5:
        break  # Termina il ciclo quando numero è uguale a 5
    if numero % 2 == 0:
        continue  # Salta le iterazioni per numeri pari
    print(numero)
    
    
# Output:

1
3