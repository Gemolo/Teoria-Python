from mezzo import Mezzo

class Bicicletta(Mezzo):

    def __init__(self, nome, marca):
        super().__init__(nome, marca)
    
    # @abstractmethod
    def tipoDiPatente(self):
        return "Nessuna"

