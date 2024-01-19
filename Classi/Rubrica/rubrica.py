class Rubrica:

    def __init__(self, dizionario) -> None:
        self.dizionario = dizionario

    def aggiungiContatto(self, nomeCognome, email):
        self.dizionario[nomeCognome] = email

    def suFile(self):
        f = open("Scuola/Morin/Informatica/3Csa/Classi/Rubrica/rubrica.txt", "w")
        contatti = self.dizionario.items()
        for nome, email in contatti:
            f.write(nome + " : " + email)
        f.close()
    
    def trovaContattoIniziale(self, iniziale):
        output = []
        contatti = self.dizionario.items()
        for nome, email in contatti:
            if nome.split(' ')[1][0] == iniziale:
                output.append(email)
        return output
    
    def stampaRubrica(self):
        contatti = self.dizionario.items()
        for nome, email in contatti:
            print(nome + " : " + email)
    
    