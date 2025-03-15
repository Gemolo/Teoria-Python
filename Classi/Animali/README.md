# 🐍 Programmazione Orientata agli Oggetti - Classi Animali

Questo repository contiene un esempio di utilizzo della **Programmazione Orientata agli Oggetti (OOP)** in Python, con un focus sulla gestione di classi astratte e ereditarietà applicata agli **animali**.

## 📂 Struttura del Repository

- **`animale.py`** → Definizione della classe astratta `Animale`.
- **`cane.py`** → Implementazione della classe `Cane`, derivata da `Animale`.
- **`cavallo.py`** → Implementazione della classe `Cavallo`, derivata da `Animale`.
- **`leone.py`** → Implementazione della classe `Leone`, derivata da `Animale`.
- **`init.py`** → File principale per eseguire il programma e testare le classi.

## 🏗️ Concetti Utilizzati

- **Classi astratte** → Definizione di un'interfaccia comune per tutti gli animali.
- **Ereditarietà** → Ogni animale eredita caratteristiche dalla classe `Animale`.
- **Polimorfismo** → Ogni animale implementa il proprio comportamento specifico.

## 🔹 Definizione della Classe Astratta `Animale`

```python
from abc import ABC, abstractmethod

class Animale(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def fai_verso(self):
        pass
```

## 🦁 Classi Derivate

### **Classe `Cane`**
```python
class Cane(Animale):
    def fai_verso(self):
        return f"{self.nome} abbaia: Bau!"
```

### **Classe `Cavallo`**
```python
class Cavallo(Animale):
    def fai_verso(self):
        return f"{self.nome} nitrisce: Hiiii!"
```

### **Classe `Leone`**
```python
class Leone(Animale):
    def fai_verso(self):
        return f"{self.nome} ruggisce: Roar!"
```

## 🎬 Esecuzione del Programma (`init.py`)

```python
def main():
    animali = [Cane("Fido"), Cavallo("Spirit"), Leone("Simba")]
    
    for animale in animali:
        print(animale.fai_verso())

if __name__ == "__main__":
    main()
```

### 📌 Output Atteso
```
Fido abbaia: Bau!
Spirit nitrisce: Hiiii!
Simba ruggisce: Roar!
```

## 🎯 Obiettivo del Progetto

- Comprendere come utilizzare le **classi astratte** per definire interfacce comuni.
- Applicare **ereditarietà e polimorfismo** per gestire più tipi di animali.
- Strutturare un progetto Python con più file e classi ben organizzate.
