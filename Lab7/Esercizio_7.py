# # TRACCIA DELL'ESERCIZIO
# Spesso i valori raccolti durante un esperimento vanno corretti, per togliere parte del
# rumore di misura. Un approccio semplice a questo problema prevede di sostituire, in
# una lista, ciascun valore con la media tra il valore stesso e i due valori adiacenti (o un
# unico adiacente se il valore in esame si trova a una delle due estremità della lista).
# Realizzate un programma che svolga tale operazione, senza creare un’altra lista.

# @function smooth si occupa di fare la media dei valori ravvicinati presenti all'interno della lista
# @param data la lista sulla quale verranno effettuate le operazioni
def smooth(data):
    if len(data) <= 1:
        return

    # In old_left salviamo la variabile che andremo a modificare per evitare poi di trovarci con delle approssimazioni
    # sballate
    old_left = data[0]
    data[0] = (data[0] + data[1]) / 2

    for i in range(1, len(data) - 1):
        current = data[i]
        data[i] = (old_left + data[i] + data[i + 1]) / 3
        old_left = current

    data[len(data) - 1] = (old_left + data[len(data) - 1]) / 2


# @function __main__ la funzione che si occupa del lancio del programma
def __main__():
    value = [1, 2, 3, 4, 5]
    print('I valori originali sono: ')
    for item in value:
        print(item, end=' ')

    print('\n\n')

    smooth(value)

    print('I valori modificati sono: ')
    for item in value:
        print(item, end=' ')


if __name__ == '__main__':
    __main__()
