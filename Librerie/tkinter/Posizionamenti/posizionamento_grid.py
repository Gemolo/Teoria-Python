import tkinter as tk

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione iniziale (larghezza x altezza)


label1 = tk.Label(root, text="Riga 0, Colonna 0", bg="lightgray")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Riga 0, Colonna 1", bg="lightblue")
label2.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()  # Avvia l'interfaccia grafica