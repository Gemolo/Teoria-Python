import tkinter as tk

clicks = 0
tempo = 10
gioco_attivo = False

def inizia_gioco():
    global clicks, tempo, gioco_attivo
    clicks = 0
    tempo = 10
    gioco_attivo = True
    label_clicks.config(text="Click: 0")
    label_timer.config(text="Tempo: 10")
    btn_click.config(state="normal")
    countdown()

def conta_click():
    global clicks
    if gioco_attivo:
        clicks += 1
        label_clicks.config(text=f"Click: {clicks}")

def countdown():
    global tempo, gioco_attivo
    if tempo > 0:
        tempo -= 1
        label_timer.config(text=f"Tempo: {tempo}")
        root.after(1000, countdown)
    else:
        gioco_attivo = False
        btn_click.config(state="disabled")
        label_timer.config(text="Tempo scaduto!")
        label_clicks.config(text=f"Totale click: {clicks}")

# GUI
root = tk.Tk()
root.title("Conta i click!")

btn_click = tk.Button(root, text="CLICCAMI!", font=("Arial", 24), command=conta_click)
btn_click.pack(pady=20)
btn_click.config(state="disabled")

label_clicks = tk.Label(root, text="Click: 0", font=("Arial", 18))
label_clicks.pack()

label_timer = tk.Label(root, text="Tempo: 10", font=("Arial", 18))
label_timer.pack(pady=10)

btn_start = tk.Button(root, text="Inizia", command=inizia_gioco)
btn_start.pack()

root.mainloop()