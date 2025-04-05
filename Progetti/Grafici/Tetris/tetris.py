import tkinter as tk
import random

# Configurazione
LARGHEZZA = 300
ALTEZZA = 600
TILE = 30
COLS = LARGHEZZA // TILE
ROWS = ALTEZZA // TILE

# Blocchi Tetris
TETROMINI = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]]
}

COLORI = {
    'I': 'cyan',
    'O': 'yellow',
    'T': 'purple',
    'S': 'green',
    'Z': 'red',
    'J': 'blue',
    'L': 'orange'
}

# Stato
campo = [[None for _ in range(COLS)] for _ in range(ROWS)]
blocco = None
blocco_x = 0
blocco_y = 0
blocco_tipo = ''
in_gioco = True

# GUI
root = tk.Tk()
root.title("Tetris")
canvas = tk.Canvas(root, width=LARGHEZZA, height=ALTEZZA, bg='black')
canvas.pack()

# Nuovo blocco
def nuovo_blocco():
    global blocco, blocco_x, blocco_y, blocco_tipo
    blocco_tipo = random.choice(list(TETROMINI.keys()))
    blocco = TETROMINI[blocco_tipo]
    blocco_x = COLS // 2 - len(blocco[0]) // 2
    blocco_y = 0
    if not puo_posizionare(blocco, blocco_x, blocco_y):
        game_over()

# Controlla se un blocco può essere posizionato
def puo_posizionare(shape, x, y):
    for i, riga in enumerate(shape):
        for j, cella in enumerate(riga):
            if cella:
                nx, ny = x + j, y + i
                if nx < 0 or nx >= COLS or ny >= ROWS or (ny >= 0 and campo[ny][nx]):
                    return False
    return True

# Posiziona blocco nel campo
def fissa_blocco():
    global campo
    for i, riga in enumerate(blocco):
        for j, cella in enumerate(riga):
            if cella:
                ny = blocco_y + i
                nx = blocco_x + j
                if 0 <= ny < ROWS and 0 <= nx < COLS:
                    campo[ny][nx] = blocco_tipo

# Ruota matrice 90°
def ruota(mat):
    return [list(row)[::-1] for row in zip(*mat)]

# Elimina righe piene
def elimina_righe():
    global campo
    nuove = [r for r in campo if any(cell is None for cell in r)]
    eliminate = ROWS - len(nuove)
    for _ in range(eliminate):
        nuove.insert(0, [None] * COLS)
    campo = nuove

# Game Over
def game_over():
    global in_gioco
    in_gioco = False
    canvas.create_text(LARGHEZZA // 2, ALTEZZA // 2, text="GAME OVER", fill="white", font=("Arial", 24))

# Disegna tutto
def disegna():
    canvas.delete("all")
    # Blocchi fissati
    for y in range(ROWS):
        for x in range(COLS):
            if campo[y][x]:
                canvas.create_rectangle(
                    x * TILE, y * TILE, (x+1) * TILE, (y+1) * TILE,
                    fill=COLORI[campo[y][x]], outline="black"
                )
    # Blocco attivo
    if in_gioco:
        for i, riga in enumerate(blocco):
            for j, cella in enumerate(riga):
                if cella:
                    x = blocco_x + j
                    y = blocco_y + i
                    if y >= 0:
                        canvas.create_rectangle(
                            x * TILE, y * TILE, (x+1) * TILE, (y+1) * TILE,
                            fill=COLORI[blocco_tipo], outline="white"
                        )

# Timer
def aggiorna():
    global blocco_y
    if not in_gioco:
        return
    if puo_posizionare(blocco, blocco_x, blocco_y + 1):
        blocco_y += 1
    else:
        fissa_blocco()
        elimina_righe()
        nuovo_blocco()
    disegna()
    root.after(300, aggiorna)

# Controlli
def muovi(dx):
    global blocco_x
    if puo_posizionare(blocco, blocco_x + dx, blocco_y):
        blocco_x += dx
        disegna()

def ruota_blocco():
    global blocco
    nuova = ruota(blocco)
    if puo_posizionare(nuova, blocco_x, blocco_y):
        blocco = nuova
        disegna()

def giu():
    global blocco_y
    while puo_posizionare(blocco, blocco_x, blocco_y + 1):
        blocco_y += 1
    disegna()

# Tasti
root.bind("<Left>", lambda e: muovi(-1))
root.bind("<Right>", lambda e: muovi(1))
root.bind("<Up>", lambda e: ruota_blocco())
root.bind("<Down>", lambda e: giu())

# Inizio gioco
nuovo_blocco()
aggiorna()
root.mainloop()