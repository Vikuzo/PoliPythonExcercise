# # TRACCIA DELL'ESERCIZIO
# Scrivete funzioni che risolvano i problemi seguenti per liste di numeri interi,
# fornendo un programma di collaudo per ciascuna funzione.
# a. Scambiare tra loro il primo e l’ultimo elemento della lista.
# b. Far scorrere tutti gli elementi di una posizione “verso destra”, spostando
# l’ultimo elemento nella prima posizione. Ad esempio, la lista 1 4 9 16 25
# deve diventare 25 1 4 9 16.
# c. Sostituire con 0 tutti gli elementi di valore pari.
# d. Sostituire ciascun elemento, tranne il primo e l’ultimo, con il più grande dei
# due elementi ad esso adiacenti. È possibile usare liste di appoggio.
# e. Eliminare l’elemento centrale della lista se questa ha dimensione dispari,
# altrimenti eliminare i due elementi centrali.
# f. Spostare tutti gli elementi pari all’inizio della lista (lasciando quelli dispari in
# coda), preservando però l’ordinamento relativo tra gli elementi.
# g. Restituire il secondo valore maggiore della lista (senza pari meriti).
# h. Restituire True se e solo se la lista è ordinata in senso crescente.
# i. Restituire True se e solo se la lista contiene due elementi adiacenti duplicati.
# j. Restituire True se e solo se la lista contiene elementi duplicati (non
# necessariamente adiacenti).

# # Sviluppo punto a)
# @function changing_first_with_last scambierà di posto il primo elemento e l'ultimo della lista
# @param a la lista di cui modificheremo primo e ultimo
def changing_first_with_last(a):
    a[0], a[-1] = a[-1], a[0]

    print("\n\nLa lista con il primo e l'ultimo elemento invertito è:")
    [print(item, end=' ') for item in a]


# # Sviluppo punto b)
# @function shifting a muove verso destra gli elementi della lista
# @param a la lista su cui effettueremo l'operazione
def shifting_right(a):
    a.insert(0, a[-1])
    a.pop()

    print('\n\nLa lista mossa di uno verso destra è:')
    [print(item, end=' ') for item in a]


# # Sviluppo del punto c)
# @function even_no_zero sostituisce tutti i valori pari della lista con 0
# @param a lista di cui elimineremo i valori pari
def even_no_zero(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] = 0

    print('\n\nLa lista con i numeri pari sostituiti da 0 è:')
    [print(item, end=' ') for item in a]


# # Sviluppo punto d)
# @function max_substitute sostituirà ogni valore con quello ad esso adiacente maggiore
# @param a la lista su cui effettueremo la sostituzione
def max_substitute(a):
    b = list(a)

    for i in range(1, len(a) - 1):
        if a[i - 1] > a[i + 1]:
            b[i] = b[i - 1]
        else:
            b[i] = b[i + 1]

    a = b
    print('\n\nLa lista prendendo il maggiore dei numeri adiacenti:')
    [print(item, end=' ') for item in a]


# # Sviluppo punto e)
# @function central_remove rimuove i valori centrali della lista
# @param a la lista su cui effettueremo le operazioni
def central_remove(a):
    if len(a) % 2 == 1:
        a.pop((len(a)//2) + 1)
    else:
        a.pop(len(a) // 2)
        a.pop((len(a) // 2))

    print("\n\nLa lista rimuovendo l'elemento centrale:")
    [print(item, end=' ') for item in a]


# # Sviluppo punto f)
# @function even_to_the_start mette i valori pari davanti
# @param a è la lista su cui effettueremo le operazioni
def even_to_the_start(a):
    b = []
    c = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append(a[i])
        else:
            c.append(a[i])

    b.extend(c)
    a = b

    print("\n\nLa lista portando i valori pari davanti è:")
    [print(item, end=' ') for item in a]


# # Sviluppo punto g)
# @function second_max restituisce il secondo termine massimo della lista
# @param a la lista su cui effettueremo le operazioni
def second_max(a):
    a.sort()
    a.reverse()

    c = 0
    run = True

    while run:
        if a[c + 1] != c:
            run = False
        else:
            c += 1

    print("\n\nIl secondo numero più grande della lista è:", a[c + 1])


# # Sviluppo punto h)
# @function check_increase_sort controlla se la lista è ordinata in modo crescente
# @param a la lista su cui effettueremo le operazioni
# @return True/False ritorna vero se sono uguali falso altrimenti
def check_increase_sort(a):
    b = list(a)
    b.sort()

    if a == b:
        return True

    return False


# # Sviluppo punto i)
# @function check_duplicate cerca dei duplicati adiacenti e restituisce vero se li trova
# @param a la lista su cui effettueremo le operazioni
# @return True/False ritorna false se esiste almeno un elemnto duplicato del precedente falso altrimenti
def check_duplicate(a):
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            return True

    return False


# # Sviluppo punto j)
# @function check_duplicate2 cerca duplicati anche fra valori non adiacenti
# @param a è la lista su cui effettueremo le operazioni
# @return True/False ritorna vero se è presente almeno un elemento duplicato altrimenti falso
def check_duplicate2(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                return True

    return False


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    a = [1, 4, 9, 16, 25]

    print('La lista originale è:')
    [print(item, end=' ') for item in a]

    changing_first_with_last(list(a))
    shifting_right(list(a))
    even_no_zero(list(a))
    max_substitute(list(a))
    central_remove(list(a))
    even_to_the_start(list(a))
    second_max(list(a))

    if check_increase_sort(list(a)):
        print('\n\nLa lista è ordinata in modo crescente')
    else:
        print('\n\nLa lista NON è ordinata in modo crescente')

    if check_duplicate(list(a)):
        print('\n\nEsiste almeno un duplicato adiacente')
    else:
        print('\n\nNON esiste nessun duplicato adiacente')

    if check_duplicate2(list(a)):
        print('\n\nEsiste almeno un duplicato')
    else:
        print('\n\nNON esistono duplicati')


if __name__ == '__main__':
    __main__()
