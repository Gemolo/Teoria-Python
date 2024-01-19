from animale import Animale

class Cavallo(Animale):

    def __init__(self, nome, eta, mantello) -> None:
        super().__init__(nome, eta)
        self.mantello = mantello

    # Qui inserisco i metodi astratti.   

    def info(self):
        return self.mantello

    def parla(self):
        return "nitrisce"

    def muove(self):
        return "galoppa"

    def mangia(self):
        return "mangia"

    def beve(self):
        return "si abbevera"

    # Metodi normali

    

    # Getters e Setters

    def getMantello(self):
        return self.mantello
    
    def setMantello(self, mantello):
        self.mantello = mantello