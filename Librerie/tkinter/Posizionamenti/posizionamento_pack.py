import tkinter as tk

root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione iniziale (larghezza x altezza)


label1 = tk.Label(root, text="Etichetta 1", bg="red")
label1.pack(fill="both", expand=True)

label2 = tk.Label(root, text="Etichetta 2", bg="blue")
label2.pack(fill="both", expand=True)

root.mainloop()  # Avvia l'interfaccia grafica