# # TRACCIA DELL'ESERCIZIO
# Scrivete la funzione sum_without_smallest che calcoli la somma di tutti i valori di
# una lista, escludendo il valore minimo.

# @function sum_without_smallest la funzione che si occuperà di sommare i valori della lista escluso il più piccolo
def sum_without_smallest(lis):
    lis.sort()

    tot = 0
    for i in range(1, len(lis)):
        tot += lis[i]

    return tot


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    lis = [2, 6, 78, 34, 12, 36, 98, 1]
    print('La somma dei numeri presenti nella lista eccetto il più piccolo è:', sum_without_smallest(lis))


if __name__ == "__main__":
    __main__()
