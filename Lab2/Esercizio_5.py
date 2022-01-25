# # TRACCIA DELL'ESERCIZIO
# Scrivere un programma che memorizzi in due variabili costanti le lunghezze dei lati
# di un rettangolo e visualizzi:
# • L’area e il perimetro del rettangolo
# • La lunghezza della sua diagonale

# Ci servirà importare la funzione "sqrt" dalla libreria math per svolgere il calcolo della diagonale. Da tenere bene a
# mente che con questo metodo di scrittura ci limitiamo ad importare la funzione sqrt dalla funzione math
from math import sqrt


# @param base lunghezza della base del rettangolo
BASE = int(input('Inserire la lunghezza della base del rettangolo: '))

# @param height lunghezza dell'altezza del rettangolo
HEIGHT = int(input("Inserire la lunghezza dell'altezza del rettangolo: "))

print("L'area del rettangolo è:", (BASE * HEIGHT))
print("Il perimetro del rettangolo è:", ((BASE * 2) + (HEIGHT * 2)))

# L'operatore % ci permette di inserire all'interno della nostra print una variabile in un secondo momento, inoltre
# ci permette di creare delle restrizioni in questo caso "%.2f" stiamo dicendo che inseriremo una variabile float e
# che le sue cifre decimali devo essere al massimo 2
print("La diagonale del rettangolo è: %.2f" % sqrt((BASE ** 2) + (HEIGHT ** 2)))
