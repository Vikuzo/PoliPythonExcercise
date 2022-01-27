# # TRACCIA DELL'ESERCIZIO
# Scrivere un programma che acquisisca dall’utente un elenco di numeri interi positivi,
# scritti su un’unica riga e separati dal carattere ‘:’.
# Esempio: 3:12:21:8:4:7
# Il programma dovrà stampare, sempre nello stesso formato:
# - gli stessi numeri, ad eccezione del minimo e del massimo (es. 12:8:4:7)
# - i soli numeri pari (es. 12:8:4)
# - i soli numeri di 2 cifre (es. 12:21)
# Si suggerisce di lavorare costruendo una lista di numeri interi.

# @function make_list rende la stringa una lista
# @param sequence è la stringa da rendere lista
# @return lis ritorna la lista generata dalla stringa data
def make_list(sequence):
    lis = []

    cs = 0
    ce = 0

    for i in range(len(sequence)):
        if sequence[i] == ':':
            lis.append(int(sequence[cs:ce]))
            cs = ce + 1
        ce += 1

    if len(sequence) > 0:
        lis.append(int(sequence[cs:]))

    return lis


# @function make_string trasforma una lista in stringa
# @param lis la lista che trasformeremo in stringa
# @return sequence ritorniamo la lista trasformata in stringa con i due punti a separare gli elementi
def make_string(lis):
    sequence = ''

    for i in range(len(lis) - 1):
        sequence += str(lis[i]) + ':'

    if len(lis) > 0:
        sequence += str(lis[-1])

    return sequence


# @function without_max_and_min elimina il minimo ed il massimo
# @param a è la lista che passiamo
def without_max_and_min(a):
    a.sort()
    a.remove(a[0])
    a.remove(a[-1])

    print('\n\nLa sequenza numerica privata del massimo e del minimo: ', end='')
    a = make_string(a)
    print(a)


# @function only_even lascia solo i numeri pari
# @param a la lista su cui effettueremo l'operazione
def only_even(a):
    for item in a:
        if item % 2 == 0:
            a.remove(item)

    print('\n\nLa sequenze numerica privata dei numeri pari è: ', end='')
    a = make_string(a)
    print(a)


# @function only_double_digits lascia solo i numeri a due cifre
# @param a la lista su cui effettueremo l'operazione
def only_double_digits(a):
    for item in a:
        if item < 10 or item > 99:
            a.remove(item)

    print('\n\nLa sequenze numerica privata dei non a due cifre: ', end='')
    a = make_string(a)
    print(a)


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    sequence = input("Inserire una sequenza di interi separati dal simbolo ':': ")

    without_max_and_min(make_list(sequence))
    only_even(make_list(sequence))
    only_double_digits(make_list(sequence))


if __name__ == "__main__":
    __main__()
