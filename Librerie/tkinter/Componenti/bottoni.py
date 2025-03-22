import tkinter as tk

def saluta():
    label.config(text="Hai premuto il pulsante!")


root = tk.Tk()  # Crea la finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta la dimensione iniziale (larghezza x altezza)

label = tk.Label(root, text="Ciao, Tkinter!", font=("Arial", 14))
label.pack()

button = tk.Button(root, text="Cliccami", command=saluta)
button.pack()

root.mainloop()  # Avvia l'interfaccia grafica