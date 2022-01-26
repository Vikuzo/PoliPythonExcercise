# # TRACCIA DELL'ESERCIZIO
# Fattorizzazione di interi. Scrivete un programma che chieda all’utente un numero
# intero e ne visualizzi i fattori. Se, ad esempio, l’utente fornisce il numero 150, il
# programma deve visualizzare:
# 2
# 3
# 5
# 5

# @param number il numero su cui effettueremo le operazioni
number = int(input('Inserire il numero che si vuole fattorializzare: '))

# @param c ci servirà per torvare i fattori di number
c = 2

while number != 1:
    if number % c == 0:
        print(c)
        number //= c
    else:
        c += 1
