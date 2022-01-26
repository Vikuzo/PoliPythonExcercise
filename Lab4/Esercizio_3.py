# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che legga un numero intero, n, e visualizzi usando asterischi,
# un quadrato e un rombo pieni il cui lato abbia lunghezza n. Se, ad esempio, l’utente
# fornisce il numero 4, il programma deve visualizzare:

# @param n il numero intero che ci darà la lunghezza del lato
n = int(input('Inserire un numero intero che rappresenti la lunghezza del lato di un quadrato e di un rombo: '))

print('Un quadrato fatto di asterischi di lato %d: \n' % n)

for i in range(0, n, 1):
    for j in range(0, n, 1):
        print('*', end='')

    print()

print('\nUn rombo fatto di asterischi di lato %d: \n' % n)

# @aster il numero di asterischi da stampare su una singola riga
aster = 1

for i in range(0, n, 1):
    # @spaces il numero di spazi a destra e a sinistra degli asterischi
    spaces = (((n * 2) - 1) - aster)//2

    for j in range(spaces):
        print(' ', end='')

    for j in range(aster):
        print('*', end='')

    for j in range(spaces):
        print(' ', end='')

    aster += 2
    print()

# Va fatto per non far ripetere ulteriormente la riga centrale
aster -= 2

while aster > 0:
    aster -= 2

    spaces = (((n * 2) - 1) - aster) // 2

    for j in range(spaces):
        print(' ', end='')

    for j in range(aster):
        print('*', end='')

    for j in range(spaces):
        print(' ', end='')
    print()
