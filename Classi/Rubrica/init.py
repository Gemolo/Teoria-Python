dizionario = {     
            #   Chiave    Valore
            #   nome      cognome
                "Kevin Gemolo": "2323",
                "Mario Rossi": "43242",
                "X Y"     : "14141241"
              }

def trovaContattoIniziale(iniziale):
        output = []
        contatti = dizionario.items()
        for nome, email in contatti:
            print(nome.split(' ')[1][0])
            if nome.split(' ')[1][0] == iniziale:
                output.append(email)
        return output

print(trovaContattoIniziale('G'))

