from persona import Persona

class Docente(Persona):
    
    # Costruttore
    def __init__(self, name, surname, matricola) -> None:
        super().__init__(name, surname, matricola)
        