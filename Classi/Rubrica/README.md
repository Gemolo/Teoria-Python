# 📞 Programmazione Orientata agli Oggetti - Rubrica Contatti

Questo repository contiene un esempio pratico di **Programmazione Orientata agli Oggetti (OOP) in Python**, applicato alla gestione di una **rubrica dei contatti**.

## 📂 Struttura del Repository

- **`rubrica.py`** → Definizione della classe `Rubrica`, che gestisce una lista di contatti.
- **`init.py`** → File principale per eseguire il programma e testare la rubrica.
- **`output.txt`** → File di output che memorizza i contatti salvati nella rubrica.

## 🏗️ Concetti Utilizzati

- **Classi e Oggetti** → Rappresentazione dei contatti e della rubrica con classi.
- **Gestione file** → Salvataggio dei contatti su un file `.txt`.
- **Metodi per gestione contatti** → Aggiunta, rimozione e visualizzazione dei contatti.

## 🔹 Definizione della Classe `Rubrica`

```python
class Rubrica:
    def __init__(self):
        self.contatti = []
    
    def aggiungi_contatto(self, nome, email):
        self.contatti.append(f"{nome} : {email}")
    
    def mostra_contatti(self):
        for contatto in self.contatti:
            print(contatto)
    
    def salva_su_file(self, filename="output.txt"):
        with open(filename, "w") as file:
            for contatto in self.contatti:
                file.write(contatto + "\n")
```

## 📋 Esecuzione del Programma (`init.py`)

```python
def main():
    rubrica = Rubrica()
    rubrica.aggiungi_contatto("Kevin Gemolo", "kevingemolo@fafa.it")
    rubrica.mostra_contatti()
    rubrica.salva_su_file()

if __name__ == "__main__":
    main()
```

### 📌 Output Atteso (`output.txt`)
```
Kevin Gemolo : kevingemolo@fafa.it
```

## 🎯 Obiettivo del Progetto

- Simulare una **rubrica digitale** con funzionalità di aggiunta e gestione contatti.
- Applicare **OOP** con metodi per manipolare i dati.
- Utilizzare la **gestione file in Python** per salvare e caricare i contatti.
