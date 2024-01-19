from autore import Autore
from libro import Libro

class Biblioteca():

    def __init__(self, nome):
        self.nome = nome
        self.libri = []
    
    def aggiungiLibro(self, libro):
        self.libri.append(libro)

    def autoreLibri(self, autore):
        libriAutore = []
        for libro in self.libri:
            if autore.info() == libro.Autore.info():
                libriAutore.append(libro)
        return libro
    
    def elencaLibri(self):
        libri = ""
        for libro in self.libri:
            libri.append(libro.info() + "/n")
        return libri

