class Corso:
    
    # Costruttore
    def __init__(self, nome, matricola, durata):
        self.nome = nome
        self.matricola = matricola
        self.durata = durata
    
    # Getters
    def getNome(self):
        return self.nome
    
    def getMatricola(self):
        return self.matricola
    
    def getDurata(self):
        self.durata
    
    # Setters
    def setNome(self, nome) -> None:
        self.nome = nome
    
    def setMatricola(self, matricola) -> None:
        self.matricola = matricola
    
    def setDurata(self, durata) -> None:
        self.durata = durata
