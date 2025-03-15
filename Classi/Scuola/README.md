# 🏫 Programmazione Orientata agli Oggetti - Sistema Scolastico

Questo repository contiene un esempio pratico di **Programmazione Orientata agli Oggetti (OOP) in Python**, applicato alla gestione di un **sistema scolastico** con corsi, docenti e studenti.

## 📂 Struttura del Repository

- **`persona.py`** → Definizione della classe `Persona`, da cui derivano `Studente` e `Docente`.
- **`studente.py`** → Implementazione della classe `Studente`.
- **`docente.py`** → Implementazione della classe `Docente`.
- **`corso.py`** → Implementazione della classe `Corso`, che include docenti e studenti.
- **`scuola.py`** → Definizione della classe `Scuola`, che gestisce i corsi.
- **`init.py`** → File principale per eseguire il programma e testare la scuola.

## 🏗️ Concetti Utilizzati

- **Classi e Oggetti** → Rappresentazione di persone, studenti, docenti, corsi e scuola.
- **Ereditarietà** → `Studente` e `Docente` ereditano da `Persona`.
- **Associazione tra classi** → Un corso ha studenti e un docente, una scuola ha più corsi.

## 🔹 Definizione della Classe `Persona`

```python
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f"{self.nome} {self.cognome}"
```

## 🎓 Classe `Studente`

```python
class Studente(Persona):
    def __init__(self, nome, cognome, matricola):
        super().__init__(nome, cognome)
        self.matricola = matricola
```

## 👨‍🏫 Classe `Docente`

```python
class Docente(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia
```

## 📖 Classe `Corso`

```python
class Corso:
    def __init__(self, nome, docente):
        self.nome = nome
        self.docente = docente
        self.studenti = []
    
    def aggiungi_studente(self, studente):
        self.studenti.append(studente)
```

## 🏫 Classe `Scuola`

```python
class Scuola:
    def __init__(self, nome):
        self.nome = nome
        self.corsi = []
    
    def aggiungi_corso(self, corso):
        self.corsi.append(corso)
```

## 🎬 Esecuzione del Programma (`init.py`)

```python
def main():
    docente = Docente("Mario", "Rossi", "Matematica")
    corso = Corso("Analisi 1", docente)
    
    studente1 = Studente("Luca", "Bianchi", "12345")
    studente2 = Studente("Anna", "Verdi", "67890")
    
    corso.aggiungi_studente(studente1)
    corso.aggiungi_studente(studente2)
    
    scuola = Scuola("Liceo Galileo")
    scuola.aggiungi_corso(corso)
    
    print(f"Scuola: {scuola.nome}")
    for corso in scuola.corsi:
        print(f"Corso: {corso.nome}, Docente: {corso.docente}")
        for studente in corso.studenti:
            print(f" - Studente: {studente}")

if __name__ == "__main__":
    main()
```

### 📌 Output Atteso
```
Scuola: Liceo Galileo
Corso: Analisi 1, Docente: Mario Rossi
 - Studente: Luca Bianchi
 - Studente: Anna Verdi
```

## 🎯 Obiettivo del Progetto

- Simulare un **sistema scolastico** con corsi, docenti e studenti.
- Comprendere l'uso di **ereditarietà** e **associazione tra classi**.
- Applicare i concetti di **OOP in Python** per gestire più entità.

