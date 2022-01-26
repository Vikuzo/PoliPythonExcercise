# # TRACCIA DELL'ESERCIZIO
# Scrivete la funzione def sameSet(a, b) che verifichi se due liste contengono gli
# stessi elementi, indipendentemente dall’ordine e ignorando la presenza di duplicati.
# Ad esempio, le due liste 1 4 9 16 9 7 4 9 11 e 11 11 7 9 16 4 1 devono essere
# considerate uguali. La funzione non deve modificare le liste ricevute come parametri.

# @function same_set funzione che compare due liste e ritorna se contengono gli stessi valori oppure no
# @param a prima delle due liste da confrontare
# @param b seconda lista delle due da confrontare
def same_set(a, b):
    for item in a:
        if item not in b:
            return False

    for item in b:
        if item not in a:
            return False

    return True


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    b = [11, 11, 7, 9, 16, 4, 1]

    print('Lista A:', end=' ')
    for item in a:
        print(item, end=' ')
    print()

    print('Lista B:', end=' ')
    for item in b:
        print(item, end=' ')
    print()

    if same_set(a, b):
        print('Le due liste sono uguali')
    else:
        print('Le due liste contengono gli stessi elementi')


if __name__ == "__main__":
    __main__()
