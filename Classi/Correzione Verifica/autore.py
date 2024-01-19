class Autore:

    def __init__ (self, nome, cognome):
        self.nome = nome
        self.cogome = cognome
    
    def info(self):
        return self.nome + " " + self.cognome