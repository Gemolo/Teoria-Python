# 📌 Posizionamento degli Elementi in Tkinter

Tkinter offre tre principali metodi per posizionare gli elementi all'interno della finestra:
1. **grid()** → Organizza i widget in una griglia.
2. **pack()** → Dispone i widget automaticamente in verticale o orizzontale.
3. **place()** → Posiziona i widget con coordinate assolute.

---

## 📂 Contenuto del Repository

| Metodo di Posizionamento | File                   | Descrizione |
|--------------------------|------------------------|------------|
| **Grid**                | `posizionamento_grid.py` | Organizza gli elementi in righe e colonne |
| **Pack**                | `posizionamento_pack.py` | Dispone gli elementi in verticale/orizzontale |
| **Place**               | `posizionamento_place.py` | Posiziona gli elementi con coordinate assolute |

---

# 🟩 **Posizionamento con `grid()`**
Il metodo `grid()` organizza i widget in una tabella (righe e colonne).

### 🔹 **Componenti**
- **`.grid(row, column)`** → Posiziona un elemento in una cella specifica.
- **`padx, pady`** → Aggiunge spazio attorno agli elementi.

### 🔹 **Codice: `posizionamento_grid.py`**
```python
import tkinter as tk

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo
root.geometry("400x300")  # Imposta la dimensione

# Creazione delle etichette in una griglia
label1 = tk.Label(root, text="Riga 0, Colonna 0", bg="lightgray")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Riga 0, Colonna 1", bg="lightblue")
label2.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()  # Avvia l'interfaccia grafica
```

✅ **Esecuzione**
```bash
python posizionamento_grid.py
```

---

# 🟦 **Posizionamento con `pack()`**
Il metodo `pack()` dispone i widget in verticale o orizzontale in modo automatico.

### 🔹 **Componenti**
- **`.pack(fill="both", expand=True)`** → Espande il widget per riempire lo spazio disponibile.
- **`side="left"`, `side="right"`** → Posiziona i widget ai lati.

### 🔹 **Codice: `posizionamento_pack.py`**
```python
import tkinter as tk

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo
root.geometry("400x300")  # Imposta la dimensione

# Creazione delle etichette usando pack()
label1 = tk.Label(root, text="Etichetta 1", bg="red")
label1.pack(fill="both", expand=True)

label2 = tk.Label(root, text="Etichetta 2", bg="blue")
label2.pack(fill="both", expand=True)

root.mainloop()  # Avvia l'interfaccia grafica
```

✅ **Esecuzione**
```bash
python posizionamento_pack.py
```

---

# 🟨 **Posizionamento con `place()`**
Il metodo `place()` permette di posizionare i widget in coordinate assolute.

### 🔹 **Componenti**
- **`.place(x, y)`** → Posiziona l'elemento alle coordinate `(x, y)`.
- **`relx, rely`** → Posizionamento relativo alla finestra.

### 🔹 **Codice: `posizionamento_place.py`**
```python
import tkinter as tk

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo
root.geometry("400x300")  # Imposta la dimensione

# Creazione di un'etichetta posizionata con place()
label = tk.Label(root, text="Testo con place()", bg="yellow")
label.place(x=100, y=50)

root.mainloop()  # Avvia l'interfaccia grafica
```

✅ **Esecuzione**
```bash
python posizionamento_place.py
```

---

# 🎯 **Conclusione**
Ogni metodo di posizionamento ha il suo utilizzo ideale:
- **`grid()`** → Ideale per layout tabellari.
- **`pack()`** → Perfetto per distribuzione verticale/orizzontale automatica.
- **`place()`** → Utile quando si vuole controllo preciso del posizionamento.

💡 **Quale metodo è il più adatto per il tuo progetto? 🚀**
