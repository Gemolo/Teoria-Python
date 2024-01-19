from veicolo import Veicolo  # Importa la classe "Veicolo" dal file "veicolo.py"

class AutoElettrica(Veicolo):
    def __init__(self, marca, modello, autonomia):
        super().__init__(marca, modello)
        self.autonomia = autonomia

    # def stampa_autonomia(self):
    #     return f"Autonomia della {self.marca} {self.modello}: {self.autonomia} chilometri"
