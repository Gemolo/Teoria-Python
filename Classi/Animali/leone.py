from animale import Animale

class Leone(Animale):

    def __init__(self, nome, eta, peso) -> None:
        super().__init__(nome, eta)
        self.peso = peso

    # Qui inserisco i metodi astratti.   

    def info(self):
        return self.peso

    def parla(self):
        return "ruggisce"

    def muove(self):
        return "va come un fulmine"

    def mangia(self):
        return "divora"

    def beve(self):
        return "ingurgita"

    # Metodi normali

    

    # Getters e Setters

    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso
