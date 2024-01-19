# Tutorial: Utilizzo di Classi e Oggetti in Python 🐍

## Cosa sono le Classi?

In programmazione orientata agli oggetti (OOP), una classe è una struttura fondamentale che serve come modello o prototipo per creare oggetti. Gli oggetti, a loro volta, sono istanze specifiche di una classe e condividono caratteristiche comuni definite dalla classe stessa.

Le classi permettono di organizzare il codice in modo modulare, raggruppando dati e comportamenti correlati. Gli attributi di una classe rappresentano le variabili associate agli oggetti, mentre i metodi sono le funzioni che operano su questi dati.

## Struttura di una Classe

Le classi in Python seguono una struttura di base:

```python
class NomeClasse:
    def __init__(self, parametro1, parametro2):
        self.attributo1 = parametro1
        self.attributo2 = parametro2

    def metodo(self):
        # implementazione del metodo
        pass
```

- **__init__**: Questo è il metodo speciale chiamato il costruttore, utilizzato per inizializzare gli attributi dell'oggetto quando viene creato.
- **self**: Rappresenta l'istanza corrente della classe, permettendo l'accesso agli attributi e ai metodi dell'oggetto.

## Utilizzo delle Classi e degli Oggetti


# Istanza della classe
```python
istanza_oggetto = MyClass(valore1, valore2)
```
```python
# Utilizzo dell'oggetto
istanza_oggetto.stampa_attributi()
```


# Metodi Astratti in Python 🚀
## 1. Importare il Modulo abc
```python
from abc import ABC, abstractmethod
```

Il modulo *abc* fornisce la classe **ABC** (Abstract Base Class) e il decoratore *abstractmethod*, necessari per definire e utilizzare metodi astratti.

## 2. Definire una Classe Astratta
```python
class FormaGeometrica(ABC):
    @abstractmethod
    def calcola_area(self):
        pass

    @abstractmethod
    def calcola_perimetro(self):
        pass
```
In questo esempio, abbiamo una classe astratta *FormaGeometrica* con due metodi astratti: *calcola_area* e *calcola_perimetro*. Ogni sottoclasse di *FormaGeometrica* deve implementare questi metodi.

## 3. Creare una Sottoclasse

```python
class Rettangolo(FormaGeometrica):
    def __init__(self, lunghezza, larghezza):
        self.lunghezza = lunghezza
        self.larghezza = larghezza

    def calcola_area(self):
        return self.lunghezza * self.larghezza

    def calcola_perimetro(self):
        return 2 * (self.lunghezza + self.larghezza)
```

La classe *Rettangolo* eredita dalla classe astratta *FormaGeometrica* e implementa i metodi astratti *calcola_area* e *calcola_perimetro*.

## 4. Utilizzare le Sottoclassi
```python
rettangolo = Rettangolo(5, 3)
area = rettangolo.calcola_area()
perimetro = rettangolo.calcola_perimetro()

print(f"Area del rettangolo: {area}")
print(f"Perimetro del rettangolo: {perimetro}")
```

Qui creiamo un'istanza di *Rettangolo* e utilizziamo i metodi implementati. Poiché *Rettangolo* è una sottoclasse di *FormaGeometrica*, è obbligato a implementare i metodi astratti della classe base.

## 5. Gestire l'Errore se un Metodo Astratto non è Implementato
Se una sottoclasse non implementa un metodo astratto, verrà sollevato un errore durante l'istanziazione. Puoi gestire questa situazione in modo elegante.
```python
class Cerchio(FormaGeometrica):
    def __init__(self, raggio):
        self.raggio = raggio

    def calcola_area(self):
        return 3.14 * self.raggio ** 2
```

In questo esempio, Cerchio non implementa il metodo *calcola_perimetro*. Quando si cerca di istanziare *Cerchio*, verrà sollevato un errore. Puoi gestirlo così:

```python
try:
    cerchio = Cerchio(4)
except TypeError as e:
    print(f"Errore: {e}")
```

Questo tutorial fornisce una panoramica su come utilizzare i metodi astratti in Python. Puoi adattare questi concetti per creare classi astratte con metodi astratti specifici per il tuo progetto.