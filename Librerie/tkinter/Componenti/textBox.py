import tkinter as tk

def mostra_testo():
    testo = entry.get()
    label.config(text=f"Hai scritto: {testo}")

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione iniziale (larghezza x altezza)

label = tk.Label(root, text="Ciao, Tkinter!", font=("Arial", 14))
label.pack()

entry = tk.Entry(root, font=("Arial", 14))  # Casella di testo
entry.pack()


button = tk.Button(root, text="Mostra Testo", command=mostra_testo)
button.pack()

root.mainloop()  # Avvia l'interfaccia grafica