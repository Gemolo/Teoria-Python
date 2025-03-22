# 🏋️‍♂️ Esercizi con Tkinter

Questa cartella contiene alcuni esercizi pratici con **Tkinter**, la libreria di Python per creare interfacce grafiche.  
Gli esercizi attuali includono una **Calcolatrice** e il **Gioco del Tris (Tic-Tac-Toe)**.

---

## 📂 Contenuto della Cartella

| Esercizio      | File               | Descrizione |
|---------------|--------------------|------------|
| **Calcolatrice** | `Calcolatrice.py` | Permette di eseguire operazioni matematiche |
| **Tris**        | `tris.py`         | Implementa il gioco del Tris per due giocatori |

---

# 🧮 **Calcolatrice con Tkinter**
La **calcolatrice** permette di inserire un'espressione matematica e ottenere il risultato.

### 🔹 **Componenti Utilizzate**
✔ `Entry()` → Casella di testo per inserire l'espressione.  
✔ `Button()` → Pulsante per calcolare il risultato.  
✔ `Label()` → Mostra il risultato.  
✔ `eval()` → Valuta l'espressione matematica (⚠ **Attenzione ai rischi di sicurezza!**).

### 🔹 **Codice Esempio**
```python
import tkinter as tk

root = tk.Tk()
root.title("Calcolatrice")

def calcola():
    try:
        risultato = eval(entry.get())
        label.config(text=f"Risultato: {risultato}")
    except:
        label.config(text="Errore!")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Calcola", command=calcola)
button.pack()

label = tk.Label(root, text="Risultato: ")
label.pack()

root.mainloop()
```

✅ **Esecuzione**
```bash
python Calcolatrice.py
```

---

# 🎮 **Gioco del Tris (Tic-Tac-Toe)**
Il gioco del **Tris** permette a due giocatori di alternarsi per posizionare "X" e "O" su una griglia 3x3.

### 🔹 **Componenti Utilizzate**
✔ `Button()` → Pulsanti per la griglia di gioco.  
✔ `messagebox.showinfo()` → Mostra un popup quando un giocatore vince.  
✔ `grid(row, column)` → Dispone i pulsanti in una griglia.  
✔ `reset_game()` → Riavvia il gioco dopo una vittoria o un pareggio.

### 🔹 **Codice Esempio**
```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tris")

player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def on_click(row, col):
    global player
    if board[row][col] == "":
        board[row][col] = player
        buttons[row][col].config(text=player, state="disabled")
        player = "O" if player == "X" else "X"

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                                  command=lambda r=i, c=j: on_click(r, c))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
```

✅ **Esecuzione**
```bash
python tris.py
```

---

# 📌 Possibili Miglioramenti
🔹 **Per la Calcolatrice:** Migliorare la sicurezza usando `ast.literal_eval()` invece di `eval()`.  
🔹 **Per il Tris:** Aggiungere un'IA per giocare contro il computer.  
🔹 Aggiungere altri esercizi pratici con Tkinter, come un convertitore di unità o un timer.
