from veicolo import Veicolo

class MotoElettrica(Veicolo):
    
    def __init__(self, marca, modello, potenzaWatt):
        super().__init__(marca, modello)
        self.potenzaWatt = potenzaWatt
    
    def stampa_autonomia(self) -> str:
        return f"Autonomia della {self.marca} {self.modello}: {self.potenzaWatt} chilometri"
    