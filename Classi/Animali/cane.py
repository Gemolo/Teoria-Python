from animale import Animale

class Cane(Animale):

    def __init__(self, nome, eta, razza) -> None:
        super().__init__(nome, eta)
        self.razza = razza

    # Qui inserisco i metodi astratti.   

    def info(self):
        return self.razza

    def parla(self):
        return "abbaia"

    def muove(self):
        return "corre"

    def mangia(self):
        return "mangia"

    def beve(self):
        return "beve"

    # Metodi normali

    

    # Getters e Setters

    def getRazza(self):
        return self.razza
    
    def setRazza(self, razza):
        self.razza = razza
