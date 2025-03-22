import tkinter as tk

root = tk.Tk()
root.title("Calcolatrice")
root.geometry("300x200")

def calcola():
    try:
        risultato = eval(entry.get())
        label.config(text=f"Risultato: {risultato}")
    except:
        label.config(text="Errore!")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Calcola", command=calcola)
button.pack()

label = tk.Label(root, text="Risultato: ", font=("Arial", 14))
label.pack()

root.mainloop()