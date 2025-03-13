def stampa(vettore):
    for i in range(len(vettore)):
        print(f"{vettore[i]}, ", end=" ")
    print(f"")

def somma(vettore):
    som = 0
    for i in range(len(vettore)):
        som += vettore[i]
    return som

def contains(elem, vettore):
    for i in range(len(vettore)):
        if vettore[i] == elem:
            return True
    return False

def raddoppiaNumero(vettore):
    for i in range(len(vettore)):
        vettore[i] *= 2
    return vettore

def reverseVettore(vettore):
    rev = []
    for i in range(len(vettore) - 1, 0, -1):
        rev.append(vettore[i])
    return rev

def contaPari(vettore):
    count = 0
    for i in range(len(vettore)):
        if vettore[i] % 2 == 0:
            count += 1
    return count

def media(vettore):
    somma = 0
    for i in range(len(vettore)):
        somma += vettore[i]
    return somma/len(vettore)

# Testing
def init():
    vettore = [1,2,3,4,5,6,7,8,9,10]

    # Esercizio 1
    stampa(vettore)

    # Esercizio 2
    print(f"La somma del vettore è {somma(vettore)}")

init()