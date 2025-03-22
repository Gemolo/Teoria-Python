# 🧮 Calcolatrice con Tkinter

Questa semplice calcolatrice utilizza `Tkinter` per permettere all'utente di inserire un'espressione matematica e ottenere il risultato.

---

## 📌 Funzionalità
✔ Permette di inserire un'espressione matematica.  
✔ Calcola il risultato premendo un pulsante.  
✔ Mostra il risultato in un'etichetta.

⚠ **Attenzione:** `eval()` può eseguire codice arbitrario, quindi non è sicuro se il programma accetta input da utenti sconosciuti.  
Per proteggere il codice, si potrebbe usare `ast.literal_eval()` per limitare i calcoli a operazioni matematiche sicure.

---

## 🔹 **Componenti Utilizzate**
| Componente | Descrizione |
|------------|------------|
| `Tk()` | Crea la finestra principale. |
| `Entry()` | Casella di testo per inserire l'espressione matematica. |
| `Button()` | Pulsante per eseguire il calcolo. |
| `Label()` | Mostra il risultato del calcolo. |
| `eval()` | Valuta l'espressione matematica inserita dall'utente. |

---

## 🔹 **Codice: `Calcolatrice.py`**
```python
import tkinter as tk  # Importiamo Tkinter

root = tk.Tk()  # Creazione della finestra principale
root.title("Calcolatrice")  # Imposta il titolo della finestra
root.geometry("300x200")  # Imposta la dimensione

# Funzione per eseguire il calcolo
def calcola():
    try:
        risultato = eval(entry.get())  # Valuta l'espressione matematica
        label.config(text=f"Risultato: {risultato}")  # Aggiorna la Label con il risultato
    except:
        label.config(text="Errore!")  # In caso di errore, mostra un messaggio

# Creazione della casella di testo per inserire i numeri
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Creazione del pulsante di calcolo
button = tk.Button(root, text="Calcola", command=calcola)
button.pack()

# Creazione dell'etichetta per il risultato
label = tk.Label(root, text="Risultato: ", font=("Arial", 14))
label.pack()

root.mainloop()  # Avvia l'interfaccia grafica
```

---

## 🚀 Esecuzione del Programma
Per avviare la calcolatrice, eseguire il seguente comando nel terminale:
```bash
python Calcolatrice.py
```

---

## 📌 Possibili Miglioramenti
🔹 Utilizzare `ast.literal_eval()` per una maggiore sicurezza.  
🔹 Aggiungere pulsanti numerici per simulare una calcolatrice fisica.  
🔹 Implementare un'interfaccia più avanzata con più operazioni e uno storico dei calcoli.
