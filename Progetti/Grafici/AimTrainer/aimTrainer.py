import tkinter as tk
import random

LARGHEZZA = 400
ALTEZZA = 400
RAGGIO = 30
TEMPO_CERCHIO = 1000  # in ms

# Variabili globali
punteggio = 0
x = y = 0
cerchio_id = None
timer_id = None

def prossimo_cerchio():
    global x, y, cerchio_id, timer_id
    canvas.delete("all")
    x = random.randint(RAGGIO, LARGHEZZA - RAGGIO)
    y = random.randint(RAGGIO, ALTEZZA - RAGGIO)
    cerchio_id = canvas.create_oval(
        x - RAGGIO, y - RAGGIO, x + RAGGIO, y + RAGGIO, fill="red"
    )
    # Cancella timer precedente, se esiste
    if timer_id is not None:
        root.after_cancel(timer_id)
    timer_id = root.after(TEMPO_CERCHIO, scade_tempo)

def scade_tempo():
    global cerchio_id
    if canvas.find_withtag(cerchio_id):
        prossimo_cerchio()

def controlla_click(event):
    global punteggio
    distanza = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
    if distanza <= RAGGIO:
        punteggio += 1
        label.config(text=f"Punteggio: {punteggio}")
        prossimo_cerchio()

# GUI setup
root = tk.Tk()
root.title("Colpisci il Cerchio!")

canvas = tk.Canvas(root, width=LARGHEZZA, height=ALTEZZA, bg="white")
canvas.pack()

label = tk.Label(root, text="Punteggio: 0")
label.pack()

canvas.bind("<Button-1>", controlla_click)

prossimo_cerchio()
root.mainloop()