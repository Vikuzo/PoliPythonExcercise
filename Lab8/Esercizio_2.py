# # TRACCIA DELL'ESERCIZIO
# Scrivete la funzione neighbor_average(values, row, column) che, in una
# tabella values, calcoli il valore medio dei vicini di un elemento nelle otto direzioni,
# come si può vedere nella figura sotto. Se, però, l’elemento si trova su un bordo della
# tabella, la media va calcolata considerando soltanto i vicini che appartengono
# effettivamente alla tabella. Ad esempio, se row e column valgono entrambe 0, ci
# sono soltanto tre vicini.

# @function neighbor_average fa la sommatoria di tutti i vicini di un elemento della matrice
# @param values è la matrice al cui interno si trovano i valori di cui fare il calcolo
# @param row la riga a cui cercare i valori
# @param column la colonna a cui cercare i valori
# @return average la somma dei vicini di quell'elemento
def neighbor_average(values, row, column):
    average = 0

    # Controlliamo se la colonna non è quella più a sinistra
    if column != 0:
        average += values[row][column - 1]
        if row != 0:
            average += values[row - 1][column - 1]
        if row != len(values) - 1:
            average += values[row + 1][column - 1]

    # Controlliamo se la colonna non è quella più a destra
    if column != len(values[0]) - 1:
        average += values[row][column + 1]
        if row != 0:
            average += values[row - 1][column + 1]
        if row != len(values) - 1:
            average += values[row + 1][column + 1]

    # Controlliamo se la riga non è quella più in "alto"
    if row != 0:
        average += values[row - 1][column]

    # Controlliamo se la riga non è quella più in "basso"
    if row != len(values) - 1:
        average += values[row + 1][column]

    return average


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print('La matrice di cui andremo a fare le somme dei vicini: ')

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

    print('\n\nLe somme dei vicini per elemento: ')

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(neighbor_average(matrix, i, j), end=' ')
        print()


if __name__ == "__main__":
    __main__()
