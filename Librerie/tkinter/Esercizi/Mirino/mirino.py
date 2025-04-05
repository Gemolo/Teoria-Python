import tkinter as tk

LARGHEZZA = 600
ALTEZZA = 400
RAGGIO_MIRINO = 20  # grandezza del mirino

def aggiorna_mirino(event):
    x, y = event.x, event.y
    canvas.coords(cerchio, x - RAGGIO_MIRINO, y - RAGGIO_MIRINO, x + RAGGIO_MIRINO, y + RAGGIO_MIRINO)
    canvas.coords(linea_orizz, x - RAGGIO_MIRINO, y, x + RAGGIO_MIRINO, y)
    canvas.coords(linea_vert, x, y - RAGGIO_MIRINO, x, y + RAGGIO_MIRINO)

# GUI
root = tk.Tk()
root.title("Mirino personalizzato")

canvas = tk.Canvas(root, width=LARGHEZZA, height=ALTEZZA, bg="white", cursor="none")
canvas.pack()

# Disegna il mirino iniziale (fuori dallo schermo per ora)
cerchio = canvas.create_oval(-100, -100, -90, -90, outline="red", width=2)
linea_orizz = canvas.create_line(-100, -100, -90, -90, fill="red", width=2)
linea_vert = canvas.create_line(-100, -100, -90, -90, fill="red", width=2)

canvas.bind("<Motion>", aggiorna_mirino)

root.mainloop()