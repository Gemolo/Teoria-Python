# 🎮 Tris (Tic-Tac-Toe) con Tkinter

Questo script implementa il classico gioco del **Tris** (Tic-Tac-Toe) utilizzando `Tkinter`.  
Due giocatori possono alternarsi per posizionare "X" e "O" su una griglia 3x3.

---

## 📌 Funzionalità
✔ Griglia 3x3 interattiva con pulsanti.  
✔ Controllo automatico della vittoria o del pareggio.  
✔ Messaggi popup per segnalare il vincitore.  
✔ Pulsante di reset per riavviare la partita.

---

## 🔹 **Componenti Utilizzate**
| Componente | Descrizione |
|------------|------------|
| `Tk()` | Crea la finestra principale del gioco. |
| `Button()` | Crea i pulsanti per le caselle della griglia. |
| `Label()` | Non usata, il gioco si basa sui pulsanti. |
| `messagebox.showinfo()` | Mostra un popup quando il gioco termina. |
| `grid(row, column)` | Posiziona i pulsanti nella finestra. |

---

## 🔹 **Codice: `tris.py`**
```python
import tkinter as tk
from tkinter import messagebox

# Creazione della finestra principale
root = tk.Tk()
root.title("Tris - Tic Tac Toe")
root.geometry("400x450")

# Variabili di gioco
player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Funzione per controllare la vittoria
def check_winner():
    for i in range(3):
        # Controllo righe e colonne
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    # Controllo diagonali
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    # Controllo pareggio
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Pareggio"

    return None

# Funzione per gestire il click sulle caselle
def on_click(row, col):
    global player

    if board[row][col] == "":
        board[row][col] = player
        buttons[row][col].config(text=player, state="disabled")
        winner = check_winner()

        if winner:
            if winner == "Pareggio":
                messagebox.showinfo("Tris", "Pareggio! Nessun vincitore.")
            else:
                messagebox.showinfo("Tris", f"🏆 Il giocatore {winner} ha vinto!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

# Funzione per resettare il gioco
def reset_game():
    global player, board
    player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# Creazione della griglia di pulsanti
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                  command=lambda r=i, c=j: on_click(r, c))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

# Pulsante per resettare il gioco
reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Avvio della finestra
root.mainloop()
```

---

## 🚀 Esecuzione del Programma
Per avviare il gioco, eseguire il seguente comando nel terminale:
```bash
python tris.py
```

---

## 📌 Possibili Miglioramenti
🔹 Aggiungere un'intelligenza artificiale per permettere di giocare contro il computer.  
🔹 Animazioni per le mosse.  
🔹 Effetti sonori per vittoria o pareggio.