from abc import abstractmethod

class Mezzo:

    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca
    
    @abstractmethod
    def tipoDiPatente(self):
        return "Non definito"