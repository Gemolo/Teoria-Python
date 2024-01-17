# Linguaggio di programmazione
# Permette di scrivere del codice che si chiameranno poi algoritmi
# Permetto di risolvere problemi, spesso qualsiasi problema dell'utente

# Python    → linguaggio di programmazione non "tipizzato"

# Variabili
# Sono dei contenitori di informazioni che variano nel tempo, ma non nella loro natura

# Tipi di variabili
# int       → intero, ovvero un numero senza virgola
# double    → numeri con la virgola
# string    → parole, "Ciao", "Come"
# char      → caratteri
# boolean   → True e False, vero e falso

# Tutto questo scritto in verde è un commento, codice non eseguibile dal programma


num = 5

parola = "casa"

c = 5.6


# str( variabile ) → castando una variabile a stringa
# print(str(num) + parola)

# print(int(c))


# Shortcuts
# CTRL + ù → per fare commenti
# CTRL + s → per salvare


# Python è un linguaggio che lavora in cascata

# Metodi
# sono parte di codice raggruppato e chiamato all'occorenza



def dimmiCiao(num1, num2, num3, num4):
    print("Ciao")
    print("ff")
    print(num1)

# dimmiCiao(1,8,7,5)

def chiedimiComeSto():
    print("Come stai?")


def somma(num1, num2):
    return num1 + num2

# risultato = somma(5, 6)
# print(risultato)

# Operazione modulo → %
# 5 % 2 = 1
# 7 % 2 = 1
# 6 % 2 = 0


def init():
    print("Sono fuori dal metodo")

    dimmiCiao(1, 0, 6)

    risultato = somma(8 ,7)
    print(risultato)

init()