from persona import Persona
from corso import Corso

class Studente(Persona):
    
    # Costruttore
    def __init__(self, name, surname, matricola) -> None:
        super().__init__(name, surname, matricola)
        
    
    