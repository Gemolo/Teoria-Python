class Persona:
    
    # Costruttore
    def __init__(self, name, surname, matricola) -> None:
        self.name = name
        self.surname = surname
        self.matricola = matricola
        self.corsi = []
    
    def inserisciCorso(self, corso):
        self.corsi.append(corso)
        
    def getCorso(self, matricola):
        for corso in self.corsi:
            if corso.getMatricola() == matricola:
                return corso
        raise("Il corso non esiste")
    
    # Getters
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getMatricola(self):
        return self.matricola
    
    # Setters    
    def setName(self, name):
        self.name = name
    
    def setSurname(self, surname):
        self.surname = surname
    
    def setMatricola(self, matricola):
        self.matricola = matricola
    
    