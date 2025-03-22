import tkinter as tk

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione iniziale (larghezza x altezza)

label = tk.Label(root, text="Testo con place()", bg="yellow")
label.place(x=100, y=50)

root.mainloop()  # Avvia l'interfaccia grafica