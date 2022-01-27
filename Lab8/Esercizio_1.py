# # TRACCIA DELL'ESERCIZIO
# Scrivete la funzione merge(a, b) che “fonde” due liste, alternando un elemento
# della prima e un elemento della seconda. Se una lista è più corta dell’altra, gli
# elementi vengono alternati fin quando è possibile, poi gli elementi rimasti nella lista
# più lunga vengono aggiunti ordinatamente in fondo. Le liste di partenza non devono
# essere modificate. Se, ad esempio, il contenuto di a è 1 4 9 16 e il contenuto di b è
# 9 7 4 9 11, l’invocazione di merge(a, b) restituisce una nuova lista contenente i
# valori 1 9 4 7 9 4 16 9 11.

# @function merge è la funzione che fonderà a termini alterni le nostre due liste
# @param a la prima lista da fondere
# @param b la seconda lista da fondere
# @return lis la lista fusa
def merge(a, b):
    lis = list()
    c = 0

    # Controllo della più lunga delle due
    if len(a) > len(b):
        for item in b:
            lis.append(a[c])
            lis.append(item)
            c += 1

        # Completamente della lista fusa con gli elementi restanti della lista più lunga
        for i in range(c, len(a) + 1):
            lis.append(a[i])
    else:
        for item in a:
            lis.append(item)
            lis.append(b[c])
            c += 1

        for i in range(c, len(a) + 1):
            lis.append(b[i])

    return lis


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    a = [1, 4, 9, 16]
    b = [9, 7, 4, 9, 11]

    lis = merge(a, b)

    print('La lista a contiene: ')
    [print(item, end=' ') for item in a]

    print('\nLa lista b contiene: ')
    [print(item, end=' ') for item in b]

    print('\n\nLa lista fusa è composta da: ')
    [print(item, end=' ') for item in lis]


if __name__ == "__main__":
    __main__()
