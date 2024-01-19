from docente import Docente
from studente import Studente
from corso import Corso
from scuola import Scuola

def init():
    scuola = Scuola("Liceo Morin", "00")
    scuola.inserisciCorso("Informatica", "00", "Annuale")
    scuola.inserisciCorso("Matematica", "01", "Annuale")
    scuola.inserisciCorso("Fisica", "02", "Trimestre")
    scuola.inserisciCorso("Italiano", "03", "Pentamestre")
    # print(scuola.getCorso("00").getNome())
    
    informatica = scuola.getCorso("00")
    
    kevin = Docente("Kevin", "Gemolo", "00000")
    
    kevin.inserisciCorso(informatica)
    print(kevin.getCorso("00"))
    
    marco = Studente("Marco","f", "22")
    marco.inserisciCorso(informatica)
    
init()
    