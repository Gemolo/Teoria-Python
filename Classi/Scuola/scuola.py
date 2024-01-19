from corso import Corso
class Scuola:
    
    def __init__(self, nome, codice) -> None:
        self.nome = nome
        self.codice = codice
        self.corsi = []
        
    #metodo per inserire un corso alla lista dei corsi
    def inserisciCorso(self, nome, matricola, durata):
        # Istanziamo l'oggetto
        corso = Corso(nome, matricola, durata)
        self.corsi.append(corso)
    
    def printCorsi(self):
        for corso in self.corsi:
            print("nome: " + corso.nome + "  matricola: " + corso.matricola + "   durata:" + corso.durata)
    
    def getCorso(self, matricola):
        for corso in self.corsi:
            if corso.getMatricola() == matricola:
                return corso
        raise("Il corso non esiste")