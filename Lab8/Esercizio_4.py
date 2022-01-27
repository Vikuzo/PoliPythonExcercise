# # TRACCIA DELL'ESERCIZIO
# Scrivete la funzione merge_sorted(a, b) che fonde due liste ordinate (si supponga
# quindi che siano già ordinate in modo crescente), restituendo una nuova lista
# ordinata in modo crescente. Gestite un indice corrente per ciascuna lista, in modo da
# tenere traccia della porzione già elaborata. Le liste di partenza non devono essere
# modificate. Se, ad esempio, il contenuto di a è 1 4 9 16 e il contenuto di b è 4 7 9
# 9 11, l’invocazione merge_sorted(a, b) restituisce una nuova lista contenente i
# valori 1 4 4 7 9 9 9 11 16. Non utilizzare il metodo sort né la funzione sorted
# (sfruttare l’informazione che gli elementi di ciascuna lista sono già ordinati per
# ottenere una soluzione più efficiente).

# @function merge_sorted ordina in modo crescente la fusione delle due liste
# @param a la prima lista da fondere
# @param b la seconda lista da fondere
# @return lis la lisat fusa in ordine crescente
def merge_sorted(a, b):
    # Contatore di a
    ca = 0

    # Contatore di b
    cb = 0

    lis = list()

    while ca < len(a) and cb < len(b):
        if a[ca] < b[cb]:
            lis.append(a[ca])
            ca += 1
        else:
            lis.append(b[cb])
            cb += 1

    if ca == len(a):
        for i in range(cb, len(b)):
            lis.append(b[i])
    else:
        for i in range(ca, len(a)):
            lis.append(a[i])

    return lis


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    a = [1, 4, 9, 16]
    b = [4, 7, 9, 9, 11]

    print('Gli elementi della lista a sono: ')
    [print(item, end=' ') for item in a]

    print('\nGli elementi della lista b sono: ')
    [print(item, end=' ') for item in b]

    print('\n\nGli elementi della fusione delle due liste ordinati sono: ')
    [print(item, end=' ') for item in merge_sorted(a, b)]


if __name__ == '__main__':
    __main__()
