# 🖥️ Guida Completa a Tkinter - Creare GUI in Python

Tkinter è la libreria standard di **Python** per creare **interfacce grafiche (GUI)**.  
Con questa guida, esploreremo le componenti principali: **TextBox, Label, Pulsanti, Posizionamenti, Colori e Animazioni**.

---

## 📌 Contenuto della Guida

| Sezione           | Descrizione |
|------------------|------------|
| **Finestre e Box** | Creare la finestra principale con Tkinter |
| **Label (Etichette)** | Mostrare testo nella GUI |
| **Button (Pulsanti)** | Interagire con la GUI |
| **Entry (Caselle di Testo)** | Inserire dati tramite input |
| **Text (Aree di Testo)** | Creare blocchi di testo modificabili |
| **Posizionamento** | Usare `grid()`, `pack()`, `place()` |
| **Colori** | Personalizzare lo sfondo e il testo |
| **Animazioni** | Creare animazioni con `after()` |

---

# 📦 **Creare una Finestra con Tkinter**
Per avviare una GUI con Tkinter, dobbiamo creare una finestra principale (`Tk()`).

### 🔹 **Codice**
```python
import tkinter as tk

root = tk.Tk()  # Creazione della finestra principale
root.title("Finestra Tkinter")  # Imposta il titolo
root.geometry("400x300")  # Imposta le dimensioni

root.mainloop()  # Avvia la finestra
```
✔ `title("Nome")` → Imposta il titolo della finestra.  
✔ `geometry("LxA")` → Definisce le dimensioni iniziali.  
✔ `mainloop()` → Avvia la GUI.

---

# 🏷️ **Label (Etichette)**
Le etichette (`Label`) servono per mostrare testo statico nella finestra.

### 🔹 **Codice**
```python
label = tk.Label(root, text="Ciao, Tkinter!", font=("Arial", 14))
label.pack()
```
✔ `text="..."` → Testo da mostrare.  
✔ `font=("Arial", 14)` → Definisce il font e la dimensione del testo.  
✔ `.pack()` → Posiziona l’etichetta.

---

# 🔘 **Button (Pulsanti)**
I bottoni (`Button`) permettono di eseguire azioni quando vengono cliccati.

### 🔹 **Codice**
```python
def saluta():
    label.config(text="Hai premuto il pulsante!")

button = tk.Button(root, text="Cliccami", command=saluta)
button.pack()
```
✔ `command=saluta` → Esegue la funzione quando viene cliccato.

---

# ✍️ **Entry (Caselle di Testo)**
Le caselle di testo (`Entry`) permettono all’utente di inserire dati.

### 🔹 **Codice**
```python
entry = tk.Entry(root, font=("Arial", 14))
entry.pack()
```
✔ `.get()` → Legge il testo inserito.

---

# 📜 **Text (Aree di Testo)**
Il widget `Text` permette di creare blocchi di testo modificabili.

### 🔹 **Codice**
```python
text = tk.Text(root, height=5, width=30)
text.pack()
```
✔ `height=5, width=30` → Imposta la dimensione del box di testo.

---

# 📌 **Posizionamento degli Elementi**
Tkinter offre 3 metodi principali per posizionare gli elementi:

### 🔹 **Grid (Griglia)**
```python
label1 = tk.Label(root, text="Colonna 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Colonna 2")
label2.grid(row=0, column=1)
```
✔ `grid(row, column)` → Posiziona in una tabella.

### 🔹 **Pack (Ordinamento Automatico)**
```python
label.pack(fill="both", expand=True)
```
✔ `fill="both"` → Espande l’elemento.

### 🔹 **Place (Posizionamento Assoluto)**
```python
label.place(x=100, y=50)
```
✔ `x, y` → Coordinate assolute.

---

# 🎨 **Colori e Personalizzazione**
Tkinter permette di personalizzare i colori di sfondo e testo.

### 🔹 **Codice**
```python
label = tk.Label(root, text="Colorato!", bg="yellow", fg="red")
label.pack()
```
✔ `bg="yellow"` → Colore di sfondo.  
✔ `fg="red"` → Colore del testo.

---

# 🎬 **Animazioni con `after()`**
Per creare animazioni, possiamo usare `after()`.

### 🔹 **Codice**
```python
def cambia_colore():
    label.config(fg="blue")
    root.after(1000, cambia_colore)

label = tk.Label(root, text="Animazione!")
label.pack()

root.after(1000, cambia_colore)
```
✔ `after(tempo, funzione)` → Esegue una funzione dopo un intervallo.

---

# 🚀 **Conclusione**
Tkinter è un’ottima libreria per creare GUI in Python.  
**Possibili miglioramenti:**
- Aggiungere menu e finestre multiple.
- Integrare con database.
- Creare layout più complessi con `grid()` e `place()`.
