# 🖥️ GUI con Tkinter - Progetti Python

Questo repository contiene script Python che utilizzano **Tkinter** per creare interfacce grafiche (GUI).  
Ogni script dimostra un elemento specifico di Tkinter: **Label, Bottoni, Box (Finestre) e Caselle di Testo**.

---

## 📂 Contenuto del Repository

| Sezione           | File               | Descrizione |
|------------------|--------------------|------------|
| **Label**       | `label.py`         | Mostra un'etichetta Tkinter |
| **Bottoni**     | `bottoni.py`       | Pulsante che aggiorna un'etichetta |
| **Box (Finestre)** | `box.py`       | Crea una semplice finestra |
| **Casella di Testo** | `textBox.py`   | Casella di testo interattiva |

---

# 🏷️ **Label (Etichette)**

Le etichette (`Label`) servono per mostrare testo statico nella finestra.

### 🔹 **Componenti**
- **`Label(root, text="...")`** → Crea un’etichetta con un testo.
- **`font=("Arial", 14)`** → Definisce il font e la dimensione del testo.
- **`.pack()`** → Posiziona l’etichetta nella finestra.

### 🔹 **Codice: `label.py`**
```python
import tkinter as tk  # Importiamo la libreria Tkinter

root = tk.Tk()  # Crea la finestra principale
root.title("Etichetta in Tkinter")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione

# Creazione di un'etichetta con un testo iniziale
label = tk.Label(root, text="Ciao, Tkinter!", font=("Arial", 14))
label.pack()  # Posiziona l'etichetta nella finestra

root.mainloop()  # Avvia l'interfaccia grafica
```

✅ **Esecuzione**
```bash
python label.py
```

---

# 🔘 **Bottoni (Pulsanti)**

I bottoni (`Button`) permettono di eseguire azioni quando vengono cliccati.

### 🔹 **Componenti**
- **`Button(root, text="...", command=funzione)`** → Crea un pulsante che esegue una funzione.
- **`.config(text="...")`** → Modifica il testo di un elemento (es. una Label).
- **`.pack()`** → Posiziona il pulsante nella finestra.

### 🔹 **Codice: `bottoni.py`**
```python
import tkinter as tk  # Importiamo Tkinter

# Funzione che cambia il testo della Label quando il pulsante viene premuto
def saluta():
    label.config(text="Hai premuto il pulsante!")  # Modifica il testo della Label

root = tk.Tk()  # Crea la finestra principale
root.title("Bottoni con Tkinter")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione della finestra

# Creazione di un'etichetta con un messaggio iniziale
label = tk.Label(root, text="Ciao, Tkinter!", font=("Arial", 14))
label.pack()  # Posiziona l'etichetta nella finestra

# Creazione di un pulsante che richiama la funzione `saluta()` quando premuto
button = tk.Button(root, text="Cliccami", command=saluta)
button.pack()  # Posiziona il pulsante nella finestra

root.mainloop()  # Avvia l'interfaccia grafica
```

✅ **Esecuzione**
```bash
python bottoni.py
```

---

# 📦 **Box (Finestre)**

Le finestre (`Tk`) sono il contenitore principale di una GUI Tkinter.

### 🔹 **Componenti**
- **`Tk()`** → Crea la finestra principale.
- **`title("Nome")`** → Imposta il titolo della finestra.
- **`geometry("LxA")`** → Definisce le dimensioni iniziali della finestra.
- **`.mainloop()`** → Avvia l’interfaccia.

### 🔹 **Codice: `box.py`**
```python
import tkinter as tk  # Importiamo la libreria Tkinter

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Vuota")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione iniziale

root.mainloop()  # Avvia l'interfaccia grafica
```

✅ **Esecuzione**
```bash
python box.py
```

---

# ✍️ **Caselle di Testo (Entry)**

Le caselle di testo (`Entry`) permettono all’utente di inserire dati.

### 🔹 **Componenti**
- **`Entry(root, font=("Arial", 14))`** → Casella di testo.
- **`Button(root, text="...", command=funzione)`** → Pulsante che esegue la funzione associata.
- **`.get()`** → Legge il testo scritto nella casella di input.

### 🔹 **Codice: `textBox.py`**
```python
import tkinter as tk  # Importiamo la libreria Tkinter

# Funzione che legge il testo dalla casella e lo mostra nella Label
def mostra_testo():
    testo = entry.get()  # Prende il testo inserito dall'utente
    label.config(text=f"Hai scritto: {testo}")  # Aggiorna la Label

root = tk.Tk()  # Crea la finestra principale
root.title("Casella di Testo")  # Imposta il titolo
root.geometry("400x300")  # Imposta la dimensione

# Creazione dell'etichetta
label = tk.Label(root, text="Scrivi qualcosa sopra", font=("Arial", 14))
label.pack()

# Creazione della casella di testo
entry = tk.Entry(root, font=("Arial", 14))  # Casella di testo
entry.pack()

# Creazione del pulsante per mostrare il testo digitato
button = tk.Button(root, text="Mostra Testo", command=mostra_testo)
button.pack()

root.mainloop()  # Avvia l'interfaccia grafica
```

✅ **Esecuzione**
```bash
python textBox.py
```

---

# 🎯 **Conclusione**

Questi script mostrano come usare Tkinter per creare interfacce grafiche semplici.  
**Miglioramenti possibili:**
- Aggiungere una barra di menu.
- Implementare un'interfaccia più complessa con più elementi interattivi.
- Migliorare l'estetica con `grid()` o `place()` per il layout.

