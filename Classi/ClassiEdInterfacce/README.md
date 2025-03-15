# 🚲 Programmazione Orientata agli Oggetti - Mezzi di Trasporto

Questo repository contiene un esempio di utilizzo della **Programmazione Orientata agli Oggetti (OOP)** in Python, applicata ai **mezzi di trasporto**.

## 📂 Struttura del Repository

- **`mezzo.py`** → Definizione della classe astratta `Mezzo`.
- **`bicicletta.py`** → Implementazione della classe `Bicicletta`, derivata da `Mezzo`.
- **`init.py`** → File principale per eseguire il programma e testare le classi.

## 🏗️ Concetti Utilizzati

- **Classi astratte** → Definizione di un'interfaccia comune per tutti i mezzi di trasporto.
- **Ereditarietà** → Ogni mezzo eredita caratteristiche dalla classe `Mezzo`.
- **Polimorfismo** → Ogni mezzo implementa il proprio comportamento specifico.

## 🔹 Definizione della Classe Astratta `Mezzo`

```python
from abc import ABC, abstractmethod

class Mezzo(ABC):
    def __init__(self, nome, velocita):
        self.nome = nome
        self.velocita = velocita
    
    @abstractmethod
    def descrizione(self):
        pass
```

## 🚲 Classe `Bicicletta`

```python
class Bicicletta(Mezzo):
    def __init__(self, nome, velocita, tipo):
        super().__init__(nome, velocita)
        self.tipo = tipo
    
    def descrizione(self):
        return f"{self.nome} è una bicicletta di tipo {self.tipo} con velocità massima di {self.velocita} km/h."
```

## 🎬 Esecuzione del Programma (`init.py`)

```python
def main():
    bici = Bicicletta("Mountain Bike", 25, "Off-road")
    print(bici.descrizione())

if __name__ == "__main__":
    main()
```

### 📌 Output Atteso
```
Mountain Bike è una bicicletta di tipo Off-road con velocità massima di 25 km/h.
```

## 🎯 Obiettivo del Progetto

- Comprendere come utilizzare le **classi astratte** per definire interfacce comuni.
- Applicare **ereditarietà e polimorfismo** per gestire più tipi di mezzi di trasporto.
- Strutturare un progetto Python con più file e classi ben organizzate.
