import tkinter as tk
import random
from PIL import Image, ImageTk

# Costanti
LARGHEZZA = 400
ALTEZZA = 500
VELOCITA_PROIETTILE = -10
VELOCITA_NEMICO = 2
SPAWN_NEMICO_MS = 2000

# Stato
nemici = []
proiettili = []
punteggio = 0
gioco_attivo = True

# GUI
root = tk.Tk()
root.title("Space Invaders PNG Edition")

canvas = tk.Canvas(root, width=LARGHEZZA, height=ALTEZZA, bg="black")
canvas.pack()

label = tk.Label(root, text="Punteggio: 0", font=("Arial", 12))
label.pack()

# Carica immagini PNG
# Carica e ridimensiona nave.png
img_nave_pil = Image.open("nave.png").resize((40, 40), Image.LANCZOS)
img_nave = ImageTk.PhotoImage(img_nave_pil)

# Carica e ridimensiona alieni.png
img_alieni_pil = Image.open("alieni.png").resize((30, 30), Image.LANCZOS)
img_alieni = ImageTk.PhotoImage(img_alieni_pil)

# Crea la nave
nave = canvas.create_image(200, 470, image=img_nave)

# Movimento nave
def muovi_nave(senso):
    x, y = canvas.coords(nave)
    dx = 15 * senso
    if 20 < x + dx < LARGHEZZA - 20:
        canvas.move(nave, dx, 0)

# Spara
def spara():
    if not gioco_attivo:
        return
    x, y = canvas.coords(nave)
    proiettile = canvas.create_rectangle(x - 2, y - 10, x + 2, y, fill="yellow")
    proiettili.append(proiettile)

# Muove proiettili e gestisce collisioni
def muovi_proiettili():
    for p in proiettili[:]:
        canvas.move(p, 0, VELOCITA_PROIETTILE)
        x1, y1, x2, y2 = canvas.coords(p)
        if y2 < 0:
            canvas.delete(p)
            proiettili.remove(p)
        else:
            for n in nemici[:]:
                if collisione(p, n):
                    canvas.delete(p)
                    canvas.delete(n)
                    proiettili.remove(p)
                    nemici.remove(n)
                    aggiorna_punteggio()
                    break
    if gioco_attivo:
        root.after(50, muovi_proiettili)

# Aumenta punteggio
def aggiorna_punteggio():
    global punteggio
    punteggio += 10
    label.config(text=f"Punteggio: {punteggio}")

# Collisione rettangolare
def collisione(a, b):
    ax1, ay1, ax2, ay2 = canvas.bbox(a)
    bx1, by1, bx2, by2 = canvas.bbox(b)
    return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

# Spawna alieni
def spawna_nemico():
    if not gioco_attivo:
        return
    x = random.randint(20, LARGHEZZA - 20)
    nemico = canvas.create_image(x, 15, image=img_alieni)
    nemici.append(nemico)
    root.after(SPAWN_NEMICO_MS, spawna_nemico)

# Muove alieni e controlla se arrivano in fondo
def muovi_nemici():
    global gioco_attivo
    for n in nemici[:]:
        canvas.move(n, 0, VELOCITA_NEMICO)
        x, y = canvas.coords(n)
        if y > ALTEZZA - 40:
            canvas.delete(n)
            nemici.remove(n)
            game_over()
            return
    if gioco_attivo:
        root.after(50, muovi_nemici)

# Fine del gioco
def game_over():
    global gioco_attivo
    gioco_attivo = False
    canvas.create_text(LARGHEZZA / 2, ALTEZZA / 2, text="GAME OVER", fill="white", font=("Arial", 24))

# Controlli tastiera
root.bind("<Left>", lambda e: muovi_nave(-1))
root.bind("<Right>", lambda e: muovi_nave(1))
root.bind("<space>", lambda e: spara())

# Avvio
spawna_nemico()
muovi_proiettili()
muovi_nemici()

root.mainloop()