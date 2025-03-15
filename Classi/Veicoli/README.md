# ⚡ Programmazione Orientata agli Oggetti - Veicoli Elettrici

Questo repository contiene un esempio pratico di **Programmazione Orientata agli Oggetti (OOP) in Python**, applicato alla gestione di **veicoli elettrici**, come auto e moto elettriche.

## 📂 Struttura del Repository

- **`veicolo.py`** → Definizione della classe base `Veicolo`.
- **`autoelettrica.py`** → Implementazione della classe `AutoElettrica`, derivata da `Veicolo`.
- **`motoelettrica.py`** → Implementazione della classe `MotoElettrica`, derivata da `Veicolo`.
- **`init.py`** → File principale per eseguire il programma e testare i veicoli elettrici.

## 🏗️ Concetti Utilizzati

- **Classi e Oggetti** → Rappresentazione di veicoli elettrici con attributi e metodi.
- **Ereditarietà** → `AutoElettrica` e `MotoElettrica` ereditano da `Veicolo`.
- **Metodi Specifici** → Ogni veicolo ha caratteristiche proprie.

## 🔹 Definizione della Classe `Veicolo`

```python
class Veicolo:
    def __init__(self, modello, autonomia):
        self.modello = modello
        self.autonomia = autonomia
    
    def descrizione(self):
        return f"{self.modello} ha un'autonomia di {self.autonomia} km."
```

## 🚗 Classe `AutoElettrica`

```python
class AutoElettrica(Veicolo):
    def __init__(self, modello, autonomia, numero_posti):
        super().__init__(modello, autonomia)
        self.numero_posti = numero_posti
    
    def descrizione(self):
        return f"L'auto elettrica {self.modello} ha {self.numero_posti} posti e un'autonomia di {self.autonomia} km."
```

## 🏍️ Classe `MotoElettrica`

```python
class MotoElettrica(Veicolo):
    def __init__(self, modello, autonomia, velocita_massima):
        super().__init__(modello, autonomia)
        self.velocita_massima = velocita_massima
    
    def descrizione(self):
        return f"La moto elettrica {self.modello} ha una velocità massima di {self.velocita_massima} km/h e un'autonomia di {self.autonomia} km."
```

## 🎬 Esecuzione del Programma (`init.py`)

```python
def main():
    auto = AutoElettrica("Tesla Model 3", 500, 5)
    moto = MotoElettrica("Zero SR/F", 250, 200)
    
    print(auto.descrizione())
    print(moto.descrizione())

if __name__ == "__main__":
    main()
```

### 📌 Output Atteso
```
L'auto elettrica Tesla Model 3 ha 5 posti e un'autonomia di 500 km.
La moto elettrica Zero SR/F ha una velocità massima di 200 km/h e un'autonomia di 250 km.
```

## 🎯 Obiettivo del Progetto

- Simulare un **sistema di gestione di veicoli elettrici**.
- Comprendere l'uso di **ereditarietà** e **override dei metodi**.
- Applicare i concetti di **OOP in Python**.

