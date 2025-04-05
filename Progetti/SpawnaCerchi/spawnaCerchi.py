import tkinter as tk
import random

LARGHEZZA = 400
ALTEZZA = 400
RAGGIO = 20
INTERVALLO_SPAWN = 1000     # ogni 1 secondo
DURATA_CERCHIO = 2000       # ogni cerchio dura 2 secondi

def crea_cerchio():
    x = random.randint(RAGGIO, LARGHEZZA - RAGGIO)
    y = random.randint(RAGGIO, ALTEZZA - RAGGIO)

    cerchio = canvas.create_oval(
        x - RAGGIO, y - RAGGIO, x + RAGGIO, y + RAGGIO,
        fill="red", outline=""
    )

    # Rimuove il cerchio dopo 2 secondi
    root.after(DURATA_CERCHIO, lambda: canvas.delete(cerchio))

    # Continua a crearne uno ogni secondo
    root.after(INTERVALLO_SPAWN, crea_cerchio)

# GUI setup
root = tk.Tk()
root.title("Cerchi casuali che spariscono")

canvas = tk.Canvas(root, width=LARGHEZZA, height=ALTEZZA, bg="white")
canvas.pack()

crea_cerchio()

root.mainloop()