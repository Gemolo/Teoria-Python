from abc import abstractmethod
import time

class Animale:

    def __init__(self, nome, eta) -> None:
        self.nome = nome
        self.eta = eta

    # Qui inserisco i metodi astratti.   

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def parla(self):
        pass

    @abstractmethod
    def muove(self):
        pass

    @abstractmethod
    def mangia(self):
        pass

    @abstractmethod
    def beve(self):
        pass



    # Metodi normali

    def dormi(self, secondi):
        time.sleep(secondi)

    

    # Getters e Setters

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getEta(self):
        return self.eta
    
    def setEta(self, eta):
        self.eta = eta



