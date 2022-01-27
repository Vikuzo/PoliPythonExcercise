# # TRACCIA DELL'ESERCIZIO
# Quadrati magici. Una matrice n × n contenente i numeri interi 1, 2, 3, ..., n^2
# è un
# quadrato magico se la somma dei suoi elementi in ciascuna riga, in ciascuna colonna
# e nelle due diagonali ha lo stesso valore.
# Scrivete un programma che acquisisca in ingresso 16 valori e verifichi se, dopo
# averli disposti in una tabella 4 × 4 ordinatamente per righe, da sinistra a destra e
# dall’alto in basso, formano un quadrato magico. Dovete verificare due proprietà:
# 1. Nei dati acquisiti sono presenti tutti e soli i numeri 1, 2, ..., 16?
# 2. Quando i numeri vengono disposti nella tabella, le somme delle righe, delle
# colonne e delle diagonali sono tutte uguali l’una all’altra?

import sys


# @function is_magical_square controlla se il quadrato inserito è un quadrato magico oppure no
# @param square è il quadrato su cui effettuerà i controlli
# @return True/False ritornerà True se è un quadrato magico altrimenti False
def is_magical_square(square):
    som = 0
    for item in square[0]:
        som += item

    # Controllo se le somme delle colonne sono uguali
    for lis in square:
        relative_som = 0
        for item in lis:
            relative_som += item

        if relative_som != som:
            return False

    # Controllo se le somme delle righe sono uguali
    for i in range(0, len(square)):
        relative_som = 0
        for lis in square:
            relative_som += lis[i]

        if relative_som != som:
            return False

    relative_som = 0

    # Controllo se le somme delle diagonali sono uguali
    for i in range(0, len(square)):
        relative_som += square[i][i]

    if relative_som != som:
        return False

    relative_som = 0

    for i in range(len(square) - 1, -1, -1):
        relative_som += square[i][i]

    if relative_som != som:
        return False

    return True


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    # @param n lunghezza del lato del nostro quadrato magico
    n = 4

    square = list()
    lis = list()

    for i in range(0, (n ** 2)):
        lis.append(int(input('Inserire un numero intero da 1 a 16: ')))

        if (i + 1) % n == 0 and i != 0:
            square.append(lis)
            lis = list()

    # Controllo se i numeri sono da 1 a 16
    checking_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for lis in square:
        for item in lis:
            if item not in checking_data:
                sys.exit('Errore di inserimento nei dati')

    if is_magical_square(square):
        print('Il quadrato inserito è un quadrato magico')
    else:
        print('Il quadrato inserito NON è un quadrato magico')


if __name__ == '__main__':
    __main__()
