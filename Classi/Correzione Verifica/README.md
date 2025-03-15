# 📚 Programmazione Orientata agli Oggetti - Biblioteca

Questo repository contiene un esempio di utilizzo della **Programmazione Orientata agli Oggetti (OOP)** in Python, applicata alla gestione di una **biblioteca**.

## 📂 Struttura del Repository

- **`autore.py`** → Definizione della classe `Autore`.
- **`libro.py`** → Implementazione della classe `Libro`, che rappresenta un libro con un autore.
- **`biblioteca.py`** → Definizione della classe `Biblioteca`, che gestisce una collezione di libri.

## 🏗️ Concetti Utilizzati

- **Classi e Oggetti** → Rappresentazione di autori, libri e biblioteche come classi.
- **Relazioni tra classi** → Un libro ha un autore, una biblioteca ha una collezione di libri.
- **Metodi e gestione dati** → Ogni classe ha metodi per manipolare le informazioni.

## 🔹 Definizione della Classe `Autore`

```python
class Autore:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f"{self.nome} {self.cognome}"
```

## 📖 Classe `Libro`

```python
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
    
    def __str__(self):
        return f"{self.titolo} di {self.autore}"
```

## 🏛️ Classe `Biblioteca`

```python
class Biblioteca:
    def __init__(self):
        self.libri = []
    
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
    
    def mostra_libri(self):
        for libro in self.libri:
            print(libro)
```

## 🎬 Esecuzione del Programma

```python
def main():
    autore1 = Autore("J.K.", "Rowling")
    autore2 = Autore("George", "Orwell")
    
    libro1 = Libro("Harry Potter", autore1)
    libro2 = Libro("1984", autore2)
    
    biblioteca = Biblioteca()
    biblioteca.aggiungi_libro(libro1)
    biblioteca.aggiungi_libro(libro2)
    
    print("Libri nella biblioteca:")
    biblioteca.mostra_libri()

if __name__ == "__main__":
    main()
```

### 📌 Output Atteso
```
Libri nella biblioteca:
Harry Potter di J.K. Rowling
1984 di George Orwell
```

## 🎯 Obiettivo del Progetto

- Creare una simulazione base di una biblioteca.
- Comprendere le relazioni tra classi (`Libro` ha un `Autore`, `Biblioteca` contiene `Libri`).
- Applicare i concetti di **OOP in Python**.
