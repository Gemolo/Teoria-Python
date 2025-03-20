import os
import time
import random

def creaMatriceValore(m, n, valore):
    matr = []
    for i in range(m):
        riga = []
        for j in range(n):
            riga.append(valore)
        matr.append(riga)
    return matr

def stampaMatrice(matr):
    for i in range(len(matr)):
        print("")
        for j in range(len(matr[i])):
            print(f"\t{matr[i][j]}", end = " ")
        print("")

def timer(secondi):
    # clear per sistema Mac
    # cls per sistema Windows
    os.system("clear")
    for i in range(secondi, 0, -1):
        print(f"{i}")
        time.sleep(1)
        os.system("clear")

def game():

    print("Trova il numero nascosto 3 tra gli tutti gli 8")
    print("Scegli la difficoltà: \n 1 › Facile \t 2 › Medio \t 3 › Difficile")
    difficolta = int(input("Scrivi qui: "))

    tempo = 0
    m = 0
    n = 0


    if difficolta == 1:
        tempo = 10
        m = 5
        n = 5
    elif difficolta == 2:
        tempo = 8
        m = 8
        n = 8
    elif difficolta == 3:
        tempo = 5
        m = 10
        n = 10
    else:
        print(f"{difficolta} scelta non valida")
        exit()

    # Creo una matrice popolata di 8
    matr = creaMatriceValore(m,n, 8)

    # Posizione random segreta del numero 3
    posX = random.randint(0, len(matr) - 1)
    posY = random.randint(0, len(matr) - 1)

    # Inserisco il numero 3 nella posizione segreta
    matr[posX][posY] = 3

    # Timer inizio gioco
    print(f"Il gioco sta per iniziare!")
    time.sleep(0.5)
    timer(5)

    stampaMatrice(matr)

    time.sleep(tempo)
    os.system("clear")

    print("Prova ad indovinare le coordinate!")

    # strip è una funzione per togliere gli spazi
    posXUtente = int(input("Indovina la riga: ").strip())
    posYUtente = int(input("Indovina la colonna: ").strip())

    print(f"{posX,posY, posXUtente, posYUtente}")

    if posX == posXUtente and posY == posYUtente:
        print("HAI VINTOO!!!")
    else:
        print("HAI PERSO!!!")

    time.sleep(1)
    rigioca = input("Se vuoi rigiocare premi 1, altrimenti premi un altro tasto: ").strip()
    if rigioca == "1":
        game()
    print("Grazie per aver giocato!")


game()
