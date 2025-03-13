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


# Testing
def init():
    vettore = [1,2,3,4,5,6,7,8,9,10]

    # Esercizio 1
    stampa(vettore)

    # Esercizio 2
    print(f"La somma del vettore è {somma(vettore)}")

init()