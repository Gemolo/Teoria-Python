import tkinter as tk
import random

GRID_SIZE = 4
TILE_SIZE = 100
TILE_MARGIN = 10

values = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
tiles = {}
score = 0

root = tk.Tk()
root.title("2048")
canvas = tk.Canvas(root, width=GRID_SIZE*(TILE_SIZE+TILE_MARGIN)+TILE_MARGIN, height=GRID_SIZE*(TILE_SIZE+TILE_MARGIN)+TILE_MARGIN, bg="#bbada0")
canvas.pack()


def get_color(value):
    colors = {
        0: "#ccc0b3",
        2: "#eee4da",
        4: "#ede0c8",
        8: "#f2b179",
        16: "#f59563",
        32: "#f67c5f",
        64: "#f65e3b",
        128: "#edcf72",
        256: "#edcc61",
        512: "#edc850",
        1024: "#edc53f",
        2048: "#edc22e",
    }
    return colors.get(value, "#3c3a32")


def add_tile():
    empty = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if values[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        values[r][c] = 2 if random.random() < 0.9 else 4


def draw_tiles():
    canvas.delete("all")
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            draw_tile(r, c)


def draw_tile(row, col):
    x0 = TILE_MARGIN + col * (TILE_SIZE + TILE_MARGIN)
    y0 = TILE_MARGIN + row * (TILE_SIZE + TILE_MARGIN)
    x1 = x0 + TILE_SIZE
    y1 = y0 + TILE_SIZE
    value = values[row][col]
    color = get_color(value)
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
    if value:
        canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(value), font=("Helvetica", 32, "bold"), fill="white")


def compress(row):
    new_row = [v for v in row if v != 0]
    new_row += [0] * (GRID_SIZE - len(new_row))
    return new_row


def merge(row):
    global score
    for i in range(GRID_SIZE - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            score += row[i]
            row[i + 1] = 0
    return row


def move_left():
    moved = False
    for i in range(GRID_SIZE):
        original = list(values[i])
        row = compress(values[i])
        row = merge(row)
        values[i] = compress(row)
        if values[i] != original:
            moved = True
    return moved


def move_right():
    for i in range(GRID_SIZE):
        values[i] = values[i][::-1]
    moved = move_left()
    for i in range(GRID_SIZE):
        values[i] = values[i][::-1]
    return moved


def move_up():
    global values
    values = [list(row) for row in zip(*values)]
    moved = move_left()
    values = [list(row) for row in zip(*values)]
    return moved


def move_down():
    global values
    values = [list(row) for row in zip(*values)]
    for i in range(GRID_SIZE):
        values[i] = values[i][::-1]
    moved = move_left()
    for i in range(GRID_SIZE):
        values[i] = values[i][::-1]
    values = [list(row) for row in zip(*values)]
    return moved


def can_move():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if values[r][c] == 0:
                return True
            if c < GRID_SIZE - 1 and values[r][c] == values[r][c + 1]:
                return True
            if r < GRID_SIZE - 1 and values[r][c] == values[r + 1][c]:
                return True
    return False


def game_over():
    canvas.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2, text="GAME OVER", fill="white", font=("Helvetica", 32, "bold"))


def key(event):
    moved = False
    if event.keysym == "Up":
        moved = move_up()
    elif event.keysym == "Down":
        moved = move_down()
    elif event.keysym == "Left":
        moved = move_left()
    elif event.keysym == "Right":
        moved = move_right()

    if moved:
        add_tile()
        draw_tiles()
        if not can_move():
            game_over()


add_tile()
add_tile()
draw_tiles()
root.bind("<Key>", key)
root.mainloop()