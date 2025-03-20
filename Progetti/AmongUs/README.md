# 🎮 Among Us - Gioco in Python 🚀

Questo è un semplice gioco in Python in cui il giocatore deve trovare un numero nascosto all'interno di una matrice prima che il tempo scada. ⏳

## 🔍 Come funziona

1. 🎲 Il gioco genera una matrice di numeri 8, con un singolo numero 3 nascosto in una posizione casuale.
2. 🎚️ Il giocatore sceglie la difficoltà:
    - 🟢 **Facile:** 5x5 con 10 secondi di tempo.
    - 🟡 **Medio:** 8x8 con 8 secondi di tempo.
    - 🔴 **Difficile:** 10x10 con 5 secondi di tempo.
3. ⏲️ Il gioco mostra la matrice per alcuni secondi, poi la nasconde.
4. ✍️ Il giocatore deve inserire le coordinate del numero 3.
5. ✅ Se le coordinate sono corrette, il giocatore vince; ❌ altrimenti perde.
6. 🔄 Il gioco offre la possibilità di rigiocare.

## 🛠️ Requisiti

- 🐍 Python 3.x
- 📦 Moduli standard (`os`, `time`, `random`)

## ▶️ Come eseguire il gioco

Scarica il file `amongUs.py` ed eseguilo con Python:

```sh
python amongUs.py
```

## 💻 Esempio di output

```
Trova il numero nascosto 3 tra tutti gli 8
Scegli la difficoltà:
 1 › Facile      2 › Medio      3 › Difficile
Scrivi qui: 2
Il gioco sta per iniziare!
...
Prova ad indovinare le coordinate!
Indovina la riga: 3
Indovina la colonna: 4
(3,4) HAI VINTO!!! 🎉
```

## 👤 Autore

Sviluppato come esercizio di programmazione in Python.

---
🎯 Buon divertimento! 🎮