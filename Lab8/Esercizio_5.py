# # TRACCIA DELL'ESERCIZIO
# Scrivete un programma che giochi a tic-tac-toe (in italiano, tris o schiera). Il tic-tactoe si gioca su una scacchiera
# 3 × 3, come quella qui raffigurata, da due giocatori
# che, a turno, posizionano in una casella libera il proprio simbolo (una croce per il
# primo giocatore e un cerchio per il secondo). Il giocatore che compone una schiera di
# tre propri simboli su una riga, una colonna o una diagonale, vince la partita. Il
# programma deve disegnare la scacchiera, chiedere all’utente le coordinate del suo
# prossimo simbolo, cambiare il giocatore di turno dopo ogni mossa e decretare il
# vincitore.

import sys


def victory_check(matrix):
    # Controllo delle righe
    for lis in matrix:
        c = 0
        for item in lis:
            if item == 'X':
                c += 1
            elif item == 'O':
                c -= 1

        if c == 3:
            return 1

        if c == -3:
            return 2

    # Controllo delle colonne
    for i in range(len(matrix)):
        c = 0
        for lis in matrix:
            if lis[i] == 'X':
                c += 1
            elif lis[i] == 'O':
                c -= 1

        if c == 3:
            return 1

        if c == -3:
            return 2

    # Controllo delle diagonali
    c = 0
    for i in range(len(matrix)):
        if matrix[i][i] == 'X':
            c += 1
        elif matrix[i][i] == 'O':
            c -= 1

    if c == 3:
        return 1

    if c == -3:
        return 2

    c = 0
    for i in range(len(matrix) - 1, -1, -1):
        if matrix[i][i] == 'X':
            c += 1
        elif matrix[i][i] == 'O':
            c -= 1

    if c == 3:
        return 1

    if c == -3:
        return 2

    return 0


def matrix_print(matrix):
    print('\n\n\n\n\n\n\n')
    for lis in matrix:
        for item in lis:
            print(item, end=' ')
        print()


def __main__():
    matrix = [['', '', ''], ['', '', ''], ['', '', '']]

    while True:
        matrix_print(matrix)

        okay = False
        while not okay:
            row = -1
            column = -1
            while (row < 0 or row > 2) and (column < 0 or column > 2):
                row = int(input('Giocatore 1; Inserisci la riga che vuoi riempire: ')) - 1
                column = int(input('Giocatore 1; Inserisci la colonna che vuoi riempire: ')) - 1

            if matrix[row][column] == '':
                okay = True
                matrix[row][column] = 'X'

        if victory_check(matrix) == 1:
            matrix_print(matrix)
            print('Il GIOCATORE 1 ha vinto')
            sys.exit()
        elif victory_check(matrix) == 2:
            matrix_print(matrix)
            print('Il GIOCATORE 2 ha vinto')
            sys.exit()

        matrix_print(matrix)

        okay = False
        while not okay:
            row = -1
            column = -1
            while (row < 0 or row > 2) and (column < 0 or column > 2):
                row = int(input('Giocatore 2; Inserisci la riga che vuoi riempire: ')) - 1
                column = int(input('Giocatore 2; Inserisci la colonna che vuoi riempire: ')) - 1

            if matrix[row][column] == '':
                okay = True
                matrix[row][column] = 'O'

        if victory_check(matrix) == 1:
            matrix_print(matrix)
            print('Il GIOCATORE 1 ha vinto')
            sys.exit()
        elif victory_check(matrix) == 2:
            matrix_print(matrix)
            print('Il GIOCATORE 2 ha vinto')
            sys.exit()


if __name__ == '__main__':
    __main__()
