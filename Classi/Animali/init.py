import random
from cane import Cane
from leone import Leone
from cavallo import Cavallo
import time

def numeroCasuale(min, max):
    return random.randint(min, max)

def getNomeCasuale():
    listaNomi = ["Mario", "Beppe", "Luca", "Marco", "Beatrice", "Sara", "Marta"]
    return listaNomi[numeroCasuale(0, len(listaNomi) - 1)]

def popola():
    listaOggetti =[]
    numeroRandom = numeroCasuale(1, 7)

    for i in range(numeroRandom - 1):
        # Istanzio l'oggetto Cane
        cane = Cane(getNomeCasuale(), numeroCasuale(0,20), "Barboncino")
        listaOggetti.append(cane)

        # Istanzio l'oggetto Cavallo
        cavallo = Cavallo(getNomeCasuale(), numeroCasuale(0,20), "Rosso")
        listaOggetti.append(cavallo)

        # Istanzio l'oggetto Leone
        leone = Leone(getNomeCasuale(), numeroCasuale(0, 10), numeroCasuale(50, 100))
        listaOggetti.append(leone)
    
    return listaOggetti
        


def init():
    animali = popola()
    # print(animali[0].info())

    for i in range(20):
        stringa = " "
        numeroRandom = numeroCasuale(0, len(animali) - 1)
        animaleCasuale = animali[numeroRandom]
        stringa = str(animaleCasuale.info()) + " " + str(animaleCasuale.mangia())

        operazioneCasuale = numeroCasuale(0,4)
        if operazioneCasuale == 0:
            stringa += " Operazione: info()"
        elif operazioneCasuale == 1:
            stringa += " Operazione: parla()"
        elif operazioneCasuale == 2:
            stringa += " Operazione: corri()"
        elif operazioneCasuale == 3:
            stringa += " Operazione: mangia()"
        elif operazioneCasuale == 4:
            stringa += " Operazione: bevi()"
        print(stringa)
        time.sleep(1)

    return 1
    
init()
